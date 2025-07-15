from django.db import models

class Puzzle(models.Model):
    CATEGORY_CHOICES = [
        ('Logical', 'Logical'),
        ('Mathematical', 'Mathematical'),
        ('Arrangement', 'Arrangement'),
        ('Shape', 'Shape'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=255)
    asked_in = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    solved = models.BooleanField()

    def __str__(self):
        return f"{self.title} ({self.category})" 