from django.contrib import admin

from zabuiki.site_conf.models import *
import admin_thumbnails


class SocialInline(admin.TabularInline):

    model = Social
    extra = 0
    fieldsets = ('Социальные сети', {
        'fields': (
            'name',
            'link',
        ),
    }),


@admin_thumbnails.thumbnail('image_1_pc')
@admin_thumbnails.thumbnail('image_2_pc')
@admin_thumbnails.thumbnail('image_3_pc')
@admin_thumbnails.thumbnail('image_1_mobile')
class SiteConfigAdmin(admin.ModelAdmin):
    inlines = [
        SocialInline,
    ]

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
                'email',
                'html_head',
                'html_footer',
                'enabled',
            ),
        }),

        ('Анонс', {
            'fields': (
                'anonce_text',
                'anonce_link',
            ),
        }),

        ('Текста на главной странице', {
            'fields': (
                'up_text',
                'down_text',
            ),
        }),

        ('Изображения на главной странице', {
            'fields': (
                'image_1_pc',
                'image_1_pc_thumbnail',
                'image_2_pc',
                'image_2_pc_thumbnail',
                'image_3_pc',
                'image_3_pc_thumbnail',
                'image_1_mobile',
                'image_1_mobile_thumbnail',
            ),
        }),
        
    )


@admin_thumbnails.thumbnail('image')
class MobileHomeBlocksAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Блок', {
            'fields': (
                'image',
                'image_thumbnail',
                'text',
                'created',
            )
        }),
    )

admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(MobileHomeBlocks, MobileHomeBlocksAdmin)
