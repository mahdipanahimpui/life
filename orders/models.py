from django.db import models
from accounts.models import User
from products.models import InvoiceProduct, FlyerProduct, PrescriptionProduct
from cart.models import ShoppingCart

# ----------------------------------------------------------
class BindingType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.type}'


# ------------------------------------------------------------
class BindingDirection(models.Model):
    direction = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.direction}'


# -----------------------------------------------------------------
class Color(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32, default='#c42b59')
    def __str__(self):
        return f'{self.name} - code:{self.code}'




# -----------------------------------------------------------------
class AdditionalService(models.Model):
    type = models.CharField(max_length=64)
    service = models.CharField(max_length=64)
    # circulation_base = models.BooleanField(default=True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.service} - [{self.price}$]'


class DesignOption(models.Model):
    type = models.CharField(max_length=64)
    price = models.IntegerField()

    def __str__(self):
        return f'design_price: [{self.price}$]'
    


#  -------------------------------------------------------------------------------
def invoice_file_path(instance, filename):
    """
    مسیر فایل: media/invoice_orders/{order_id}/{filename}
    """
    order_id = instance.pk
    return f'media/invoice_orders/id-{order_id}/{filename}'


#  -------------------------------------------------------------------------------
def flyer_file_path(instance, filename):
    """
    مسیر فایل: media/flyer_orders/{order_id}/{filename}
    """
    order_id = instance.pk
    return f'media/flyer_orders/id-{order_id}/{filename}'


#  -------------------------------------------------------------------------------
def prescription_file_path(instance, filename):
    """
    مسیر فایل: media/prescription_orders/{flyer_id}/{filename}
    """
    order_id = instance.pk
    return f'media/prescription_orders/id-{order_id}/{filename}'

# -----------------------------------------------------------------------------
class InvoiceProductOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='invoice_product_orders')
    invoice_product = models.ForeignKey(InvoiceProduct, on_delete=models.SET_NULL, null=True)
    binding_type = models.ForeignKey(BindingType, on_delete=models.SET_NULL, null=True)
    binding_direction = models.ForeignKey(BindingDirection, on_delete=models.SET_NULL, null=True)
    start_from = models.IntegerField(null=True, blank=True)
    with_number = models.BooleanField(default=True)
    numbering_location = models.CharField(max_length=128, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    additional_services = models.ManyToManyField(AdditionalService, blank=True)
    design_requirement = models.BooleanField(default=False)
    description = models.CharField(max_length=1024, null=True, blank=True)
    # is_paid = models.BooleanField(default=False)
    shopping_cart = models.ForeignKey(
        ShoppingCart, 
        on_delete=models.CASCADE, 
        related_name='invoice_orders',
        null=True,  # موقتاً null=True تا بتوانید داده‌های موجود را مدیریت کنید
        blank=True
    )

    file = models.FileField(
        upload_to = invoice_file_path,  # استفاده از تابع custom
        null=True,
        blank=True
    )

    status = models.CharField(max_length=64, default='در حال چاپ')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        # قیمت پایه محصول
        base_price = self.invoice_product.base_price if self.invoice_product else 0
        
        # هزینه طراحی در صورت انتخاب
        design_price = 0
        if self.design_requirement:
            # فرض می‌کنیم DesignOption یک مدل با قیمت ثابت است
            design_option = DesignOption.objects.get(type='invoice')   
            if design_option:
                design_price = design_option.price
        
        # هزینه خدمات اضافی
        additional_services_price = sum(
            service.price for service in self.additional_services.all()
        )
        
        return base_price + design_price + additional_services_price


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'id:{self.id} - [product_id:{self.invoice_product.id if self.invoice_product else None}] - [{self.total_price}$]'
    
    def save(self, *args, **kwargs):
        # اگر این اولین بار است که ذخیره می‌شود و فایل دارد
        if self.pk is None and self.file:
            # فایل موقت را ذخیره کن
            temp_file = self.file
            self.file = None
            super().save(*args, **kwargs)  # حالا ID دارد
            
            # حالا فایل اصلی را با مسیر درست ذخیره کن
            self.file = temp_file
            # force_update=True برای جلوگیری از ایجاد رکورد جدید
            super().save(force_update=True)
        else:
            super().save(*args, **kwargs)



# -----------------------------------------------------------------------------
class FlyerProductOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='flyer_product_orders')
    flyer_product = models.ForeignKey(FlyerProduct, on_delete=models.SET_NULL, null=True)
    additional_services = models.ManyToManyField(AdditionalService, blank=True)
    design_requirement = models.BooleanField(default=False)
    description = models.CharField(max_length=1024, null=True, blank=True)
    # is_paid = models.BooleanField(default=False)
    shopping_cart = models.ForeignKey(
        ShoppingCart, 
        on_delete=models.CASCADE, 
        related_name='flyer_orders',
        null=True,  # موقتاً null=True تا بتوانید داده‌های موجود را مدیریت کنید
        blank=True
    )

    file_front = models.FileField(
        upload_to = flyer_file_path,  # استفاده از تابع custom
        null=True,
        blank=True
    )

    file_back = models.FileField(
        upload_to = flyer_file_path,  # استفاده از تابع custom
        null=True,
        blank=True
    )

    status = models.CharField(max_length=64, default='در حال چاپ')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        # قیمت پایه محصول
        base_price = self.flyer_product.base_price if self.flyer_product else 0


        if self.flyer_product:
            if self.flyer_product.side.num == 1: 
                design_option = DesignOption.objects.get(type='flyer_one_side')
            elif self.flyer_product.side.num == 2:
                design_option = DesignOption.objects.get(type='flyer_two_side')

        else:
            design_option = DesignOption.objects.get(type='flyer_two_side')


        design_price = 0
        # هزینه طراحی در صورت انتخاب
        if self.design_requirement:
            # فرض می‌کنیم DesignOption یک مدل با قیمت ثابت است
            if design_option:
                design_price = design_option.price
        
        # هزینه خدمات اضافی
        additional_services_price = sum(
            service.price for service in self.additional_services.all()
        )
        
        return base_price + design_price + additional_services_price


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'id:{self.id} - [product_id:{self.flyer_product.id if self.flyer_product else None}] - [{self.total_price}$]'

    def save(self, *args, **kwargs):

        flag = False

        if self.pk is None and self.file_front:

            temp_file_front = self.file_front
            self.file_front = None
            super().save(*args, **kwargs)  
            self.file_front = temp_file_front
            flag = True
            
        if self.pk is None and self.file_back:
            temp_file_back = self.file_back
            self.file_back = None
            super().save(*args, **kwargs)  
            self.file_back = temp_file_back
            flag = True

        if flag == True:
            super().save(force_update=True)
        else:
            super().save(*args, **kwargs)



# -----------------------------------------------------------------------------
class PrescriptionProductOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='prescription_product_orders')
    prescription_product = models.ForeignKey(PrescriptionProduct, on_delete=models.SET_NULL, null=True)
    glue_attach = models.BooleanField(default=True)
    binding_direction = models.ForeignKey(BindingDirection, on_delete=models.SET_NULL, null=True)
    additional_services = models.ManyToManyField(AdditionalService, blank=True)
    design_requirement = models.BooleanField(default=False)
    description = models.CharField(max_length=1024, null=True, blank=True)
    # is_paid = models.BooleanField(default=False)
    shopping_cart = models.ForeignKey(
        ShoppingCart, 
        on_delete=models.CASCADE, 
        related_name='prescription_orders',
        null=True,  # موقتاً null=True تا بتوانید داده‌های موجود را مدیریت کنید
        blank=True
    )

    file = models.FileField(
        upload_to = prescription_file_path,  # استفاده از تابع custom
        null=True,
        blank=True
    )

    status = models.CharField(max_length=64, default='در حال چاپ')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        # قیمت پایه محصول
        base_price = self.prescription_product.base_price if self.prescription_product else 0
        
        # هزینه طراحی در صورت انتخاب
        design_price = 0
        if self.design_requirement:
            design_option = DesignOption.objects.get(type='prescription')   
            if design_option:
                design_price = design_option.price
        
        # هزینه خدمات اضافی
        additional_services_price = sum(
            service.price for service in self.additional_services.all()
        )
        
        return base_price + design_price + additional_services_price


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'id:{self.id} - [product_id:{self.prescription_product.id if self.prescription_product else None}] - [{self.total_price}$]'
    

    def save(self, *args, **kwargs):
        # اگر این اولین بار است که ذخیره می‌شود و فایل دارد
        if self.pk is None and self.file:
            # فایل موقت را ذخیره کن
            temp_file = self.file
            self.file = None
            super().save(*args, **kwargs)  # حالا ID دارد
            
            # حالا فایل اصلی را با مسیر درست ذخیره کن
            self.file = temp_file
            # force_update=True برای جلوگیری از ایجاد رکورد جدید
            super().save(force_update=True)
        else:
            super().save(*args, **kwargs)