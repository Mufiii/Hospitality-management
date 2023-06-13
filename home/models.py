from django.db import models

# Create your models here.


class Departments(models.Model) :
   dep_name = models.CharField(max_length=200)
   dep_desc = models.TextField() 
   
   def __str__(self) :
      return self.dep_name
   
class Doctors(models.Model) :
   doc_name = models.CharField(max_length=255)
   doc_spec = models.CharField(max_length=255)
   dep_name = models.ForeignKey(Departments , on_delete=models.CASCADE)
   doc_image = models.ImageField(upload_to='doctors')
   
   def __str__(self) :
      return 'Dr. ' + self.doc_name + "(" + self.doc_spec + ")"
   
   
class Booking(models.Model) :
   p_name = models.CharField(max_length=100)
   p_phone = models.CharField(max_length=20)
   p_email = models.EmailField(max_length=20)
   doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
   booking_date = models.DateField()
   booked_on = models.DateField(auto_now=True)
   
   def __str__(self) :
      return  self.p_name