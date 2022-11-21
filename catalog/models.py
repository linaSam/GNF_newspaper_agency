from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from newspaper_agency import settings


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("catalog:redactor-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(auto_now=False)
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    redactors = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="newspapers")

    def __str__(self):
        return f"{self.title}: {self.content}, {self.published_date}"
