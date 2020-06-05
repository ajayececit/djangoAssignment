from django.db import models

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length = 254) 
    # Further update on table goes here

    def __str__(self):
        return self.firstName
