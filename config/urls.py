from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from landing.views import index

urlpatterns = [
    path('', index, name="landing-index"),
    path('landing/', include('landing.urls')),
    path('academy/', include('academy.urls')),
    path('attachments/', include('attachments.urls', namespace='attachments')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('content/', include('content.urls')),
    path('forum/', include('forum.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('feedback/', include('feedback.urls')),
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)

