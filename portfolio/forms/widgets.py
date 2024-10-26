from django.forms import widgets


class TextInput(widgets.TextInput):
    input_type = "text"
    template_name = "portfolio/forms/widgets/text.html"


class CheckboxInput(widgets.CheckboxInput):
    input_type = "checkbox"
    template_name = "portfolio/forms/widgets/checkbox.html"


class FileInput(widgets.FileInput):
    input_type = "file"
    template_name = "portfolio/forms/widgets/file.html"


class TextareaInput(widgets.Textarea):
    template_name = "portfolio/forms/widgets/textarea.html"
