from django.contrib import admin

from zabuiki.pages.forms import PageChangeForm
from zabuiki.pages.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_view', 'created',)
    ordering = ('-created',)
    form = PageChangeForm
    fieldsets = (
        ('META информация', {
            'fields': (
                'meta_title',
                'meta_description',
                'meta_image',
            )
        }),

        ('Основные данные', {
            'fields': (
                'title',
                'slug',
                'nav_name',
                'is_view',
                'created',
                'html_text',
            ),
        }),
    )

admin.site.register(Page, PageAdmin)
