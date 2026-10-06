from django.db import models
from django.utils.text import slugify
from django.db import models
from .utils import get_usd_rate


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Аталышы")
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(verbose_name="Сүрөттөмө", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баасы")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Сүрөт")
    is_active = models.BooleanField(default=True, verbose_name="Активдүү")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товарлар"
        ordering = ['-created_at']

    def str(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Phone(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баасы (сом)")
    image = models.ImageField(upload_to='phones/', blank=True, null=True)

    def str(self):
        return self.name

    @property
    def price_usd(self):
        """Сомдогу бааны долларга айландырат (реалдуу курс боюнча)"""
        rate = get_usd_rate()
        return round(float(self.price) / rate, 2)

    @property
    def price_usd_display(self):
        return f"${self.price_usd}"


# Create your models here.
