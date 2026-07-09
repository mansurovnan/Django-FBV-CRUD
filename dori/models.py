from django.db import models

# Create your models here.
from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    fabric = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

  
    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = 'drug'
        verbose_name_plural = 'drugs'
        ordering = ['name']