from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
# Create your models here.
class NoticeBoard(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    description = RichTextUploadingField()
    posted_name = models.CharField(max_length=50)
    facebook = models.URLField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Notice Board'