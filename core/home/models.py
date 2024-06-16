from django.db import models


# Create your models here.
class AboutUs(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=700,blank=False)
    image=models.ImageField(upload_to='about/',blank=False)
    def __str__(self):
        return self.title
class Slider(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=700,blank=False)
    image=models.ImageField(upload_to='slider/',blank=False)
    def __str__(self):
        return self.title
        
                            
