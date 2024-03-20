from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_elasticsearch_dsl.search import Search
from elasticsearch_dsl import Q
from icecream import ic
from blog.serializers import BlogDocumentSerializer
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from blog.documents import BlogDocument


class BlogDocumentViewset(BaseDocumentViewSet):
    document = BlogDocument
    serializer_class = BlogDocumentSerializer
    search_fields = (
        "title",
        "content_text",
        "author__last_name",
    )
