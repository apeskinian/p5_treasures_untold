import stripe
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listens for webhooks from Stripe
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

    event_type = event.type
    print(f"Processing event: {event_type}")
    print('SUCCESS!')
    return HttpResponse(status=200)
