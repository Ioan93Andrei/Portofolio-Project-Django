from django.db import models
from django.db.models.fields import CharField

class Blog(models.Model):
  title = models.CharField(max_length=250)
  date = models.DateField(auto_now=False, auto_now_add=False)
  content = models.TextField(max_length=1000)
  image = models.ImageField(upload_to="blog/images/", blank=True)

  def __str__(self):
    return self.title