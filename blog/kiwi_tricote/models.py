from django.db import models

# Create your models here.
# Nom
# text
# picture

class Articles(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
