from django.db import models

# Create your models here.
class Contact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=20, default="New", choices=(("New", "New"), ("Read", "Read"), ("Closed", "Closed")))
    sentTime =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact"
