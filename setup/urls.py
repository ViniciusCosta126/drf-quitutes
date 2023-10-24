from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from quitutes.views import DoceViewSet
router = routers.DefaultRouter()
router.register('doces', DoceViewSet, basename='Alunos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
