from django.db import models
from django.core.validators import FileExtensionValidator
from taggit.managers import TaggableManager
# Create your models here.
from django.utils import timezone

class Vedio(models.Model):
    vedio = models.FileField(upload_to='vedio_file', validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(upload_to='vedio_thumbnail', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "VIDEO"


class VedioComment(models.Model):
    vedio = models.ForeignKey(Vedio, on_delete=models.CASCADE, related_name='vedio_comment')
    name = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.vedio} commented {self.comment}"

class Audio(models.Model):
    audio = models.FileField(upload_to='audio_file', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    thumbnail = models.FileField(upload_to='audio_thumbnail', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description= models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "AUDIO"