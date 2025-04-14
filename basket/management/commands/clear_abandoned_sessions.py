from datetime import datetime, timedelta

from django.contrib.sessions.models import Session
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

from products.models import Product


class Command(BaseCommand):
    """
    Command to detect abandoned sessions by comparing the last interaction
    time and seeing if it's more than the specified limit.
    If so, any basket items are retrieved and rewards deactivated.
    The session is also then deleted logging the user out.
    """
    help = 'Retrieves stock from abandoned sessions'

    def handle(self, *args, **kwargs):
        basket_counter = 0
        item_counter = 0
        now = datetime.now()

        # Set the value that will  determine an abandoned session.
        expiry_time = now - timedelta(minutes=30)

        all_sessions = Session.objects.all()

        for session in all_sessions:
            session_data = session.get_decoded()
            last_modified_str = session_data.get('modified')

            # Error handling for missing or invalid session data.
            if not last_modified_str:
                self.stdout.write(
                    self.style.WARNING(
                        f'Skipping session {session.session_key}: '
                        'No modified time found.'
                    )
                )
                continue

            try:
                last_modified = datetime.strptime(
                    last_modified_str, '%d/%m/%Y, %H:%M:%S'
                )
            except ValueError as e:
                self.stderr.write(
                    self.style.ERROR(
                        f'Skipping session {session.session_key}: '
                        f'Invalid modified format - {e}'
                    )
                )
                continue

            # Check valid session data for expired time and perform recovery.
            if last_modified < expiry_time:
                # Recovery of any basket items.
                if 'basket' in session_data:

                    # create report list for email
                    report = []

                    basket = session_data['basket']
                    for item_id, quantity in basket.items():
                        try:
                            product = get_object_or_404(Product, pk=item_id)

                            # Add items to a report list.
                            report.append(product.name)

                            # Recover stock.
                            updated_stock = product.stock
                            updated_stock += quantity
                            if updated_stock < 0:
                                product.stock = 0
                                product.save()
                                raise ValueError('Stock cannot be negative.')
                            elif product.unique_stock and updated_stock > 1:
                                product.stock = 1
                                product.save()
                                raise ValueError(
                                    'Stock cannot be more than 1 '
                                    'for unique items'
                                )
                            else:
                                item_counter += quantity
                                product.stock += quantity
                                product.save()
                        except ValueError as e:
                            self.stderr.write(
                                self.style.ERROR(
                                    'Error updating stock for '
                                    f'{product.id}: {e}'
                                )
                            )

                    # Send an email report with the items recovered.
                    if report:
                        time_stamp = now.strftime('%Y-%m-%d %H:%M:%S')
                        subject = 'Abandoned Basket Recovered'
                        message = (
                            'Items have been recovered from a basket.\n'
                            f'Time: {time_stamp}\n'
                            f'Products recovered:\n' + '\n'.join(report)
                        )
                        recipient_list = [settings.DEFAULT_FROM_EMAIL]

                        send_mail(
                            subject,
                            message,
                            settings.DEFAULT_FROM_EMAIL,
                            recipient_list,
                        )

                    basket_counter += 1
                session.delete()

        self.stdout.write(
            self.style.SUCCESS(
                f'Recovered {item_counter} items from {basket_counter} baskets'
            )
        )
