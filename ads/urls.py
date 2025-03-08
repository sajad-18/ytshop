from django.urls import path
from . import views


app_name = 'ads'
urlpatterns = [
    path('', views.AdsView.as_view(), name='ads'),
    path('ad/create/', views.AdCreateView.as_view(), name='ad_create'),
    path('ad/<int:ad_id>', views.AdDetailView.as_view(), name='ad_detail'),
]
