from .forms import SubscriberForm


def subscriber_form(request):
    """
    Context processor that provides a global newsletter sign-up form.

    This form is used in the `info_section.html` include file. To prevent
    conflicts when another instance of this form appears on the Newsletter
    page, it is prefixed with 'newsletter'.

    **Returns:**
    - A dictionary containing an instance of :form:`support.SubscriberForm`
        prefixed with 'newsletter' so that when on the Newsletter page it does
        not conflict with the other instance of the same form.
    """
    return {'subscriber_form': SubscriberForm(prefix='newsletter')}
