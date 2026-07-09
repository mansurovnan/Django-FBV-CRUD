from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['full_name']