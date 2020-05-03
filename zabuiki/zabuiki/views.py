from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from zabuiki.pages.models import Page, Category
from zabuiki.events.models import Event
from zabuiki.site_conf.models import (Lecturers, MobileHomeBlocks, SiteConfig,
                                      Social, HomeMobileSlider)


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