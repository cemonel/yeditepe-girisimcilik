from django.urls import path
from main_site import views


urlpatterns = [
    path('', views.index, name='index'),
	path('ekip/', views.team, name='team'),
	path('biz_kimiz/', views.info, name='info'),
	path('etkinlikler/', views.event, name='event'),
	path('partnerlikler/', views.supporter, name='supporter')

]