from django.db import models


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)  # e.g. Selected as SBI Clerk 2024
    message = models.TextField()
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.name

