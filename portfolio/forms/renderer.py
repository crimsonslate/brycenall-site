from django.forms.renderers import TemplatesSetting
from django.template.base import Template
from django.conf import settings


class PortfolioFormRenderer(TemplatesSetting):
    form_template_name = "portfolio/forms/form.html"
    field_template_name = "portfolio/forms/field.html"

    def get_template(self, template_name: str) -> Template | None:
        if settings.DEBUG:
            print(f"Getting template '{template_name}'...")

        return super().get_template(template_name)
