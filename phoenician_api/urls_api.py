from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    path('users/signup/', include('users.urls_signup')),
    path('users/', include('users.urls_list')),
    path('users/<int:pk>/', include('users.urls_user')),
    path('users/login/', include('users.urls_login')),
    path('users/logout/', include('users.urls_logout')),
]
