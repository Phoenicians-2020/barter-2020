from users.views import LogoutAPIView

from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    path('', LogoutAPIView.as_view(), name="user_signup"),
]
