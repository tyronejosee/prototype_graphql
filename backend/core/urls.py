"""
URL configuration for core project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from graphene_django.views import GraphQLView

urlpatterns = [
    path("", RedirectView.as_view(url="/admin/")),
    path("admin/", admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True)),
]

# Debug config
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )


# AdminSite props.
# admin.site.site_header = settings.PROJECT_NAME
# admin.site.site_title = settings.PROJECT_NAME
# admin.site.index_title = "Admin"
