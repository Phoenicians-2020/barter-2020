from users.views import UserListAPIView

from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    path('', UserListAPIView.as_view(), name="user_signup"),
]
