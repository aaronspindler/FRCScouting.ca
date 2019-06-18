"""FRCScouting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('ContentPages.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls')),
    path('account/', include('Accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'ContentPages.views.permission_denied'
handler404 = 'ContentPages.views.page_not_found'
handler500 = 'ContentPages.views.server_error'
