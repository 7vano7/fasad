from django import forms
from django.contrib import admin
from .models import Language
from country.models import Country

class LanguageAdminChangeForm(forms.ModelForm):

    model = Language
    name = forms.ChoiceField(choices=Country.get_list())
    status = forms.ChoiceField(choices=Language.LIST_STATUSES)
    main = forms.ChoiceField(choices=Language.LIST_STATUSES)

class LanguageAdminForm(forms.ModelForm):

    model = Language
    name = forms.ChoiceField(choices=Country.get_list())
    status = forms.ChoiceField(choices=Language.LIST_STATUSES)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):

    list_display = ('name', 'iso_code', 'status', 'main')
    form = LanguageAdminForm

    def get_form(self, request, obj=None, **kwargs):
        if obj:
             kwargs['form'] = LanguageAdminChangeForm
             kwargs['exclude'] = ('iso_code',)

        else:
             kwargs['form'] = LanguageAdminForm
             kwargs['exclude'] = ('iso_code', 'main',)
        return super(LanguageAdmin, self).get_form(request, obj=None, **kwargs)



