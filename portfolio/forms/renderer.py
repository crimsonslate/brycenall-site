from django.forms.renderers import TemplatesSetting
from django.template.base import Template
from django.conf import settings


class PortfolioFormRenderer(TemplatesSetting):
    form_template_name = "portfolio/forms/form.html"
    field_template_name = "portfolio/forms/field.html"

    def get_template(self, template_name: str) -> Template | None:
        if settings.DEBUG:
            print(f"Getting template '{template_name}'...")

        match template_name:
            case "django/forms/label.html":
                return self.get_template("portfolio/forms/label.html")
            case "django/forms/legend.html":
                return self.get_template("portfolio/forms/legend.html")
            case _:
                return super().get_template(template_name)
