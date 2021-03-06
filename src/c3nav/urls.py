from django.conf.urls import include, url
from django.contrib import admin

import c3nav.access.urls
import c3nav.api.urls
import c3nav.editor.urls
import c3nav.site.urls

urlpatterns = [
    url(r'^access/', include(c3nav.access.urls)),
    url(r'^editor/', include(c3nav.editor.urls)),
    url(r'^api/', include(c3nav.api.urls, namespace='api')),
    url(r'^admin/', admin.site.urls),
    url(r'^locales/', include('django.conf.urls.i18n')),
    url(r'^', include(c3nav.site.urls)),
]
