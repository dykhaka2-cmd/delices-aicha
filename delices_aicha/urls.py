from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.http import HttpResponse
from django.contrib.auth.models import User

def creer_admin_temp(request):
    User.objects.filter(username='aicha').delete()
    User.objects.create_superuser(
        username='aicha',
        email='aicha@gmail.com',
        password='Delice2026!'
    )
    return HttpResponse("Admin recree avec succes ! Utilisateur: aicha")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('creer-admin-secret-xyz/', creer_admin_temp),
    path('', include('boutique.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]