from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostDocumentViewSet

router = DefaultRouter()
router.register(r"document", PostDocumentViewSet, basename="post-document")
router.register(r"", PostViewSet, basename="post")


urlpatterns = [
    path("", include(router.urls)),
]
