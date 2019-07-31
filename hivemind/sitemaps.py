from django.contrib.sitemaps import Sitemap
from django.urls import reverse
import blog.models
import gallery.models
import leads.models
import pages.models
import cms.models


class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return Post.objects.filter(published=True)

#
# class StaffSitemap(Sitemap):
#     priority = 0.5
#     changefreq = 'weekly'
#     protocol = 'https'
#
#     def items(self):
#         return Employee.objects.filter(active=True)
#
#
# class ProgramSitemap(Sitemap):
#     priority = 1.0
#     changefreq = 'weekly'
#     protocol = 'https'
#
#     def items(self):
#         return Program.objects.filter(active=True)


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return [
            'pages:index',
            'blog:blog_list',
            'gallery:gallery',
                ]

    def location(self, item):
        return reverse(item)
