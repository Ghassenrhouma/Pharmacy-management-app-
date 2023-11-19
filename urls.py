from django.urls import path,include 
from rest_framework import routers
from .views import DoctorViewSet,PatientViewSet,DrugViewSet,PrescriptionViewSet,LabratoryViewSet,AddressViewSet,PharmacistViewSet
#definir des routes
router=routers.DefaultRouter()
router.register(r'doctors',DoctorViewSet)
router.register(r'patients',PatientViewSet)
router.register(r'drungs',DrugViewSet)
router.register('persecreption',PrescriptionViewSet)
router.register('Labratory',LabratoryViewSet)
router.register('Address',AddressViewSet)

router.register('Pharmacist',PharmacistViewSet)
urlpatterns =[
    path('',include(router.urls))
]