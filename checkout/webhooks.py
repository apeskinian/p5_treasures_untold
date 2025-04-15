import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listens for webhooks from Stripe and assigns a relevant handler from
    webhook_handler.py

    **Arguments:**
    - `request`: The HTTP request object.

    **Returns:**
    - `HttpResponse`:
        - On success: A response from the appropriate event handler, usually
        indicating successful processing of the event.
        - On failure: A response indicating an error (e.g., 400 for invalid
        payload or signature).
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(content=e, status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up webhook handler.
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler functions.
    event_map = {
        'payment_intent.succeeded':
            handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed':
            handler.handle_payment_intent_payment_failed,
    }

    # Get the webhook type.
    event_type = event['type']

    # If there's a handler for that type of event use it, if not use the
    # generic one.
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the event.
    response = event_handler(event)
    return response
