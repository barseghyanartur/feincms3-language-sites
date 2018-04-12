from django.contrib import admin
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('is_default', 'host'),
        }),
        (capfirst(_('advanced')), {
            'fields': ('host_re',),
            'classes': ('collapse',),
        }),
    ]
    list_display = ('host', 'is_default', 'host_re')
    ordering = ('-is_default',)
