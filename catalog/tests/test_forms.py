from django.test import TestCase

from catalog.forms import (
    RedactorCreationForm,
    RedactorSearchForm,
    NewspaperSearchForm,
    RedactorYearsOfExperienceForm,
    TopicSearchForm,
)
from catalog.models import Redactor, Newspaper, Topic


class FormsTests(TestCase):
    def test_redactor_creation_form(self):
        data = {
            "username": "test",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "test_first",
            "last_name": "test_last",
            "years_of_experience": 4
        }
        form = RedactorCreationForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)

    def test_redactor_update_correct_redactor_years_of_experience_form(self):
        data = {"years_of_experience": 4}
        form = RedactorYearsOfExperienceForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)

    def test_redactor_search_form_valid_data(self):
        redactor = Redactor.objects.create(
            username="test",
            years_of_experience=4
        )
        data = {"redactor_0": redactor.username}
        form = RedactorSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_newspaper_search_form_valid_data(self):
        topic = Topic.objects.create(name="test")
        newspaper = Newspaper.objects.create(
            title="test",
            content="test",
            published_date="2022-01-22",
            topic=topic,
        )
        data = {"newspaper_0": newspaper.title}
        form = NewspaperSearchForm(data=data)
        self.assertTrue(form.is_valid())

    def test_topic_search_form_valid_data(self):
        topic = Topic.objects.create(name="test")
        data = {"topic_0": topic.name}

        form = TopicSearchForm(data=data)
        self.assertTrue(form.is_valid())
