from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

from zabuiki.site_conf.models import MobileHomeBlocks, SiteConfig, Social
from zabuiki.pages.models import Page

def get_main_context(request):
    config = SiteConfig.objects.filter(enabled=True).first()
    socials = Social.objects.all()
    mobile_blocks = MobileHomeBlocks.objects.filter(is_view=True)
    context = {
        "site_config": config,
        "socials": socials,
        "mobile_blocks": mobile_blocks,
    }

    return context


def e_handler404(request):
    response = render(request, 'error404.html')
    response.status_code = 404
    return response


def index(request):
    context = get_main_context(request)
    pages = Page.objects.filter(is_view=True).values('title', 'nav_name', 'slug')
    context.update({
        'pages': pages,
    })
    return render(request, "index.html", context=context)
