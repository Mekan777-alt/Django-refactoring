from django.urls import path
from rest_framework.routers import DefaultRouter

from real_estate.api.views.leases import LeaseAPIView
from real_estate.api.views.real_estate_object import RealEstateObjectAPIView
from real_estate.api.views.type import RealEstateObjectTypeAPIView

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend([
    path('real-estate-object-types', RealEstateObjectTypeAPIView.as_view()),
    path('real-estate-object', RealEstateObjectAPIView.as_view()),
    path('real-estate-object/<int:pk>/leases', LeaseAPIView.as_view()),
])
