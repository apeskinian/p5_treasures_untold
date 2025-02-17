from django.core.management.base import BaseCommand
from datetime import timedelta, datetime
from django.contrib.sessions.models import Session
from products.models import Product
from django.shortcuts import get_object_or_404


class Command(BaseCommand):
    help = "Retrieves stock from abandoned sessions"

    def handle(self, *args, **kwargs):
        basket_counter = 0
        item_counter = 0
        now = datetime.now()
        expiry_time = now - timedelta(minutes=10)

        all_sessions = Session.objects.all()

        for session in all_sessions:
            session_data = session.get_decoded()
            last_modified = datetime.strptime(
                session_data.get('modified'), '%d/%m/%Y, %H:%M:%'
            )

            print(last_modified, expiry_time)

            if last_modified and last_modified < expiry_time:

                if 'basket' in session_data:
                    basket = session_data['basket']

                    for item_id, quantity in basket.items():
                        product = get_object_or_404(Product, pk=item_id)
                        item_counter += quantity
                        product.stock += quantity
                        if product.stock < 0:
                            raise ValueError('Stock cannot be negative.')
                        product.save()

                    basket_counter += 1

                session.delete()

        self.stdout.write(
            self.style.SUCCESS(
                f'Recovered {item_counter} items from {basket_counter} baskets'
            )
        )
