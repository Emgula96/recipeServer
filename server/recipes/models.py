from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    url = models.URLField(max_length=200, blank=True)  # New field added

    def __str__(self):
        return self.title
