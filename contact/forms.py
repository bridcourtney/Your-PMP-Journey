from django import forms


class ContactUsForm(forms.Form):
    """
    A form for contact page
    """

    full_name = forms.CharField(
        required=True,
        label='Full Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Full Name'
        })
    )
    message = forms.CharField(
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Query Details'
        })
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your Email'
        })
    )

    class Meta:
        fields = ['full_name', 'email', 'message']
