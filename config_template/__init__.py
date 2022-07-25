"""Plugin declaration for config_template."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class ConfigTemplateConfig(PluginConfig):
    """Plugin configuration for the config_template plugin."""

    name = "config_template"
    verbose_name = "Config Template"
    version = __version__
    author = "James Williams"
    description = "Config Template."
    base_url = "config-template"
    required_settings = []
    min_version = "1.2.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = ConfigTemplateConfig  # pylint:disable=invalid-name
