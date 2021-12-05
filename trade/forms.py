from django import forms

class Owner_details_form(forms.Form):
    kite_api_key = forms.CharField()
    kite_secret_key = forms.CharField()

class Order(forms.Form):
    instrument = forms.CharField()
    premium = forms.CharField()
    distance = forms.CharField()
    buy_quantity = forms.CharField()
    sell_qunatity = forms.CharField()