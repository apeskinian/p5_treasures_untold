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
            last_modified_str = session_data.get('modified')

            if not last_modified_str:
                print(
                    f'Skipping session {session.session_key}: '
                    'No modified time found.'
                )
                continue

            try:
                last_modified = datetime.strptime(
                    last_modified_str, '%d/%m/%Y, %H:%M:%S'
                )
            except ValueError as e:
                print(
                    f'Skipping session {session.session_key}: '
                    f'Invalid modified format - {e}'
                )
                continue

            if last_modified < expiry_time:
                if 'basket' in session_data:
                    basket = session_data['basket']

                    for item_id, quantity in basket.items():
                        try:
                            product = get_object_or_404(Product, pk=item_id)
                            updated_stock = product.stock
                            updated_stock += quantity
                            if updated_stock < 0:
                                raise ValueError('Stock cannot be negative.')
                            elif product.unique_stock and updated_stock > 1:
                                raise ValueError(
                                    'Stock cannot be more than 1 '
                                    'for unique items'
                                )
                            else:
                                item_counter += quantity
                                product.stock += quantity
                                product.save()
                        except ValueError as e:
                            print(
                                f"Error updating stock for {product.id}: {e}"
                            )

                    basket_counter += 1

                session.delete()

        self.stdout.write(
            self.style.SUCCESS(
                f'Recovered {item_counter} items from {basket_counter} baskets'
            )
        )
