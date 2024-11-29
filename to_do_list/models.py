from django.db import models

# To-do list models

class Label(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    text = models.TextField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']