from django import forms
from contact_module.models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class':'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows':'5',
                'id':'message'
            })
        }

        labels = {
            'full_name':'نام و نام خانوادگی',
            'email':'ایمیل',
            'title':'عنوان پیام',
            'message':'متن پیام',
        }

        error_messages = {
            'full_name':{
                'required':'لطفا نام و نام خانوادگی را وارد کنید',
                'max_lenght':'نام و نام خانوادگی نمی تواند بیشتر از 300 کارکتر باشد'
        },
            'email': {
                'required':'لطفا ایمیل خود را وارد کنید',
                'max_lenght':'ایمیل نمی تواند بیشتر از 300 کارکتر باشد'
        },
            'title': {
                'required': 'لطفا عنوان پیام را وارد کنید',
                'max_lenght':'عنوان نمی تواند بیشتر از 300 کارکتر باشد'
        },
            'message': {
                'required': 'متن پیام نمی تواند خالی باشد لطفا متن خود را بنویسید',
        }
        }

