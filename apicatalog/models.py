from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from common.utils.email_utils import send_product_notification

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    sku = models.CharField(max_length=16)
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=50, default='')
    image_url = models.CharField(default='', max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def send_save_email(sender, instance, created, **kwargs):
    """
    Send email to admin notify changes.
    """
    product = instance
    if created:
        send_product_notification(
            product, 'New Product Added ID' + str(product.id))
    else:
        send_product_notification(
            product, 'Product Updated ID ' + str(product.id))

@receiver(post_delete, sender=Product)
def send_delete_email(sender, instance, **kwargs):
    """
    Send email to admin notify changes.
    """
    product = instance
    send_product_notification(product,'Product Deleted  ' + str(product.id))
