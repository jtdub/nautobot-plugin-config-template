"""Config Template url definitions."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.extras.views import ObjectChangeLogView

from config_template import models, views

app_name = "config-template"

urlpatterns = [
    path("", views.ConfigTemplateListView.as_view(), name="configtemplatemodel_list"),
    path("add/", views.ConfigTemplateEditView.as_view(), name="configtemplatemodel_add"),
    path("<str:slug>/", views.ConfigTemplateView.as_view(), name="configtemplatemodel"),
    path("<str:slug>/edit/", views.ConfigTemplateEditView.as_view(), name="configtemplatemodel_edit"),
    path("<str:slug>/delete/", views.ConfigTemplateDeleteView.as_view(), name="configtemplatemodel_delete"),
    path("<uuid:pk>/", views.ConfigTemplateView.as_view(), name="configtemplatemodel"),
    path("<uuid:pk>/edit/", views.ConfigTemplateEditView.as_view(), name="configtemplatemodel_edit"),
    path("<uuid:pk>/delete/", views.ConfigTemplateDeleteView.as_view(), name="configtemplatemodel_delete"),
    path(
        "<uuid:pk>/changelog/",
        ObjectChangeLogView.as_view(),
        name="configtemplatemodel_changelog",
        kwargs={"model": models.ConfigTemplateModel},
    ),
    path("docs/", RedirectView.as_view(url=static("config_template/docs/index.html")), name="docs"),
]
