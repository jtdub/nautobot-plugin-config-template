"""Config Template API URL definitions."""
from django.urls import include, path

from nautobot.core.api import OrderedDefaultRouter

from config_template.api import views


router = OrderedDefaultRouter()
router.register("", views.ConfigTemplateModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
