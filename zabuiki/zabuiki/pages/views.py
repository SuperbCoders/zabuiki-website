from django.http import (Http404, HttpResponse, HttpResponseNotFound,
                         HttpResponsePermanentRedirect, HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from zabuiki.pages.models import Category, Page, PageMobileSlider
from zabuiki.views import get_main_context


def page(request, slug):
    context = get_main_context(request)
    category = get_object_or_404(Category, slug=slug)
    page = Page.objects.filter(category=category).filter(is_view=True).first()

    if not page:
        raise Http404('')

    mobile_slider = PageMobileSlider.objects.all()
    current_cat = slug

    context.update({
        'page': page,
        'current_cat': current_cat,
        'mobile_slider': mobile_slider,
    })

    return render(request, "page.html", context=context)
