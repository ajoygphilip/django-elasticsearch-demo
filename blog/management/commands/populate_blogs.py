# Import necessary modules
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Author, Blog
import requests
from icecream import ic
from random import choice


# Define your command class
class Command(BaseCommand):
    help = "Populates Blog model with data from a web API"

    def handle(self, *args, **kwargs):

        for id in range(1, 11):
            url = f"https://api.slingacademy.com/v1/sample-data/blog-posts/{id}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()["blog"]
                author = Author.objects.get(id=id)

                if Blog.objects.filter(title=data["title"]).first():
                    ic(f"{data['title']} exist skipping")
                    continue

                blog, created = Blog.objects.get_or_create(
                    author=author,
                    defaults={
                        "title": data["title"],
                        "description": data["description"],
                        "category": data["category"],
                        "content_text": data["content_text"],
                        "content_html": data["content_html"],
                    },
                )

                if blog:
                    ic(f"{blog} created")
