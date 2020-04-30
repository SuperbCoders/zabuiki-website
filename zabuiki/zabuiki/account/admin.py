from django.contrib import admin
from zabuiki.account.models import User

from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):

    list_display = ('__str__', 'email', 'phone', 'status', 'date_joined')
    ordering = ('is_staff', 'pk',)
    search_fields = ('email', 'phone',)
    list_per_page = 150

    profile_fieldsets = (
        ('Права', {
            'fields': (
                'is_staff',
                'is_superuser',
                'is_active',
                'groups',

            )
        }),
        ('Персональная информация', {
            'fields': (
                'name',
                'email',
                'phone',
                'social',
                'telegram',
                'birthday',
            ),
        }),
        ('Административная информация', {
            'fields': (
                'status',
                'payment_status',
                'comment'
            ),
        }),
    )

    fieldsets = (
        (None, {
            'fields': ('password',)
        }),
        *profile_fieldsets
    )

    add_fieldsets = (
        (None, {
            'fields': (
                'email',
                'phone',
                'is_staff',
                'is_superuser',
                'is_active',
                'social',
                'telegram',
                'birthday',

                'password1',
                'password2',

            )
        }),
    )


admin.site.register(User, AccountAdmin)
