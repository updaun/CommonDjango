from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django.conf import settings
from post.models import Post


post_index = f"{settings.ELASTICSEARCH_DSL['default']['index_prefix']}post"


@registry.register_document
class PostDocument(Document):
    title = fields.TextField(attr="title")
    content = fields.TextField(attr="content")

    class Index:
        name = post_index
        settings = {"number_of_shards": 1, "number_of_replicas": 0}
        using = "default"

    class Django:
        model = Post
        fields = [
            "id",
        ]
