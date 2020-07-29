import sys

from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
import django.contrib.auth.password_validation as validators

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Profile

User = get_user_model()


class UserModelSerializer(serializers.ModelSerializer):
    """
    User model serializer class with UniqueValidators for user's email account
    """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'password',
            'confirm_password',
        )

    def create(self, validated_data):
        password = validated_data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password == confirm_password:
            user = User(
                email=validated_data.get('email'),
                name=validated_data.get('name')
            )
            user.set_password(password)
            user.save()

        user_profile = Profile(
            user=user
        )
        user_profile.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile serializer class
    """

    class Meta:
        model = Profile
        fields = '__all__'


class AuthCustomTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            try:
                validate_email(username)
                user_request = get_object_or_404(User, email=username)
                username = user_request.username
            except ValidationError as e:
                return Response({
                    "status": 400,
                    "error": True,
                    "message": str(e),
                })

            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to login with the provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include email/phone number and a password.')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs
