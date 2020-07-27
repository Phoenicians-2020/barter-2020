from users.views import UserObjectAPIView

from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    path('', UserObjectAPIView.as_view(), name="user_signup"),
]
