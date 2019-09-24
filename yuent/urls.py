"""yuent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.urls import path

#  from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
	path('', include('main_site.urls')),
	url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
	url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
	path('blog', include('blog.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "7Yuent Admin"
admin.site.site_title = "7Yuent Admin Portal"
admin.site.index_title = "Welcome to 7Yuent Researcher Portal"