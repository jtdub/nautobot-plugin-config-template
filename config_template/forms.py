"""Config Template forms."""

from django import forms
from nautobot.utilities.forms import BootstrapMixin

from config_template import models


class ConfigTemplateFilterForm(BootstrapMixin, forms.Form):
    """Filtering/search form for 'ConfigTemplateModel' objects."""

    model = models.ConfigTemplateModel
    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(max_length=512, required=False)


class ConfigTemplateForm(BootstrapMixin, forms.ModelForm):
    """Create/update form for 'ConfigTemplateModel' objects."""

    class Meta:
        """Meta definitions."""

        model = models.ConfigTemplateModel
        fields = ["name", "context", "template"]
