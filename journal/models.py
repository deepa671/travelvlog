from django.db import models

# Journal models

class Entry(models.Model):
    place = models.CharField(max_length=150)
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notes

    class Meta:
        ordering = ['date']

