from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)  # e.g. 4.5
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title