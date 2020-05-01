from django.contrib import admin
from zabuiki.events.models import Event


class EventAdmin(admin.ModelAdmin):
    ordering = ('-event_time',)
    list_display = ('name', 'price', 'event_time', 'is_free', 'is_view')


admin.site.register(Event, EventAdmin)