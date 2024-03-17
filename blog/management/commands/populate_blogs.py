from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from blog.models import Author, Blog
from icecream import ic
from random import choice
from faker import Faker
from random import choice, randint


# Define your command class
class Command(BaseCommand):
    help = "Populates Blog model with data from a web API"

    def handle(self, *args, **kwargs):
        fake = Faker()
        authors = Author.objects.all()

        for _ in range(100):

            paragraphs = []
            num_sentences = randint(3, 6)
            num_paras = randint(3, 5)

            for _ in range(num_paras):
                sentences = []
                for _ in range(num_sentences):
                    sentence_length = randint(10, 20)
                    sentence = fake.sentence(nb_words=sentence_length)
                    sentences.append(sentence.strip())
                paragraph = " ".join(sentences)
                paragraphs.append(paragraph)

            title = fake.sentence()[:-1]
            category = fake.word()
            description = fake.sentence()
            content_text = "\n\n".join(paragraphs)
            content_html = "".join([f"<p>{p}</p>" for p in paragraphs])

            author = choice(authors)
            blog = Blog.objects.create(
                author=author,
                title=title,
                description=description,
                category=category,
                content_text=content_text,
                content_html=content_html,
            )
            blog.save()
            if blog:
                ic(f"{blog} ")
