from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from PIL import Image
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title') 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news_description = RichTextUploadingField()
    posted_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news_pic', blank=True)
    facebook = models.URLField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)
        
        if img.height > 500 or img.width > 500:
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name_plural = 'NEWS'


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = "COMMENT"
