import admin_thumbnails
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.shortcuts import render
from django.utils.safestring import mark_safe

from zabuiki.pages.forms import PageChangeForm
from zabuiki.pages.models import Category, Page, PageMobileSlider


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, renderer, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(u' <a href="%s" target="_blank"><img width="200px" src="%s" alt="%s" /></a>' % \
                          (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ImageWidgetAdmin(admin.StackedInline):
    image_fields = []

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.image_fields:
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_view', 'created',)


class MobileSliderInline(ImageWidgetAdmin):
    model = PageMobileSlider
    extra = 0
    max_num = 10
    image_fields = ['image']

@admin_thumbnails.thumbnail('image')
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_view', 'created',)
    ordering = ('-created',)
    inlines = [MobileSliderInline]
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
                'category',
                'lecturer',
                'link',
                'is_view',
                'created',
                'image',
                'image_thumbnail',
                'html_text',
            ),
        }),
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
