"""Config Template Views."""

import pynautobot
from jinja2 import BaseLoader, Environment, StrictUndefined
from nautobot.core.views import generic

from config_template import constants, filters, forms, models, tables


class ConfigTemplateListView(generic.ObjectListView):
    """List 'ConfigTemplateModel' objects."""

    queryset = models.ConfigTemplateModel.objects.all()
    filterset = filters.ConfigTemplateModelFilterSet
    filterset_form = forms.ConfigTemplateFilterForm
    table = tables.ConfigTemplateModelTable


class ConfigTemplateEditView(generic.ObjectEditView):
    """Edit a single 'ConfigTemplateModel' object."""

    queryset = models.ConfigTemplateModel.objects.all()
    model_form = forms.ConfigTemplateForm


class ConfigTemplateDeleteView(generic.ObjectDeleteView):
    """Delete a single 'ConfigTemplateModel' object."""

    queryset = models.ConfigTemplateModel.objects.all()


class ConfigTemplateView(generic.ObjectView):
    """Detail view for a single 'ConfigTemplateModel' object."""

    queryset = models.ConfigTemplateModel.objects.all()

    def get_extra_context(self, request, instance):
        """Extra contexts to compile templates."""
        api_token = constants.CONFIG_TEMPLATE_SETTINGS.get("token")
        nb_api = pynautobot.api(url="http://localhost:8080", token=api_token)
        gql_query = nb_api.graphql.query(query=instance.context.query)
        data = gql_query.json.get("data")
        template = Environment(
            loader=BaseLoader(),
            undefined=StrictUndefined,
            trim_blocks=True,
            autoescape=True,
        ).from_string(instance.template)
        return {"compiled_template": template.render(data), "raw_template": instance.template}
