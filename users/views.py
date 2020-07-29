import json
import sys

from django.contrib.auth import (
    get_user_model,
    login as django_login,
    logout as django_logout,
)
from django.core.serializers import serialize
from django.http import Http404
from django.shortcuts import render
from django.utils import timezone

from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import Profile
from users.serializers import (
    AuthCustomTokenSerializer,
    ProfileSerializer,
    UserModelSerializer
)

User = get_user_model()


class UserSignupView(APIView):

    def post(self, request, format=None):
        serializer = UserModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserObjectAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProfileSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)


def get_current_datetime():
    return timezone.now().astimezone(timezone.get_default_timezone())


class LoginAPIView(APIView):

    def post(self, request, forma=None):
        serializer = AuthCustomTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')

        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)

        if not created:
            user = token.user
            token.delete()
            token = Token.objects.create(user=user)
            token.created = get_current_datetime()
            token.save()

        return Response({'token': token.key}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):

    def post(self, request, format=None):
        try:
            token = Token.objects.get(key=request.user.auth_token)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        token.delete()
        return Response(status=status.HTTP_200_OK)


class UpdateUserAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({
                'error': 'True',
                'message': 'User profile not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        profile = self.get_object(pk)
        serializer = UserModelSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
