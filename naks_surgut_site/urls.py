"""naks_surgut_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('news/', mainapp.news, name='news'),
    path('contact/', mainapp.contact, name='contact'),
    # re_path(r'details/$', mainapp.details, name='post_details'),
    path('detailview/<slug:content>/<slug:pk>',
         mainapp.details, name='detailview'),
    # path('create/<slug:content_type>', mainapp.create_factory, name='create'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    # path('messages/', mainapp.messages, name='messages'),
    # path('validate_form/', mainapp.validate_form,
        #  name='validate_form'), # use for ajax form validation
    # path('documents/', mainapp.documents, name="documents"),
    path('services/', mainapp.services, name="services"),
    path('about/', mainapp.about, name="about"),
    # path('staff', mainapp.staff, name='staff')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)