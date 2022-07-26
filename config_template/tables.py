"""Config Template tables."""

import django_tables2 as tables
from nautobot.utilities.tables import BaseTable, ButtonsColumn, ToggleColumn

from config_template import models


class ConfigTemplateModelTable(BaseTable):
    """Table for list view of 'ConfigTemplateModel' objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    actions = ButtonsColumn(models.ConfigTemplateModel)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta definitions."""

        model = models.ConfigTemplateModel
        fields = ["pk", "name", "context"]
