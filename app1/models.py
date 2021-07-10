from django.db import models

# Create your models here.
class Students(models.Models):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntergerField()
    
