from django.shortcuts import render

# Create your views here.
# Definir le crud
from rest_framework import viewsets 
from  .models import Doctor,Patient,Drug,Prescription,Labratory,Address,Pharmacist
from .serializers import DoctorSerializer,PatientSerializer,DrugSerializer,PrescriptionSerializer,LabratorySerializer,AddressSerializer,PharmacistSerializer
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()#recuperation des objets des doctors 
    serializer_class = PatientSerializer
class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    http_method_names = ['get','post'] #customize the methods 

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()#recuperation des objets des doctors 
    serializer_class = PrescriptionSerializer

class LabratoryViewSet(viewsets.ModelViewSet):
    queryset = Labratory.objects.all()#recuperation des objets des doctors 
    serializer_class = LabratorySerializer
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()#recuperation des objets des doctors 
    serializer_class = AddressSerializer



class PharmacistViewSet(viewsets.ModelViewSet):
    queryset = Pharmacist.objects.all()#recuperation des objets des doctors 
    serializer_class = PharmacistSerializer

