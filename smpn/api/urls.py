from django.urls import path

from .views import userView, inventoryView, inventoryQty, loggingView, inventoryDetail, InventoryPost

app_name = "api"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', userView.as_view()),

    path('inventory/', inventoryView.as_view()),
    path('inventory/post/', InventoryPost.as_view()),
    path('inventory/qty/<get_uid>', inventoryQty.as_view()),
    path('inventory/detail/<detailed_uid>', inventoryDetail.as_view()),
    path('inventory/update/<logical_uid>', inventoryView.as_view()),

    path('logging/', loggingView.as_view()),
]