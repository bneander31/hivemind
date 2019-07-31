from django.http import HttpResponse
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)
from django.shortcuts import (
    render,
    get_object_or_404,
    # redirect,
)
from cms.models import (
    Client,
    BusinessHours,
    SocialMedia,
    Asset,
    Item,
)
from .models import (
    # Cta,
    Carousel,
    Slide,
    Form,
    Field,
    ParallaxRow,
    ColumnInfo,
)
from django.core.paginator import (
    EmptyPage,
    PageNotAnInteger,
    Paginator,
)
from django.contrib import messages
from django.views.generic import (
    View,
    TemplateView,
    # CreateView,
    # UpdateView,
    # DeleteView,
)


# class BaseView(LoginRequiredMixin,View):
#     def get(self, request, *args, **kwargs):
#         client = get_object_or_404(
#             Client,
#             # BusinessHours,
#             # SocialMedia
#         )
#         return render(
#             request,
#             'home.html',
#             {'client': client}
#         )


class HomePageView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        client = get_object_or_404(Client)
        hour = BusinessHours.objects.all
        social = SocialMedia.objects.all
        slide = Slide.objects.all
        form = Form.objects.get(pk=1)
        field = Field.objects.all
        parallaxrow = ParallaxRow.objects.get(pk=1)
        column = ColumnInfo.objects.all
        service = Asset.objects.filter(Published=True).get(Type='Services')
        product = Asset.objects.filter(Published=True).get(Type='Products')
        item = Item.objects.filter(Published=True)

        context = {
            'client': client,
            'hour': hour,
            'social': social,
            'slide': slide,
            'form': form,
            'field': field,
            'parallaxrow': parallaxrow,
            'column': column,
            'service': service,
            'product': product,
            'item': item,
            # 'cta': cta,
        }

        return render(
            request,
            'home.html',
            context,
            *args,
            **kwargs,
        )

# class LandingPageView(LoginRequiredMixin, TemplateView):
#     def get(self, request, *args, **kwargs):
#         client = get_object_or_404(
#             Client,
#             BusinessHours,
#             SocialMedia,
#         )
#         return render(
#             request,
#             'landing_page.html',
#             {'client':  client}
#         )
