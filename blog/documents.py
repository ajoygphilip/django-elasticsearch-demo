from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Author, Blog


@registry.register_document
class BlogDocument(Document):

    author = fields.ObjectField(
        properties={
            "first_name": fields.TextField(),
            "last_name": fields.TextField(),
        }
    )

    class Index:
        name = "blog"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Blog

        fields = ["title", "description", "content_text"]
        ignore_signals = True
        auto_refresh = False


@registry.register_document
class AuthorDocument(Document):
    class Index:
        name = "author"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Author

        fields = ["first_name", "last_name"]
        ignore_signals = True
        auto_refresh = False
