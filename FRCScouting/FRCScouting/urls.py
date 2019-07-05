from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', include('ContentPages.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls')),
    path('account/', include('Accounts.urls')),
    path('scouting/', include('Scouting.urls')),
    path('tba/', include('TheBlueAlliance.urls')),
    path('contact/', include('Contact.urls')),
    path('egg/', include('eggs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'ContentPages.views.permission_denied'
handler404 = 'ContentPages.views.page_not_found'
handler500 = 'ContentPages.views.server_error'
