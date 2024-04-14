from django.urls import path
from .views import (
    DownloadFilesView,
    ProductCreateView,
    ImageResizeView,
    DetailAllApiView,
    DetailUserApiView,
    apiOverview,
    ImagesApiView,
    export_xlsx,
    PromoStickerView,
    VendorImageViews,
    PromoView
)


urlpatterns = [
    path("", apiOverview, name="api_overview"),
    path("api/create", ProductCreateView.as_view(), name="create"),
    path("api/images", ImagesApiView.as_view({"post": "create"}), name="images"),
    path("api/resize_image", ImageResizeView.as_view(), name="resize_image"),
    path("api/download/<str:name>", DownloadFilesView.as_view(), name="download"),
    path("api/export/<str:name>", export_xlsx, name="export"),
    path("api/detail/<int:user_id>", DetailUserApiView.as_view(), name="detail_user"),
    path("api/detail", DetailAllApiView.as_view(), name="detail"),
    path("api/detail_user", DetailUserApiView.as_view(), name="detail_user"),
    path("api/sticker", PromoStickerView.as_view({"post":"sticker"}), name="sticker"),
    path("api/stick", PromoView.as_view({"get":"list"}), name="sticker"),
    path("api/sticker/create", PromoStickerView.as_view({"post":"create"}), name="sticker-create"),
    path("api/sticker/<str:name>", PromoStickerView.as_view({"get":"download"}), name="sticker-download"),
    path("api/vendor/create", VendorImageViews.as_view({"post":"create"}), name="vendor-create"),
]
