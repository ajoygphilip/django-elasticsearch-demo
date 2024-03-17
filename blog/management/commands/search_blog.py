# Import necessary modules
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Author
import sys
from icecream import ic
from blog.documents import BlogDocument, AuthorDocument


# Define your command class
class Command(BaseCommand):
    help = "Populates UserProfile model with data from a web API"

    def add_arguments(self, parser):
        parser.add_argument("action", type=str)
        parser.add_argument("arg1", nargs="?", type=str)
        parser.add_argument("arg2", nargs="?", type=str)
        parser.add_argument("arg3", nargs="?", type=str)

    def handle(self, *args, **kwargs):
        q = sys.argv[2]

        s = BlogDocument.search().filter("match", title=q)

        # s = BlogDocument.search().query("match", title=q)

        for hit in s:
            ic(hit.title)
