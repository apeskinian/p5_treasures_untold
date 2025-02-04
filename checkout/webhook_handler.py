from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handles webhooks from Stripe
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic webhook event
        """
        return HttpResponse(
            content=f'TU Unhandled webhook: {event['type']}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'TU Payment intent succeeded: {event['type']}', status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'TU Payment failed: {event['type']}', status=200
        )
