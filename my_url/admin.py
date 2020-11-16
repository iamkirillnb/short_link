from django.contrib import admin
from .models import Links


class LinksAdmin(admin.ModelAdmin):
    list_display = ('link', 'shortened', 'change_flag')
    list_display_links = ('link',)


admin.site.register(Links, LinksAdmin)