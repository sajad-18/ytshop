from django import forms
from .models import Ads


class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ('level', 'cp_count', 'sync', 'region', 'battle_pass', 'description',
                  'image_lobby', 'image_character', 'image_guns', 'image_danes', 'image_optional', 'price')

    level = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'لول'}))
    cp_count = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'مقدار cp'}))
    battle_pass = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'بتل پس های اکانت'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'توضیحات'}))
    price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'قیمت پیشنهادی', 'class': 'price'}))
    image_optional = forms.ImageField(required=False)
