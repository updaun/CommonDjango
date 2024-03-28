from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import PostDocument


class PostDocumentSerializer(DocumentSerializer):
    class Meta:
        document = PostDocument
        fields = (
            "id",
            "title",
            "content",
        )

    def get_location(self, obj):
        try:
            return obj.location.to_dict()
        except:
            return {}
