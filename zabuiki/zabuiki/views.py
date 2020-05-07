from django.http import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from zabuiki.events.models import Event
from zabuiki.pages.models import Category, Page
from zabuiki.site_conf.models import (HomeMobileSlider, Lecturers,
                                      MobileHomeBlocks, SiteConfig, Social)
from django.views.generic.list import ListView


def get_main_context(request):
    config = SiteConfig.objects.filter(enabled=True).first()
    socials = Social.objects.all()
    mobile_blocks = MobileHomeBlocks.objects.filter(is_view=True)
    categories = Category.objects.filter(is_view=True)

    context = {
        "site_config": config,
        "socials": socials,
        "categories": categories,
    }

    return context


def e_handler404(request, exception):
    context = get_main_context(request)
    response = render(request, '404.html', context=context)
    response.status_code = 404

    return response


def index(request):
    context = get_main_context(request)

    mobile_blocks = MobileHomeBlocks.objects.filter(is_view=True)
    mobile_slider = HomeMobileSlider.objects.all()

    context.update({
        'mobile_blocks': mobile_blocks,
        'mobile_slider': mobile_slider,
    })

    return render(request, "index.html", context=context)


def about(request):
    context = get_main_context(request)
    lecturers = Lecturers.objects.all()
    context.update({
        'lecturers': lecturers,
    })

    return render(request, "about.html", context=context)


def events(request):
    context = get_main_context(request)
    events = Event.objects.filter(is_view=True)
    context.update({
        'events': events,
    })

    return render(request, "events.html", context=context)


class EventsView(ListView):
    model = Event
    paginate_by = 12
    context_object_name = 'events'
    queryset = Event.objects.filter(is_view=True)
    template_name = 'events.html'
    ordering = ['event_time']

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        context.update(get_main_context(self.request))
        return context


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
