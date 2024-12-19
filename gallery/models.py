from django.db import models

# Create your models here.

class Gallery(models.Model):

    image = models.ImageField(upload_to="images_work/")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f'{self.title} made around {self.created_at}'
