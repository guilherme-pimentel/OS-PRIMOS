from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('medidores/', include('medidores.urls')),
    path('leituras/', include('leituras.urls')),
    path('faturas/', include('faturas.urls')),
    path('equipamentos/', include('equipamentos.urls')),
    path('admin/', admin.site.urls),
]
