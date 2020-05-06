from django.contrib import admin

from zabuiki.orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'payment', 'amount')
    list_filter = ('product', )


admin.site.register(Order, OrderAdmin)