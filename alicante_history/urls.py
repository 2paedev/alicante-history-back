from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
    path('', include('tags.urls')),
    path('', include('authors.urls')),
    path('', include('email_subscription.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
