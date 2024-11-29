from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='album')
    picture = models.ImageField(blank=False, null=False)
    description = models.CharField(max_length=350, null=False, blank=False)

    def __str__(self):
        return self.description