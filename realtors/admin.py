from django.contrib import admin
from .models import Realtor
# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    list_display_links = ('phone',)


admin.site.register(Realtor, RealtorAdmin)
