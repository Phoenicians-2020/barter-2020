from products.views import CreateProductAPIView

from django.conf.urls import url
from django.urls import include, path


urlpatterns = [
    path('', CreateProductAPIView.as_view(), name="product_create"),
]
