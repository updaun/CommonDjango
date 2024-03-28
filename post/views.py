from rest_framework import viewsets
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .models import Post
from .serializers import PostSerializer
from .documents import PostDocument
from .doc_serializers import PostDocumentSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDocumentViewSet(DocumentViewSet):
    document = PostDocument
    serializer_class = PostDocumentSerializer
