from django.db import models

# Create your models here.
# Nom
# text
# picture

class Articles(models.Model):
    title = models.CharField(max_length=100, default='')
    text = models.TextField()
    image = models.ImageField(upload_to='media/')
    
    def __str__(self) -> str:
        return self.title