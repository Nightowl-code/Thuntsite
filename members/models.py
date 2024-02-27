from django.db import models
from time import timezone

# Create your models here.
class SubmittedData(models.Model):
    text_data = models.TextField()

    
    def __str__(self):       
        return self.text_data