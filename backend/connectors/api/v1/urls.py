from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137792ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137792", Testconnectors137792ViewSet, basename="testconnectors137792"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
