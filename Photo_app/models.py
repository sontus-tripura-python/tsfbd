from django.db import models
from PIL import Image
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        
        if img.height > 400 or img.width > 500:
            output_size =(400, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)