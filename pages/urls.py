from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # path('', views.BaseView.as_view(), name='baseView'),
    path('', views.HomePageView.as_view(), name='homePage'),
    # path('', views.LandingPageView, name='landingPage')
]
