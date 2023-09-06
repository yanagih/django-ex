from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, test, measurements, jee, setting, about, admin, labs, login, mode, info

from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', test, name='test'),
    url(r'^measurements$', measurements, name='measurements'),
    url(r'^jee$', jee, name='jee'),
    url(r'^setting$', setting, name='setting'),
    url(r'^about$', about, name='about'),
    url(r'^admin$', admin, name='admin'),
    url(r'^labs$', labs, name='labs'),
    url(r'^login$', login, name='login'),
    url(r'^mode$', mode),
    url(r'^info$', info),
    # url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
