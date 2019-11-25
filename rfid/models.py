from django.db import models

# Create your models here.

class rfid(models.Model):
    codigo = models.IntegerField(null=False) 
    status = models.CharField(max_length=100, null=False)

    idalumno = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'rfid'
