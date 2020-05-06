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
@admin_thumbnails.thumbnail('image_1_pc_r')
@admin_thumbnails.thumbnail('image_2_pc_r')
@admin_thumbnails.thumbnail('image_3_pc_r')
@admin_thumbnails.thumbnail('about_page_direcor_image')
@admin_thumbnails.thumbnail('about_page_direcor_image_r')
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

        ('META информация страницы О нас', {
            'fields': (
                'meta_title_about',
                'meta_description_about',
            )
        }),

        ('META информация страницы Расписание', {
            'fields': (
                'meta_title_events',
                'meta_description_events',
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
                'image_1_pc_r',
                'image_1_pc_r_thumbnail',
                'image_2_pc_r',
                'image_2_pc_r_thumbnail',
                'image_3_pc_r',
                'image_3_pc_r_thumbnail',
            ),
        }),

        ('Контент на странице о нас', {
            'fields': (
                'about_page_direcor',
                'about_page_direcor_image',
                'about_page_direcor_image_thumbnail',
                'about_page_direcor_image_r',
                'about_page_direcor_image_r_thumbnail',
                'about_page_main_text',
                'about_page_top_first_text',
                'about_page_top_second_text',
                'about_page_bottom_html',
            ),
        }),
    )


@admin_thumbnails.thumbnail('image')
@admin_thumbnails.thumbnail('image_r')
class MobileHomeBlocksAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_view', 'created')
    ordering = ('-created',)
    fieldsets = (
        ('Блок', {
            'fields': (
                'image',
                'image_thumbnail',
                'image_r',
                'image_r_thumbnail',
                'text',
                'created',
            )
        }),
    )


@admin_thumbnails.thumbnail('image')
@admin_thumbnails.thumbnail('image_r')
class HomeMobileSliderAdmin(admin.ModelAdmin):
     fieldsets = (
        ('Cлайд', {
            'fields': (
                'image',
                'image_thumbnail',
                'image_r',
                'image_r_thumbnail',
            )
        }),
    )


@admin_thumbnails.thumbnail('image')
@admin_thumbnails.thumbnail('image_r')
class LecturersAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Информация о участнике', {
            'fields': (
                'name',
                'position',
                'text',
                'image',
                'image_thumbnail',
                'image_r',
                'image_r_thumbnail',
            )
        }),
    )

admin.site.register(SiteConfig, SiteConfigAdmin)
admin.site.register(MobileHomeBlocks, MobileHomeBlocksAdmin)
admin.site.register(Social)
admin.site.register(HomeMobileSlider, HomeMobileSliderAdmin)
admin.site.register(Lecturers, LecturersAdmin)