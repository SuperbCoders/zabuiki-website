"""zabuiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.static import serve
from django.contrib import admin
from zabuiki.orders.views import order_event
from zabuiki import views
from zabuiki.account.views import CreateUser

admin.autodiscover()

handler404 = 'zabuiki.views.e_handler404'

urlpatterns = [
    path('', views.index, name="index-page"),
    path('admin/', admin.site.urls),
    path('about/', views.about, name="about"),
    #path('events/', views.events, name="events"),
    path('events/', views.EventsView.as_view(), name="events"),
    path('events/<event_id>/payment', order_event, name="events-payment"),
    path('products/', include('zabuiki.pages.urls')),
    path('create_user/', CreateUser.as_view(), name="create-user"),
    path("robots.txt/", views.robots_txt),
    path('fail-payment/', TemplateView.as_view(template_name='fail.html'), name='payment_fail'),
    path('success-payment/', TemplateView.as_view(template_name='success.html'), name='payment_success'),
    path('yandex-money/', include('yandex_money.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
