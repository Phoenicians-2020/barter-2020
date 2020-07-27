from users.views import LoginAPIView

from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    path('', LoginAPIView.as_view(), name="user_signup"),
]
