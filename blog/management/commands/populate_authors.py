# Import necessary modules
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Author
import requests
from icecream import ic


# Define your command class
class Command(BaseCommand):
    help = "Populates UserProfile model with data from a web API"

    def handle(self, *args, **kwargs):

        response = requests.get("https://api.slingacademy.com/v1/sample-data/users")

        if response.status_code == 200:
            data = response.json()

            for item in data["users"]:

                user, created = User.objects.get_or_create(
                    username=f'{item["first_name"]}_{item["last_name"]}',
                    defaults={"email": item["email"]},
                )

                profile, created = Author.objects.get_or_create(
                    user=user,
                    defaults={
                        "first_name": item["first_name"],
                        "last_name": item["last_name"],
                        "phone": item.get("phone", ""),
                        "city": item["city"],
                        "state": item["state"],
                        "country": item["country"],
                        "zipcode": item["zipcode"],
                    },
                )

                if profile:
                    ic(f"profile created for {user.username}")
