from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ItemCreateView, ItemDetailView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Item CRUD routes
    path('items/', ItemCreateView.as_view(), name='create_item'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),

]
