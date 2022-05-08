from django.urls import path


from .views import registration_view, MyTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView 

urlpatterns = [
    path('register/', registration_view, name='register'),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
