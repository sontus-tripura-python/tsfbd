from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class StudentCategory(models.Model):
    current_enroll_name = models.CharField(max_length=100,  null=True, blank=True)

    def __str__(self):
        return self.current_enroll_name

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='profile_pic', blank=True)
    university = models.CharField(max_length=100, blank=True)
    School = models.CharField(max_length=100, blank=True)
    college = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=20, default="Male", choices=(("Male", "Male"), ("Female", "Female")))
    status = models.CharField(max_length=30, default="Single", choices=(("Single", "Single"), ("Married", "Married"), ("In a Relationship","In a Relationship")))
    fathername = models.CharField(max_length=50, blank=True)
    mothername = models.CharField(max_length=50, blank=True)
    deparment = models.CharField(max_length=50, blank=True)
    current_enroll = models.ForeignKey(StudentCategory, on_delete=models.CASCADE, null=True, blank=True, related_name="current_enroll")
    religion = models.CharField(max_length=20, blank=True)
    Class = models.CharField(max_length=50, blank=True)
    Village = models.CharField(max_length=150, blank=True)
    thana = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    district = models.CharField(max_length=100, blank=True)
    current_city = models.CharField(max_length=100, blank=True)
    local_city = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(default="1990-02-02", null=True, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
