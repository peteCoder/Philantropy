from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403, handler400
urlpatterns = [
    path('admin/', admin.site.urls),
    path('comment/', include('comment.urls')),
    path('', include("websiteapp.urls")),
    path('blog/', include("blogapp.urls")),
    path('members/', include("membersapp.urls")),
    path('members/', include("django.contrib.auth.urls")),
    #path('paypal/', include('paypal.standard.ipn.urls')),
    #path('api/', include('comment.api.urls')),
]


handler404 = 'blogapp.views.custom_page_not_found'
handler403 = 'blogapp.views.custom_permission_denied'
handler400 = 'blogapp.views.custom_bad_request'
handler500 = 'blogapp.views.custom_error_view'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
