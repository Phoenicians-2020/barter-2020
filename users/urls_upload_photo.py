from users.views import UploadProfilePhotoAPIView

from django.conf.urls import url
from django.urls import include, path

from rest_framework import routers

router = routers.DefaultRouter()

router.register('', UploadProfilePhotoAPIView, basename="user_upload_photo")

urlpatterns = [
    path('', include(router.urls)),
]
