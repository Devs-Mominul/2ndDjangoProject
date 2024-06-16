from django.shortcuts import render
from django.http import HttpResponse
from home.models import AboutUs
from home.models import Slider

# Create your views here.
def index(request):
   aboutdata=AboutUs.objects.all()[0]
   sliderdata=Slider.objects.all()[0]
   context={
       "about":aboutdata,
       "slider":sliderdata,
   }
   return render(request,"index.html",context)
  
    
    
    
