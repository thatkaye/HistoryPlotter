from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class uploadfilemodel(models.Model):
    file = models.FileField(null = True)

    class Meta:
        db_table = "uploads"

class Post(models.Model):
    body = RichTextField(blank=True, null = True)