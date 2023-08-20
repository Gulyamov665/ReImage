from django.urls import path
from .views import ProductCreateView, ImageResizeView

urlpatterns = [
    path("new-product", ProductCreateView.as_view(), name="create_product"),
    path("resize", ImageResizeView.as_view(), name="resize")
]
