from django.contrib import admin
from .models import Language

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code')

# Define the admin class
#class LanguageAdmin(admin.ModelAdmin):
#    pass

#admin.site.register(Language, LanguageAdmin)

# Register your models here.
