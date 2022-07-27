from django.db import models

# Create your models here.

class CMS(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name