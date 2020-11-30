from django.db import models

# Create your models here

CHOICES = (
    (True, "Listed"),
    (False, "Unlisted")
)

class inventory(models.Model):
    logical_uid = models.CharField(primary_key = True, max_length = 50, unique = True)
    name = models.CharField(max_length = 50, null = True)
    qty = models.IntegerField(blank = True, null = True)
    status = models.BooleanField(null = True, choices = CHOICES)
    def __str__(self):
        return self.logical_uid

class logging(models.Model):
    id = models.AutoField(primary_key=True, unique = True)
    logical_uid = models.ForeignKey('inventory',on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=144)
    qty = models.IntegerField()
    time = models.CharField(max_length = 144)
    warehouse = models.CharField(max_length = 144, default = "")
    
    def __str__(self):
        return str(self.logical_uid) if self.logical_uid else ''