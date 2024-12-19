from django.db import models

# Create your models here.

class Employed(models.Model):
    name = models.CharField(max_length=130)
    image = models.ImageField(upload_to="images_employed/")
    role_in_company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Here is {self.name}. working with {self.role_in_company} in the company.'