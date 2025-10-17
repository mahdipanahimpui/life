from django import forms
from .models import Address

PROVINCE_CHOICES = [
    ('', 'انتخاب استان'),
    ('tehran', 'تهران'),
    ('alborz', 'البرز'),
    ('isfahan', 'اصفهان'),
    ('fars', 'فارس'),
    ('khorasan-razavi', 'خراسان رضوی'),
    ('azarbaijan-sharghi', 'آذربایجان شرقی'),
    ('azarbaijan-gharbi', 'آذربایجان غربی'),
    ('kermanshah', 'کرمانشاه'),
    ('khozestan', 'خوزستان'),
    ('gilan', 'گیلان'),
    ('mazandaran', 'مازندران'),
    ('golestan', 'گلستان'),
    ('kordestan', 'کردستان'),
    ('hamadan', 'همدان'),
    ('markazi', 'مرکزی'),
    ('lorestan', 'لرستان'),
    ('qom', 'قم'),
    ('yazd', 'یزد'),
    ('kerman', 'کرمان'),
    ('hormozgan', 'هرمزگان'),
    ('sistan', 'سیستان و بلوچستان'),
    ('bushehr', 'بوشهر'),
    ('zanjan', 'زنجان'),
    ('ardabil', 'اردبیل'),
    ('qazvin', 'قزوین'),
    ('chaharmahal', 'چهارمحال و بختیاری'),
    ('semnan', 'سمنان'),
    ('kohgiluyeh', 'کهگیلویه و بویراحمد'),
    ('ilam', 'ایلام'),
    ('north-khorasan', 'خراسان شمالی'),
    ('south-khorasan', 'خراسان جنوبی'),
]

class AddressForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'نام و نام‌خانوادگی خود را وارد کنید',
            'required': 'required'
        })
    )

        
    province = forms.ChoiceField(
        choices=PROVINCE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'province',
            'required': 'required'
        })
    )
    
    city = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'city',
            'placeholder': 'نام شهر را وارد کنید',
            'required': 'required'
        })
    )
    
    post_code = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'postalCode',
            'placeholder': '1234567890',
            'pattern': '[0-9]{10}',
            'maxlength': '10',
        })
    )
    
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phone_number',
            'placeholder': '0912...',
            'pattern': '[0-9]{11}',
            'maxlength': '11',
            'required': 'required'
        })
    )


    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'type': 'email',
            'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
            'placeholder': 'example@gmail.com',
        })
        
    )
    
    complete_address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'address',
            'placeholder': 'آدرس کامل پستی شامل خیابان، کوچه، پلاک، واحد و ...',
            'rows': 3,
            'required': 'required'
        })
    )
    
    lat = forms.DecimalField(
        required=False,
        widget=forms.HiddenInput(attrs={
            'id': 'lat'
        })
    )
    
    lng = forms.DecimalField(
        required=False,
        widget=forms.HiddenInput(attrs={
            'id': 'lng'
        })
    )

    class Meta:
        model = Address
        fields = ['name', 'email', 'province', 'city', 'post_code', 'phone_number', 
                 'complete_address', 'lat', 'lng']
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # تنظیمات اولیه برای فیلدها
        self.fields['province'].required = True
        self.fields['city'].required = True
        self.fields['name'].required = True
        self.fields['phone_number'].required = True
        self.fields['complete_address'].required = True

        self.fields['post_code'].required = False
        self.fields['email'].required = False



