"""
URL configuration for portfolio_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.db import connection
from django.http import JsonResponse
from django.urls import include, path


def root_view(request):
    return JsonResponse({"message": "Welcome to the Portfolio API"})


def ping_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")

    return JsonResponse({"ok": True, "db": "connected"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("portfolio.urls")),
    path("ping/", ping_view),
    path("", root_view),
]

if settings.DEBUG and not getattr(settings, "USE_SUPABASE_STORAGE", False):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
