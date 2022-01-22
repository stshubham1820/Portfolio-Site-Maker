from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CommaSeparatedIntegerField
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class user_profile(models.Model):
    user_name = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=100)
    passion = models.CharField(max_length=100)
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    linkidin = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    skype = models.URLField(max_length=200)
class user_about(models.Model):
    d_choice = (
        ('1','Higher Education'),
        ('2','Bachelor'),
        ('3','Diploma'),
        ('4','Master'),
    )
    f_choice = (
        ('1','Available'),
        ('2','Not Available')
    )
    user = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    job_profile = models.CharField(max_length=100)
    job_desc = models.CharField(max_length=200)
    Dob = models.DateField(null = True)
    age = models.IntegerField(null = True)
    website = models.URLField(max_length=200)
    degree = models.CharField(max_length=1,choices=d_choice,null = True)
    phone = PhoneNumberField(unique = True, null = True, blank = False)
    email = models.EmailField(max_length = 254)
    city = models.CharField(max_length=200)
    Freelancer = models.CharField(max_length=1,choices=f_choice,null = True)
    about = models.TextField()
    clients = models.IntegerField(null = True)
    project = models.IntegerField(null = True)
    Hrs = models.IntegerField(null = True)
    Awards = models.IntegerField(null = True)
class resume(models.Model):
    user = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    skill= models.CharField(verbose_name="Seperate Skills With Comma",max_length=200)
    skillpercentage = models.CharField(validators=[CommaSeparatedIntegerField],max_length=200)
    highereducationtitle = models.CharField(max_length=100)
    highereducationYear = models.CharField(max_length=100)
    highereducationName = models.CharField(max_length=100)
    highereducationDescription = models.TextField()
    primaryeducationtitle = models.CharField(max_length=100)
    primaryeducationYear = models.CharField(max_length=100)
    primaryeducationName = models.CharField(max_length=100)
    primaryeducationDescription = models.TextField()
    primaryWorktitle = models.CharField(max_length=100)
    primaryWorkYear = models.CharField(max_length=100)
    primaryWorkName = models.CharField(max_length=100)
    primaryWorkDescription = models.TextField()
    secondaryWorktitle = models.CharField(max_length=100)
    secondaryWorkYear = models.CharField(max_length=100)
    secondaryWorkName = models.CharField(max_length=100)
    secondaryWorkDescription = models.TextField()
class intrest(models.Model):
    user = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    icon = models.CharField(max_length=50)
    intrest = models.CharField(max_length=50)
class testimonial(models.Model):
    user = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    ClientName = models.CharField(("Name"), max_length=100)
    ClientProfile = models.CharField(("Profile"), max_length=100)
    ClientWords = models.TextField()
    ClientImage = models.ImageField(upload_to='media/',null=True)
class Service(models.Model):
    user = models.ForeignKey(user_profile, on_delete=models.CASCADE)
    ServiceIcon = models.CharField(max_length=50)
    ServiceName = models.CharField(max_length=50)
    ServiceDiscription = models.TextField()
class Images(models.Model):
    User =  models.ForeignKey(user_profile, on_delete=models.CASCADE)
    Name = models.CharField(("Name"),max_length=50)
    Category = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='media',null=True)