from django.urls import path

from .views import loggingView, inventoryView, inventoryQty, inventoryDetail, UserList, current_user

app_name = "api"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),

    path('inventory/', inventoryView.as_view()),
    path('inventory/qty/<get_uid>', inventoryQty.as_view()),
    path('inventory/detail/<detailed_uid>', inventoryDetail.as_view()),
    path('inventory/update/<logical_uid>', inventoryView.as_view()),

    path('logging/', loggingView.as_view()),
]