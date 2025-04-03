from django import forms


class DepositForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2, 
        label="Amount",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'})
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        label="Password"
    )

class OfferForm(forms.Form):
    amount = forms.DecimalField(
        max_digits=10, decimal_places=2,
        label="Your Offer",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your offer'})
    )