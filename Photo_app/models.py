from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class PhotoCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')


    def __str__(self):
        return self.name


class PhotoAlbum(models.Model):
    category = models.ForeignKey(PhotoCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Photo_album', blank=True)
    caption = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cation