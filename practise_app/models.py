from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.text import slugify 
from django.urls import reverse

# Create your models here.
class Contacts(models.Model):
    name = models.TextField(max_length=20)
    surname = models.TextField(max_length=20)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(120)])
    slug = models.SlugField(default="", null=False, db_index=True)

    # def __save__(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    
    def get_absolute_url(self):
        return reverse("contact-detail", args=[self.slug])
    