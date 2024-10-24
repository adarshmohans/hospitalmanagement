from django.shortcuts import render
from . models import Department, Doctor

# Create your views here.
def index(request):
     department = Department.objects.all()
     doctor = Doctor.objects.all()
     
     context= {
          "department": department,
          "doctor": doctor
     }
     
     return render(request, 'index.html',context)

def about(request):
     department = Department.objects.all()
     doctor = Doctor.objects.all()
     
     context= {
          "department": department,
          "doctor": doctor
     }
     return render(request, 'about.html', context)

def error(request):
     return render(request, '404.html')

def appointment(request):
     return render(request, 'appointment.html')

def contact(request):
     return render(request, 'contact.html')

def feature(request):
     return render(request, 'feature.html')

def service(request):
     department = Department.objects.all()
     doctor = Doctor.objects.all()
     
     context= {
          "department": department,
          "doctor": doctor
     }
     return render(request, 'service.html', context)

def team(request):
     department = Department.objects.all()
     doctor = Doctor.objects.all()
     
     context= {
          "department": department,
          "doctor": doctor
     }
     return render(request, 'team.html', context)

def testimonial(request):
     return render(request, 'testimonial.html')