"""Config Template models."""
from django.db import models
from django.urls import reverse
from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import OrganizationalModel
from nautobot.extras.models import GraphQLQuery
from nautobot.extras.utils import extras_features


@extras_features(
    "custom_links",
    "dynamic_groups",
    "graphql",
    "webhooks",
)
class ConfigTemplateModel(OrganizationalModel):
    """Config Template models."""

    name = models.CharField(max_length=512, help_text="The name of the template.")
    slug = AutoSlugField(populate_from="name")
    context = models.ForeignKey(
        GraphQLQuery, on_delete=models.CASCADE, help_text="Saved GraphQL query that provides context to the template."
    )
    template = models.TextField(help_text="Jinja template that describes the config.")

    class Meta:
        """Meta definitions."""

        ordering = ["name", "context"]

    def __str__(self):
        """Return string for 'ConfigTemplateModel' object."""
        return self.name

    def get_absolute_url(self):
        """Reverse URL for 'ConfigTemplateModel' objects."""
        return reverse("plugins:config_template:configtemplatemodel", kwargs={"slug": self.slug})
