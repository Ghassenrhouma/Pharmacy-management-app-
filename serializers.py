#serialize classes implementations 
from rest_framework import serializers
from .models import Doctor,Patient,Drug,Prescription,Labratory,Address,Pharmacist
class DoctorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Doctor
        fields='__all__'#les champs qu'on va serializer
class PatientSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Patient
        fields='__all__'#les champs qu'on va serializer
class DrugSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Drug
        fields='__all__'#les champs qu'on va serializer

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Prescription
        fields='__all__'
class LabratorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Labratory
        fields='__all__'
class AddressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Address
        fields='__all__'

class  PharmacistSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Pharmacist
        fields='__all__'