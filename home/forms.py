from django import forms


class ProductFilterForm(forms.Form):
    REGION_CHOICES = [
        ('iran', 'ایران'),
        ('india', 'هند'),
        ('europe', 'اروپا'),
        ('america', 'آمریکا'),
    ]
    region = forms.MultipleChoiceField(choices=REGION_CHOICES, label='ریجن', required=False,
                                       widget=forms.CheckboxSelectMultiple)
    price_asc = forms.BooleanField(label='قیمت کم به زیاد', required=False)
    price_desc = forms.BooleanField(label='قیمت زیاد به کم', required=False)
    price_range = forms.CharField(label='محدوده قیمت', required=False, widget=forms.TextInput(
        attrs={'type': 'range', 'id': 'price_range', 'class': 'form-range', 'min': '0', 'max': '10000000',
               'step': '1000'}))

