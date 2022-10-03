from django.db import models

# Create your models here.


class Reservation(models.Model):
    pass


class PaymentStatus(models.TextChoices):
    NOT_PAID = 'not_paid', 'Not Paid'  # TODO: make this  _('translatable')
    PROCESSING = 'processed', 'Processing'
    PAID = 'paid', 'Paid'
    COUPON = 'coupon', 'Coupon'


class Payment(models.Model):
    status = models.CharField(
        max_length=16,
        choices=PaymentStatus.choices,
        default=PaymentStatus.NOT_PAID,
    )

    def get_payment_status(self) -> PaymentStatus:
        return PaymentStatus[self.status]

