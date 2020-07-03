from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('movie/<int:pk>/', views.DetailPageView.as_view(), name='detail'),
    path('hollywood/', views.HollywoodPageView.as_view(), name='hollywood'),
    path('bollywood/', views.BollywoodPageView.as_view(), name='bollywood'),
    path('tollywood/', views.TollywoodPageView.as_view(), name='tollywood'),
    path('web_series/', views.WebSeriesPageView.as_view(), name='web_series'),
    path('movierequest/', views.contact, name='movie_request'),
    path('search/', views.search, name='search'),
]
