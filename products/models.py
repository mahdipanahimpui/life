from django.db import models
from accounts.models import User
from slugify import slugify
from django.urls import reverse

# -------------------------------------------------------
class PaperType(models.Model):
    type = models.CharField(max_length=64)
    # level = models.DecimalField(default=1)

    def __str__(self):
        return f'{self.type}'


# -------------------------------------------------------
class PaperSize(models.Model):
    size = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.size}'


# -------------------------------------------------------
class CirculationPrint(models.Model):
    circulation = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.circulation}'

# --------------------------------------------------------
class ColorMode(models.Model):
    mode = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.mode}'
    
# ------------------------------------------------------
class BasePrintProduct(models.Model):
    paper_type = models.ForeignKey(PaperType, on_delete=models.SET_NULL, null=True)
    paper_size = models.ForeignKey(PaperSize, on_delete=models.SET_NULL, null=True)
    circulation = models.ForeignKey(CirculationPrint, on_delete=models.SET_NULL, null=True)
    color_mode = models.ForeignKey(ColorMode, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
            abstract = True


# --------------------------------------------------------
class InvoiceType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.type}'
    

# --------------------------------------------------------
class SideType(models.Model):
    type = models.CharField(max_length=64)
    num = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.type}'

# --------------------------------------------------------
class InvoiceProduct(BasePrintProduct):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    invoice_type = models.ForeignKey(InvoiceType, on_delete=models.SET_NULL, null=True)
    base_price = models.IntegerField()
    slug = models.CharField(max_length=128, unique=True, blank=True, validators=[])

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            self.slug = f"{self.id}-{slugify(self.title, allow_unicode=True)}"
            super().save(update_fields=['slug'])
            super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('orders:invoice_order_create', kwargs={'slug': self.slug})

    def __str__(self):
        return f'id:{self.id} - {self.paper_type} - {self.paper_size} - {self.color_mode} - {self.circulation} - {self.invoice_type} - [{self.base_price}$]'





class FlyerProduct(BasePrintProduct):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    side = models.ForeignKey(SideType, on_delete=models.SET_NULL, null=True)
    base_price = models.IntegerField()
    slug = models.CharField(max_length=128, unique=True, blank=True, validators=[])

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            self.slug = f"{self.id}-{slugify(self.title, allow_unicode=True)}"
            super().save(update_fields=['slug'])
            super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('orders:flyer_order_create', kwargs={'slug': self.slug})

    def __str__(self):
        return f'id:{self.id} - {self.paper_type} - {self.paper_size} - {self.color_mode} - {self.circulation} - {self.side} - [{self.base_price}$]'
    


class PrescriptionProduct(BasePrintProduct):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    base_price = models.IntegerField()
    slug = models.CharField(max_length=128, unique=True, blank=True, validators=[])

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            self.slug = f"{self.id}-{slugify(self.title, allow_unicode=True)}"
            super().save(update_fields=['slug'])
            super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('orders:prescription_order_create', kwargs={'slug': self.slug})

    def __str__(self):
        return f'id:{self.id} - {self.paper_type} - {self.paper_size} - {self.circulation} - [{self.base_price}$]'