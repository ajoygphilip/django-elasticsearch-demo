import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from blog.documents import BlogDocument


class BlogDocumentSerializer(DocumentSerializer):

    class Meta:
        document = BlogDocument

        felids = ["title", "author", "description", "content_text"]
