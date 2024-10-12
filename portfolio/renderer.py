from django.forms.renderers import TemplatesSetting


class PortfolioFormRenderer(TemplatesSetting):
    form_template_name = "portfolio/forms/_form.html"
    formset_template_name = "portfolio/forms/_formset.html"
    field_template_name = "portfolio/forms/_field.html"
