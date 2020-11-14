from django.urls import path

from .views import userView, inventoryView, loggingView

app_name = "users"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', userView.as_view()),
    # path('users/update/<int:update_user_pk>', userView.as_view()),
    # path('users/delete/<int:delete_user_pk>', userView.as_view()),

    path('inventory/', inventoryView.as_view()),
    path('inventory/update/<uid>', inventoryView.as_view()),

    path('logging/', loggingView.as_view()),
]