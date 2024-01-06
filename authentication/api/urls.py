from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.api.view.registration import RegistrationAPIView

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend([
    path('auth/registration', RegistrationAPIView.as_view()),
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
])
