
from django.contrib import admin
from django.urls import path, include
from core.views import home
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', home),
 path('services/', include('services.urls')),
 path('testimonials/', include('testimonials.urls')),
 path('contact/', include('contact.urls')),
 path('pages/', include('pages.urls')),

]
