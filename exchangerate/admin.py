from django.contrib import admin
from .models import Exchangerate

# Register your models here.


class ExchangerateAdmin(admin.ModelAdmin):
    list_display = ('end_of_day', 'usd', 'cny', 'jpy', 'cad', 'aud', 'sgd', 'thb', 'myr', 'eur', 'date_created')
#     # list_display_links = ('country', 'year')
#     # list_filter = ('year',)
#     # list_editable = ('year',)
#     # search_fields = ('country', 'year')

#     # list_per_page = 25

# admin.site.register(Population, PopulationAdmin)
admin.site.register(Exchangerate, ExchangerateAdmin)