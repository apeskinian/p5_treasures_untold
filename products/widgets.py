from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    Custom widget for handling file input with a clearable option.

    **Attributes:**
    - 'clear_checkbox_label': The label for the checkbox to clear file input.
    - 'initial_text': Text shown for the current file (if any).
    - 'input_text': Placeholder text for the file input field.
    - 'template_name': Path to the custom template used for rendering.

    **Template:**
    - :template:`products/custom_widget_templates/custom_clearable_file_input.html` # noqa: E501
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html'
    )
