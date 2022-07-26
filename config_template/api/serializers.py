"""Config Template API serializer definitions."""
# from rest_framework import serializers

from nautobot.core.api import ValidatedModelSerializer

from config_template import models


class ConfigTemplateModelSerializer(ValidatedModelSerializer):
    """Config Template CRUD operations."""

    # url = serializers.HyperlinkedIdentityField(view_name="plugins-api:config-template-api:configtemplatemodel-detail")

    class Meta:
        """Meta definitions."""

        model = models.ConfigTemplateModel
        fields = "__all__"
