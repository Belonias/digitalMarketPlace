from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(default='slug-field')  # unique=True
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2,
            default=0.0, null=True, blank=True)

    def __str__(self):
        return self.title
