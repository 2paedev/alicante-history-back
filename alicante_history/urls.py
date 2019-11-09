from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from rest_framework import routers

from articles.urls import router as router_articles
from authors.urls import router as router_authors
from email_subscription.urls import router as router_email_subscription
from resume.urls import router as router_resume
from tags.urls import router as router_tags


class DefaultRouter(routers.DefaultRouter):
    """
    Extends `DefaultRouter` class to add a method for
    extending url routes from another router.
    """
    def extend(self, router):
        """
        Extend the routes with url routes of the passed in router.
        Args:
             router: SimpleRouter instance containing route definitions.
        """
        self.registry.extend(router.registry)


router = DefaultRouter()
router.extend(router_articles)
router.extend(router_authors)
router.extend(router_tags)
router.extend(router_email_subscription)
router.extend(router_resume)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^images/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
