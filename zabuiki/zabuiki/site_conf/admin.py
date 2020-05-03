from django.contrib import admin

from zabuiki.site_conf.models import *
import admin_thumbnails
from zabuiki.site_conf.froms import SiteConfigChangeForm


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
@admin_thumbnails.thumbnail('about_page_direcor_image')
class SiteConfigAdmin(admin.ModelAdmin):
    form = SiteConfigChangeForm

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
            ),
        }),

        ('Контент на странице о нас', {
            'fields': (
                'about_page_direcor',
                'about_page_direcor_image',
                'about_page_direcor_image_thumbnail',
                'about_page_main_text',
                'about_page_top_first_text',
                'about_page_top_second_text',
                'about_page_bottom_left_text',
                'about_page_bottom_right_text',
            ),
        }),
    )


@admin_thumbnails.thumbnail('image')
class MobileHomeBlocksAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_view', 'created')
    ordering = ('-created',)
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


@admin_thumbnails.thumbnail('image')
class HomeMobileSliderAdmin(admin.ModelAdmin):
     fieldsets = (
        ('Cлайд', {
            'fields': (
                'image',
                'image_thumbnail',
            )
        }),
    )


@admin_thumbnails.thumbnail('image')
class LecturersAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Информация о лекторе', {
            'fields': (
                'name',
                'position',
                'text',
                'image',
                'image_thumbnail',
            )
        }),
    )

admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(MobileHomeBlocks, MobileHomeBlocksAdmin)
admin.site.register(Social)
admin.site.register(HomeMobileSlider, HomeMobileSliderAdmin)
admin.site.register(Lecturers, LecturersAdmin)