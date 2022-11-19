from django.db import models

STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),)
GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)
# Create your models here.
class crud_student(models.Model):
    sname=models.CharField(max_length=70)
    sroll=models.IntegerField()
    course=models.CharField(max_length=40)
    doj=models.DateField()
    dob=models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    state=models.CharField(choices=STATE_CHOICES,max_length=500)
    nationality=models.CharField(max_length=60)
    mob=models.BigIntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'student'



