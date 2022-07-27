from djongo import models

# Create your models here.

class login(models.Model):
    id= models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    class Meta:
        abstract = True