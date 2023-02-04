from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    name = models.TextField(max_length=40)
    surname = models.TextField(max_length=40)
    age = models.IntegerField()
    photo = models.FilePathField(path="/Users/nikitalutsai/VScodeProjects/practise1/nikita/static/nikita/images")
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.slug}"
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.slug])
