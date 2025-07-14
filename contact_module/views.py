from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from site_module.models import SiteSetting
from .forms import ContactUsModelForm
from .models import ContactUs, UserProfile
from django.views.generic.edit import FormView , CreateView

class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact_us/'

    def get_context_data(self,*args,**kwargs):
        context = super(ContactUsView, self).get_context_data(*args,**kwargs)
        setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context



class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact_us/'


class ProfilesView(ListView):
    template_name = 'contact_module/profile_list.html'
    model = UserProfile
    context_object_name = 'profiles'




