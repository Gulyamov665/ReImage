from django.urls import path
from .views import ProductCreateView, ImageResizeView, DetailAllApiView, UserCreateAPI, DetailUserApiView, apiOverview

urlpatterns = [
    path("", apiOverview, name="api_overview"),
    path("api/create", ProductCreateView.as_view(), name="create"),
    path("api/detail/<int:user_id>", DetailUserApiView.as_view(), name="detail_user"),
    path("api/detail", DetailAllApiView.as_view(), name="detail"),
    path("api/create_user", UserCreateAPI.as_view(), name="create_user"),
    path("api/detail_user", DetailUserApiView.as_view(), name="detail_user"),
    path("api/resize_image", ImageResizeView.as_view(), name="resize_image"),
]
