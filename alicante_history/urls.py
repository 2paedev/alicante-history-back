from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from articles.urls import router as router_articles
from authors.urls import router as router_authors
from email_subscription.urls import router as router_email_subscription
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
