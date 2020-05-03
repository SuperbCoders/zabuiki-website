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
from django.views.static import serve

from zabuiki import views
from zabuiki.account.views import CreateUser

handler404 = 'zabuiki.views.e_handler404'

urlpatterns = [
    path('', views.index, name="index-page"),
    path('admin/', admin.site.urls),
    path('about_us/', views.about, name="about"),
    path('events/', views.events, name="events"),
    path('pages/', include('zabuiki.pages.urls')),
    path('create_user/', CreateUser.as_view(), name="events"),
    path("robots.txt", views.robots_txt),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
