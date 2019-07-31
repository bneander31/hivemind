from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import  (
    render,
    get_object_or_404,
    redirect,
)
from .models import (
    Client,
    BusinessHours,
    SocialMedia,
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
)


# class ClientView(LoginRequiredMixin, View):
#     def get(self, request, *args, **kwargs):
#         client = get_object_or_404(Client, BusinessHours, SocialMedia)
#         return render(request, c)