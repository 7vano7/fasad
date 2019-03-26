from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
#from django_admin_multiple_choice_list_filter.list_filters import MultipleChoiceListFilter
from .models import Country

#class StatusListFilter(MultipleChoiceListFilter):
#    title = 'Status'
#    parameter_name = 'status__in'

#    def lookups(self, request, model_admin):
#        return Statuses.CHOICES

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('id', 'name', 'iso_code')
    list_filter = (('name', DropdownFilter), ('iso_code', DropdownFilter))
    #list_filter = (('name', StatusListFilter), ('iso_code', DropdownFilter))
