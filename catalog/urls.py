from django.urls import path

from .views import (
    index,
    NewspaperListView,
    NewspaperDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    RedactorListView,
    RedactorDetailView,
    RedactorCreationView,
    RedactorDeleteView,
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    toggle_assign_to_newspaper, RedactorUpdateView, register_request,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topic/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "topic/create/",
        TopicCreateView.as_view(),
        name="topic-create",
    ),
    path(
        "topic/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update",
    ),
    path(
        "topic/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete",
    ),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path(
        "newspapers/<int:pk>/toggle-assign/",
        toggle_assign_to_newspaper,
        name="toggle-newspaper-assign",
    ),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path(
        "redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"
    ),
    path("redactor/create", RedactorCreationView.as_view(), name="redactor-create"),
    path(
        "redactor/<int:pk>/update",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
    path(
        "redactor/<int:pk>/delete",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path("register/", register_request, name="register")
]

app_name = "catalog"
