from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import Topic, Newspaper


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="test")

        self.assertEqual(
            str(topic), topic.name
        )

    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="test",
            password="test123",
            first_name="test first",
            last_name="test last",
            years_of_experience=2
        )

        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})",
        )

    def test_redactor_get_absolute_url(self):
        redactor = get_user_model().objects.create_user(
            id=1,
            username="test",
            password="test123",
            first_name="test first",
            last_name="test last",
            years_of_experience=2
        )
        self.assertEqual(redactor.get_absolute_url(), "/redactors/1/")

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="test")
        newspaper = Newspaper.objects.create(
            title="test",
            content="test",
            published_date="2022-04-21",
            topic=topic
        )

        self.assertEqual(str(newspaper), f"{newspaper.title}: {newspaper.content}, {newspaper.published_date}")
