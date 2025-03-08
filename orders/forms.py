from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(initial=1, min_value=1, max_value=1, widget=forms.HiddenInput())
