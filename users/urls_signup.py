from users.views import UserSignupView

from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    path('', UserSignupView.as_view(), name="user_signup"),
]
