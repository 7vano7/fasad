from django.contrib import admin
from django import forms
from .models import Menu, MenuLang
from country.models import Country

class MenuAdminCreateForm(forms.ModelForm):
    model = Menu
    status = forms.ChoiceField(choices=Menu.LIST_STATUSES)
    class MenuLang(forms.ModelForm):
        model = MenuLang
        name = forms.TextField()
        lang = forms.ChoiceField(choices=Language.get_list(true)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('status', 'url',)
    form = MenuAdminCreateForm

