from nautobot.utilities.filters import BaseFilterSet, SearchFilter

from config_template import models


class ConfigTemplateModelFilterSet(BaseFilterSet):
    """API filter for filtering config template model objects."""

    q = SearchFilter(
        filter_predicates={"name": "icontains", "context": "icontains"},
    )

    class Meta:
        model = models.ConfigTemplateModel
        fields = [
            "name",
            "context",
        ]
