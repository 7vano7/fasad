from django import forms
from django.contrib import admin
from .models import Language

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    exclude = ('main','iso_code',)
    list_display = ('name', 'iso_code', 'status', 'main')

    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "status":
            kwargs['choice'] = ((STATUS_ACTIVE, STATUS_ACTIVE), (STATUS_ACTIVE, STATUS_ACTIVE)),
        return super(LanguageAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)