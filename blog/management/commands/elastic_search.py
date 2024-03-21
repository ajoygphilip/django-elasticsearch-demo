# Import necessary modules
from django.core.management.base import BaseCommand
import sys
from icecream import ic
from django_elasticsearch_dsl.search import Search
from elasticsearch_dsl import Q


# Define your command class
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("action", type=str)
        parser.add_argument("arg1", nargs="?", type=str)
        parser.add_argument("arg2", nargs="?", type=str)
        parser.add_argument("arg3", nargs="?", type=str)

    def handle(self, *args, **kwargs):
        q = sys.argv[2]
        q2 = sys.argv[3]
        search_obj = Search()

        search_obj = search_obj.query("match", title=q).filter(
            "match", author__last_name=q2
        )

        # search_obj = search_obj.query(q)
        for h in search_obj:
            ic(h.title, h.author)
