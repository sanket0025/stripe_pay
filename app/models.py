from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
# from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL

def get_image_filename(instance, filename):
    name = instance.name
    slug = slugify(name)
    return f"products/{slug}-{filename}"

class ProductTag(models.Model):
    name = models.CharField( max_length=100, blank=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField(ProductTag, blank=True)
    desc = models.TextField(("Description"), blank=True)
    thumbnail = models.ImageField(upload_to=get_image_filename, blank=True)
    url = models.URLField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product.name} {self.price}"