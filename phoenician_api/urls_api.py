from django.conf.urls import url
from django.urls import include, path

urlpatterns = [
    path('users/signup/', include('users.urls_signup')),
    path('users/', include('users.urls_list')),
    path('users/<int:pk>/', include('users.urls_user')),
    path('users/login/', include('users.urls_login')),
    path('users/logout/', include('users.urls_logout')),
    path('users/update/<int:pk>/', include('users.urls_user_update')),
    path('users/upload-photo/', include('users.urls_upload_photo')),

    path('products/create/', include('products.urls_create_product'))
]
