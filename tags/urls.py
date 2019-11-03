from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'tags', views.TagsViewSet)
# router.register(r'simple-articles', views.SimpleArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
