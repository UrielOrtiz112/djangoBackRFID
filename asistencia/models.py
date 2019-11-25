from django.db import models
from django.utils import timezone

# Create your models here.


class asistencia(models.Model):
    fecha = models.DateTimeField(default = timezone.now)
    idalumno = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'asistencia'
