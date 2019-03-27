from django import forms
from django.contrib import admin
from .models import Language
from country.models import Country

class LanguageAdminForm(forms.ModelForm):
    model = Language
    name = forms.ChoiceField(choices=Country.get_list())
    status = forms.ChoiceField(choices=Language.LIST_STATUSES)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    form = LanguageAdminForm
    exclude = ('main','iso_code',)
    list_display = ('name', 'iso_code', 'status', 'main')

