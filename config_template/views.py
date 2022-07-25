from nautobot.core.views import generic

from config_template import models, forms, filters, tables


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
