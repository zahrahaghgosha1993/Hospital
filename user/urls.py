from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('patient-list', views.patient_list, name='patient-list'),
    path('patient-create', views.patient_create, name='patient-create'),
    path('patient-update/<uuid:id>', views.patient_update, name='patient-update'),
    path('patient-delete/<uuid:id>', views.patient_delete, name='patient-delete'),
]