from django.db import models

# Create your models here.
class Finch(models.Model):
  # First define the attributes/fields
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  # Django will create inputs for a form
  # TextField will create a <textarea>
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return f'{self.name} ({self.id})'
