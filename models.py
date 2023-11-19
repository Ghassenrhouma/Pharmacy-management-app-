from django.db import models
class Drug(models.Model):
     Code=models.PositiveIntegerField(primary_key=True)
     nom=models.CharField(max_length=30)
     prix=models.IntegerField()
     country=models.CharField(max_length=30)
     Datefin=models.DateField()
     Datefab=models.DateField()
     Stock=models.PositiveIntegerField(null=False,blank=False)
     photo= models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
     description= models.CharField(max_length=100)
class Patient(models.Model):
     numSS=models.PositiveIntegerField(primary_key=True)
     nom1=models.CharField(max_length=30)
     prenom=models.CharField(max_length=30)
     email=models.EmailField(max_length=250)
     numero=models.IntegerField()
     class Meta:
         db_table='patient'
     def __str__(self):
         return self.numSS
      
class Labratory(models.Model):
     nom2=models.CharField(primary_key=True,max_length=100)
     email2=models.EmailField(max_length=250)
     numero2=models.IntegerField()
     URL = models.URLField(max_length=200)
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street_number = models.CharField(max_length=50)
    street_name = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    class Meta:
        db_table = 'Address'
    def _str_(self):
        return'(',',',self.number,',',self.street,')'
      #return'(%s,%s,%s,%s)'%

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    firstName=models.CharField(max_length=100,default='')
    lastName=models.CharField(max_length=100,default='')
    date_of_birth = models.DateField()

    class Meta:
        abstract=True
    def __str__(self):
            return f'{self.firstName} {self.lastName}'
    

class Pharmacist(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    start_time = models.TimeField()

    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    class Meta:
        db_table = 'pharmacist'

class Doctor(Person):
    SPECIALITIES = [
        ('generalist', 'Généraliste'),
        ('orthopedist', 'Orthopédiste'),
        ('dermatologist', 'Dermatologue'),
        ('ophthalmologist', 'Ophtalmologue'),
        ('neurologist', 'Neurologue'),
        ('cardiologist', 'Cardiologue'),
        ('rheumatologist', 'Rhumatologue'),
        ('ENT', 'ORL'),
        ('other', 'Autre'),
    ]
#choices=[('generalist', 'Généraliste'),
       # ('orthopedist', 'Orthopédiste'),
       # ('dermatologist', 'Dermatologue'),
       # ('ophthalmologist', 'Ophtalmologue'),
       # ('neurologist', 'Neurologue'),
       # ('cardiologist', 'Cardiologue'),
       # ('rheumatologist', 'Rhumatologue'),
       # ('ENT', 'ORL'),
       # ('other', 'Autre'),]
   
   
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialty = models.CharField(max_length=20, choices=SPECIALITIES)
    address = models.ForeignKey(Address, on_delete=models.CASCADE,null=True, blank=True)
    class Meta:
        db_table = 'doctor'
    def __str__(self):
        return str(self.id)
class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    visit_date = models.DateField()
    treatment_duration = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        db_table = 'persecription'
