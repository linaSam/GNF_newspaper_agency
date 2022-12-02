from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import Topic, Newspaper, Redactor

TOPIC_URL = reverse("catalog:topic-list")
NEWSPAPER_URL = reverse("catalog:newspaper-list")
NEWSPAPER_DETAIL_URL = reverse("catalog:newspaper-detail", kwargs={"pk": 1})
REDACTOR_URL = reverse("catalog:redactor-list")
REDACTOR_DETAIL_URL = reverse("catalog:newspaper-detail", kwargs={"pk": 1})


class PublicTopicTests(TestCase):
    def test_topic_login_required(self):
        res = self.client.get(TOPIC_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "password123")
        self.client.force_login(self.user)

    def test_retrieve_topic(self):
        Topic.objects.create(name="Test1")
        Topic.objects.create(name="Test2")

        response = self.client.get(TOPIC_URL)
        topics = Topic.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]), list(topics)
        )
        self.assertTemplateUsed(response, "catalog/topic_list.html")


class PublicNewspaperTests(TestCase):
    def test_newspaper_login_required(self):
        res = self.client.get(NEWSPAPER_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_newspaper_login_required_for_detail(self):
        res = self.client.get(NEWSPAPER_DETAIL_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateNewspaperTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "password123")
        self.client.force_login(self.user)

    def test_retrieve_newspaper(self):
        topic = Topic.objects.create(name="test")
        Newspaper.objects.create(
            title="test1",
            published_date="2022-01-23",
            topic=topic
        )
        Newspaper.objects.create(
            title="test2",
            published_date="2022-01-23",
            topic=topic
        )

        response = self.client.get(NEWSPAPER_URL)
        newspapers = Newspaper.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["newspaper_list"]), list(newspapers))
        self.assertTemplateUsed(response, "catalog/newspaper_list.html")


class PublicRedactorTests(TestCase):
    def test_login_required(self):
        res = self.client.get(REDACTOR_URL)

        self.assertNotEqual(res.status_code, 200)

    def test_redactor_login_required_for_detail(self):
        res = self.client.get(REDACTOR_DETAIL_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "password123")
        self.client.force_login(self.user)

    def test_retrieve_redactor(self):
        Redactor.objects.create(username="test1", years_of_experience=1)
        Redactor.objects.create(username="test2", years_of_experience=2)

        response = self.client.get(REDACTOR_URL)
        redactors = Redactor.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["redactor_list"]), list(redactors))
        self.assertTemplateUsed(response, "catalog/redactor_list.html")
