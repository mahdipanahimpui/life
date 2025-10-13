from django import forms
from .models import DeliveryOption, PaymentOption



class DeliveryPaymentSelectionForm(forms.Form):
    shipping_method = forms.ChoiceField(
        choices=[],
        widget=forms.RadioSelect(attrs={'class': 'shipping-option-input'}),
    )

    payment_method = forms.ChoiceField(
        choices=[],
        widget=forms.RadioSelect(attrs={'class': 'shipping-option-input'}),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # پر کردن choices بر اساس options موجود در دیتابیس
        delivery_options = DeliveryOption.objects.all()
        self.fields['shipping_method'].choices = [
            (option.id, option) for option in delivery_options
        ]

        options = PaymentOption.objects.all()
        self.fields['payment_method'].choices = [
            (option.id, option) for option in options
        ]



class CardToCardPaymentForm(forms.Form):
    card_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'XXXX-XXXX-XXXX-XXXX',
            'maxlength': '19'
        }),
        label="شماره کارتی که با آن پرداخت انجام داده اید"
    )
    
    tracking_code = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'کد پیگیری دریافتی از بانک'
        }),
        label="کد پیگیری پرداخت"
    )
    
    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
        card_number = card_number.replace('-', '').replace(' ', '')
        
        if len(card_number) != 16:
            raise forms.ValidationError("شماره کارت باید 16 رقمی باشد")
        
        if not card_number.isdigit():
            raise forms.ValidationError("شماره کارت باید فقط شامل اعداد باشد")
        
        return card_number