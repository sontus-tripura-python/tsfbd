from django.db import models
from autoslug import AutoSlugField
from PIL import Image
# Create your models here.
class CentralYear(models.Model):
    yearname = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='yearname')

    def __str__(self):
        return self.yearname

    class Meta:
        verbose_name_plural = "central year"

class CentralMember(models.Model):

    STATUS = (

    ('University', 'University'),
    ('College', 'College'),
    ('School', 'School'),
    ('Job', 'Job'),
    ('Other', 'Other'),
    )
    session = models.ForeignKey(CentralYear, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.jpg', upload_to='central')
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    position = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    village = models.CharField(max_length=200, blank=True)
    thana = models.CharField(max_length=200, blank=True)
    district = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=20, default="Male", choices=(("Male", "Male"), ("Female", "Female")))
    current_enroll = models.CharField(max_length=200, null=True, choices=STATUS)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 200 or img.width > 200:
            output_size =(200, 200)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    class Meta:
        verbose_name_plural = 'Central Member'

class BranchCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')


class BranchName(models.Model):
    branchname = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='branchname')
    branch_category = models.ForeignKey(BranchCategory, on_delete=models.CASCADE, related_name='branch_categories')

    def __str__(self):
        return self.branchname
    class Meta:
        verbose_name_plural = "Branch Name"

class BranchYear(models.Model):
    branchyear = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='branchyear')
    branches = models.ForeignKey(BranchName, on_delete=models.CASCADE, related_name='branch_names')

    class Meta:
        ordering = ('-id',)


    def __str__(self):
        return f"{self.branchyear } members of {self.branches}"

    class Meta:
        verbose_name_plural = "Branch year"

class BranchMember(models.Model):

    STATUS = (

    ('University', 'University'),
    ('College', 'College'),
    ('School', 'School'),
    ('Job', 'Job'),
    ('Other', 'Other'),
    )
    branch_year = models.ForeignKey(BranchYear, on_delete=models.CASCADE, related_name='branch_years')
    photo = models.ImageField(default='default.jpg', upload_to='branchmember', blank=True)
    University = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    slug = AutoSlugField(populate_from='name')
    position = models.CharField(max_length=50, blank=True)
    blood_group = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    gender = models.CharField(max_length=20, default="Male", choices=(("Male", "Male"), ("Female", "Female")))
    current_enroll = models.CharField(max_length=200, null=True, choices=STATUS)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = "Branch member"

    def __str__(self):
        return f"{self.name } of {self.branch_year}"

    def save(self):
        super().save()

        img = Image.open(self.photo.path)
        
        if img.height > 200 or img.width > 200:
            output_size =(200, 200)
            img.thumbnail(output_size)
            img.save(self.photo.path)


class Coordinator(models.Model):
    photo = models.ImageField(default='default.jpg', upload_to='branchmember', blank=True)
    name = models.CharField(max_length=50, blank=True)
    slug = AutoSlugField(populate_from='name')
    position = models.CharField(max_length=200, blank=True)
    about_description = models.TextField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self):
        super().save()

        img = Image.open(self.photo.path)
        
        if img.height > 200 or img.width > 200:
            output_size =(200, 200)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    class Meta:
        verbose_name_plural = "Co-ordinator"
