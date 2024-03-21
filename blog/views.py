from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from elasticsearch_dsl import Q
from icecream import ic
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
