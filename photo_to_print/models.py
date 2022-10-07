from django.db import models
from wagtail import images

# Create your models here.
ImageModel = images.get_image_model()


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


class Coupon(models.Model):
    discount_code = models.TextField()
    # user_reference = models.TextField
    payment_applied_to = models.ForeignKey(Payment, on_delete=models.CASCADE)


class Order(models.Model):

    person = models.TextField()  #FIXME: make into a user-like model maybe (?)
    # photo = ImageModel()
    photo = models.ForeignKey(
        'wagtailimages.Image',  # named https://docs.wagtail.org/en/latest/releases/2.0.html#wagtail-module-path-updates
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    payment = models.ForeignKey(to=Payment, null=True, on_delete=models.SET_NULL)

