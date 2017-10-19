"""metroserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

import sms.views
import run.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sms/$', sms.views.reply_to_sms_messages),
    url(r'^manifest/(?P<run_id>[0-9]+)/$', run.views.manifest_view),
    url(r'^export/(?P<run_id>[0-9]+)/$', run.views.job_export_view),
    url(r'^invoice/(?P<run_id>[0-9]+)/$', run.views.invoice_export_view),
]
