from users.views import UpdateUserAPIView

from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    path('', UpdateUserAPIView.as_view(), name="user_signup"),
]
