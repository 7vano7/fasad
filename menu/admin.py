from django.contrib import admin
from django import forms
from .models import Menu, MenuLang
from country.models import Country
from languages.models import Language

#class MenuLangAdminForm(forms.ModelForm):
    #model = MenuLang
    #name = forms.CharField()
    #lang = forms.ChoiceField(choices=Language.get_list(True))

class MenuAdminCreateForm(forms.ModelForm):
    model = Menu
    status = forms.ChoiceField(choices=Menu.LIST_STATUSES)
    name = forms.CharField()
    lang = forms.ChoiceField(choices=Language.get_list(True))

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('status', 'url',)
    fields = ['name, lang', 'url', 'status']
    form = MenuAdminCreateForm







