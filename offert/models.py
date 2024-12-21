from django.db import models

# Create your models here.

class Offert(models.Model):
    BUILD_CHOICES = [
        ('roof','Roof'),
        ('bathroom','Bathroom'),
        ('kitchen','Kitchen'),
        ('floor','Floor'),
        ('facade','Facade'),
        ('terrace','Terrace'),
        ('window_door_replacement','Widow/Door Replacement'),
        ('garage_door','Garage Door'),
        ('carport','Carport'),
        ('other','Other'),
    ]
    name = models.CharField(max_length=200)
    epost = models.EmailField()
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    option_service = models.CharField(choices=BUILD_CHOICES, default=other)
    job_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Offert by {self.name} wants {self.option_service} at {self.location}'