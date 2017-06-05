from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)  # unique=True
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2,
            default=0.0, null=True, blank=True)

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    print(sender)
    print(instance)
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(product_pre_save_receiver, sender=Product)


# def product_post_save_receiver(sender, instance, *args, **kwargs):
#     if instance.slug != slugify(instance.title):
#         instance.slug = slugify(instance.title)
#         instance.save()
