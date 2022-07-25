from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView

from nautobot.extras.views import ObjectChangeLogView

from config_template import views, models


app_name = "config-template"

urlpatterns = [
    path("", views.ConfigTemplateListView.as_view(), name="configtemplatemodel_list"),
    path("add/", views.ConfigTemplateEditView.as_view(), name="configtemplatemodel_add"),
    path("<slug:slug>/", views.ConfigTemplateView.as_view(), name="configtemplatemodel"),
    path("<slug:slug>/edit/", views.ConfigTemplateEditView.as_view(), name="configtemplatemodel_edit"),
    path("<slug:slug>/delete/", views.ConfigTemplateDeleteView.as_view(), name="configtemplatemodel_delete"),
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
