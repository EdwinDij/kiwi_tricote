from django.db import models
from django.urls import reverse

# Create your models here.
# Nom
# text
# picture

class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128)
    text = models.TextField()
    image = models.ImageField(upload_to='media/')
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})
    