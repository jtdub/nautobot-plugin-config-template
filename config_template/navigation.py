from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:config_template:configtemplatemodel_list",
        link_text="Config Templates",
        permissions=["config_template.view_configtemplatemodel"],
        buttons=(
            PluginMenuButton(
                link="plugins:config_template:configtemplatemodel_add",
                title="Add a new config template.",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["config_template.add_configtemplatemodel"],
            ),
        ),
    ),
)
