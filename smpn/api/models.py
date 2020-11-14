from django.db import models

# Create your models here.
class user(models.Model):
    uname = models.CharField(max_length = 144)
    passwd = models.CharField(max_length = 144)
    permission = models.CharField(max_length = 144)
    def __str__(self):
        return self.uname

class inventory(models.Model):
    uid = models.CharField(primary_key = True, max_length = 50, unique = True)
    name = models.CharField(max_length = 50, null = True)
    qty = models.IntegerField(blank = True, null = True)
    def __str__(self):
        return self.uid

class logging(models.Model):
    id = models.AutoField(primary_key = True)
    uid = models.ForeignKey('inventory', to_field="uid", on_delete=models.CASCADE)
    status = models.CharField(max_length = 10)
    qty = models.IntegerField()
    time = models.CharField(max_length = 144)
    def __str__(self):
        return str(self.uid) if self.uid else ''