
from django import forms
from .models import (
    InvoiceProductOrder, 
    FlyerProductOrder,
    PrescriptionProductOrder
)

class InvoiceProductOrderForm(forms.ModelForm):
    
    class Meta:
        model = InvoiceProductOrder
        fields = [
            'binding_type', 'binding_direction',
            'start_from', 'with_number', 'numbering_location', 'color', 'additional_services',
            'design_requirement', 'description', 'file'
        ]
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'توضیحات کامل در خصوص سفارشتان...',
                'class': 'form-control',
                'id': 'description-field'
            }),
            'start_from': forms.NumberInput(attrs={
                'min': 1,
                'placeholder': 'شروع شماره از', 
                'class': 'form-control',
                'id': 'startNumber'
            }),
            'numbering_location': forms.TextInput(attrs={
                'placeholder': 'مثال: بالای صفحه زیر تاریخ',
                'class': 'form-control',
                'id': 'numberingLocation'
            }),
            'design_requirement': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'design-requirement-checkbox'
            }),
            'with_number': forms.CheckboxInput(attrs={
                'class': 'no-number-btn',
                'id': 'noNumber',
            }),
            'additional_services': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
                'id': 'additional-services-checkboxes'
            }),
            'binding_type': forms.Select(attrs={
                'class': 'form-control',
                'id': 'bindingType'
            }),
            'binding_direction': forms.Select(attrs={
                'class': 'form-control',
                'id': 'bindingDirection'
            }),
            'colors': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
                'id': 'additional-services-checkboxes'
            }),
            'file': forms.FileInput(attrs={
                'id': 'fileInput',
                'style': 'display: none;'
            })
        }
        labels = {
            'start_from': 'شروع شماره از',
            'numbering_location': 'محل شماره گذاری',
            'design_requirement': 'نیاز به انجام طراحی',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # تنظیمات اولیه برای فیلدها
        self.fields['color'].required = False
        self.fields['additional_services'].required = False
        self.fields['file'].required = False




        self.fields['with_number'].initial = False

        self.fields['binding_type'].empty_label = "انتخاب کنید"
        self.fields['binding_direction'].empty_label = "انتخاب کنید"

        
        # حذف فیلد invoice_product از فرم چون از طریق slug دریافت می‌شود
        if 'invoice_product' in self.fields:
            del self.fields['invoice_product']
        
        # تنظیم برچسب‌های فارسی برای فیلدهایی که در Meta.labels تعریف نشده‌اند
        self.fields['binding_type'].label = 'نوع صحافی'
        self.fields['binding_direction'].label = 'جهت صحافی'
        self.fields['color'].label = 'رنگ'
        self.fields['additional_services'].label = 'خدمات تکمیلی'
        self.fields['description'].label = 'توضیحات تکمیلی'
        self.fields['file'].label = 'آپلود فایل'

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.with_number =  not self.cleaned_data['with_number']

        if not instance.with_number:
            instance.start_from = None
            instance.numbering_location = None
        
        if commit:
            instance.save()
    
        return instance


# ----------------------------------------------------------------------
class FlyerProductOrderForm(forms.ModelForm):
    
    class Meta:
        model = FlyerProductOrder
        fields = [
            'additional_services',
            'design_requirement', 'description', 'file_front', 'file_back'
        ]
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'توضیحات کامل در خصوص سفارشتان...',
                'class': 'form-control',
                'id': 'description-field'
            }),
            'design_requirement': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'design-requirement-checkbox'
            }),
            'additional_services': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
                'id': 'additional-services-checkboxes'
            }),

            'file_front': forms.FileInput(attrs={
                'id': 'frontFileInput',
                'style': 'display: none;'
            }),
            'file_back': forms.FileInput(attrs={
                'id': 'backFileInput',
                'style': 'display: none;'
            })
        }
        labels = {
            'design_requirement': 'نیاز به انجام طراحی',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # تنظیمات اولیه برای فیلدها
        self.fields['additional_services'].required = False
        self.fields['file_front'].required = False
        self.fields['file_back'].required = False


        
        # حذف فیلد invoice_product از فرم چون از طریق slug دریافت می‌شود
        if 'flyer_product' in self.fields:
            del self.fields['flyer_product']
        
        # تنظیم برچسب‌های فارسی برای فیلدهایی که در Meta.labels تعریف نشده‌اند
        self.fields['additional_services'].label = 'خدمات تکمیلی'
        self.fields['description'].label = 'توضیحات تکمیلی'
        self.fields['file_front'].label = 'آپلود فایل (روی طرح)'
        self.fields['file_back'].label = 'آپلود فایل (پشت طحر)'



# ----------------------------------------------------------------------
class PrescriptionProductOrderForm(forms.ModelForm):
    
    class Meta:
        model = PrescriptionProductOrder
        fields = [
            'binding_direction','additional_services', 'glue_attach',
            'design_requirement', 'description', 'file'
        ]
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'توضیحات کامل در خصوص سفارشتان...',
                'class': 'form-control',
                'id': 'description-field'
            }),

            'design_requirement': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'design-requirement-checkbox'
            }),

            'glue_attach': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'glueAttachCheckbox'
            }),

            'additional_services': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
                'id': 'additional-services-checkboxes'
            }),

            'binding_direction': forms.Select(attrs={
                'class': 'form-control',
                'id': 'bindingDirection'
            }),

            'file': forms.FileInput(attrs={
                'id': 'fileInput',
                'style': 'display: none;'
            })
        }
        labels = {
            'glue-attach': 'نیاز به سرچسب',
            'design_requirement': 'نیاز به انجام طراحی',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # تنظیمات اولیه برای فیلدها
        self.fields['additional_services'].required = False
        self.fields['file'].required = False
        self.fields['glue_attach'].initial = False
        self.fields['binding_direction'].required = False
        self.fields['binding_direction'].empty_label = "انتخاب کنید"

        
        # حذف فیلد invoice_product از فرم چون از طریق slug دریافت می‌شود
        if 'prescriptions_product' in self.fields:
            del self.fields['prescription_product']
        
        # تنظیم برچسب‌های فارسی برای فیلدهایی که در Meta.labels تعریف نشده‌اند
        self.fields['binding_direction'].label = 'جهت سرچسب'
        self.fields['additional_services'].label = 'خدمات تکمیلی'
        self.fields['description'].label = 'توضیحات تکمیلی'
        self.fields['file'].label = 'آپلود فایل'

    def save(self, commit=True):
        instance = super().save(commit=False)
        is_glue_attach = instance.glue_attach =  self.cleaned_data['glue_attach']

        if not is_glue_attach:
            instance.binding_direction = None
        
        if commit:
            instance.save()
    
        return instance
