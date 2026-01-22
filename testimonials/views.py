from django.shortcuts import render
from .models import Testimonial
def testimonials(request): return render(request,'testimonials/list.html',{'testimonials':Testimonial.objects.all()})
