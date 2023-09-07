from django.urls import path
from .views import (
    DownloadFilesView,
    ProductCreateView,
    ImageResizeView,
    DetailAllApiView,
    DetailUserApiView,
    apiOverview,
    ImagesApiView,
)


urlpatterns = [
    path("", apiOverview, name="api_overview"),
    path("api/create", ProductCreateView.as_view(), name="create"),
    path("api/images", ImagesApiView.as_view({"post": "create"}), name="images"),
    path("api/resize_image", ImageResizeView.as_view(), name="resize_image"),
    path("api/download/<str:name>", DownloadFilesView.as_view(), name="download"),
    path("api/detail/<int:user_id>", DetailUserApiView.as_view(), name="detail_user"),
    path("api/detail", DetailAllApiView.as_view(), name="detail"),
    path("api/detail_user", DetailUserApiView.as_view(), name="detail_user"),
]
