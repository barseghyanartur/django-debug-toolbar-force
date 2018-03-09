from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from nine import versions

__all__ = ('urlpatterns',)

admin.autodiscover()

urlpatterns = []
urlpatterns_args = []

# Admin URLs
if versions.DJANGO_GTE_2_0:
    urlpatterns_args += [
        url(r'^admin/', admin.site.urls),
    ]
else:
    urlpatterns_args += [
        url(r'^admin/', include(admin.site.urls)),
    ]

urlpatterns_args = [
    # foo URLs:
    url(r'^foo/', include('debug_toolbar_force.tests.foo.urls')),

    url(r'^$', TemplateView.as_view(template_name='home/base.html')),
]

urlpatterns += i18n_patterns(*urlpatterns_args)

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

if settings.DEBUG_TOOLBAR is True:
    import debug_toolbar

    if versions.DJANGO_GTE_2_0:
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    else:
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
