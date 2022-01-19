from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paciente/', include('paciente.urls')),
    path('auth/', include('medico.urls'))
]
