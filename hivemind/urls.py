from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
from .sitemaps import (
    StaticViewSitemap,
    BlogSitemap,
    # StaffSitemap,
    # ProgramSitemap,
)
from django.contrib.sitemaps.views import sitemap


sitemaps = {
    'static': StaticViewSitemap,
    'posts': BlogSitemap,
    # 'staff': StaffSitemap,
    # 'programs': ProgramSitemap
}


urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('leads/', include('leads.urls', namespace='leads')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('client/', include('client.urls', namespace='client')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemap.views.sitemap'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)