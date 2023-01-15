from django.contrib import admin
from .models import Population

# Register your models here.


# class PopulationAdmin(admin.ModelAdmin):
#     list_display = ('country', 'year', 'human_count')
#     # list_display_links = ('country', 'year')
#     # list_filter = ('year',)
#     # list_editable = ('year',)
#     # search_fields = ('country', 'year')

#     # list_per_page = 25

# admin.site.register(Population, PopulationAdmin)
admin.site.register(Population)



# class ListingAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'city', 'state')
#     list_display_links = ('id', 'title')
#     list_filter = ('realtor',)
#     list_editable = ('is_published',)
#     search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

#     list_per_page = 25

# admin.site.register(Listing, ListingAdmin)