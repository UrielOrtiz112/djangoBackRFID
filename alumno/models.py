from django.db import models
from django.utils import timezone

# Create your models here.


class alumno(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=100, null=False)
    ap_mat = models.CharField(max_length=100, null=False)
    fecha = models.DateTimeField(default = timezone.now)

    idrfid = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'alumno'
