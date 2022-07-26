"""Config Template API view definitions."""
from nautobot.core.api.views import ModelViewSet

from config_template.api import serializers
from config_template import filters, models


class ConfigTemplateModelViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    """Config Template API Viewset."""

    queryset = models.ConfigTemplateModel.objects.all()
    serializer_class = serializers.ConfigTemplateModelSerializer
    filter_class = filters.ConfigTemplateModelFilterSet
