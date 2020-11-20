from django.db import models

# Create your models here.
class user(models.Model):
    uname = models.CharField(max_length = 144, unique = True)
    passwd = models.CharField(max_length = 144)
    permission = models.CharField(max_length = 144)
    def __str__(self):
        return self.uname

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

CHOICES_LOGGING = (
    (True, "In"),
    (False, "Out")
)

class logging(models.Model):
    logical_uid = models.ForeignKey('inventory', to_field="logical_uid", on_delete=models.CASCADE)
    status = models.BooleanField(null = True, choices = CHOICES_LOGGING)
    qty = models.IntegerField()
    time = models.CharField(max_length = 144)

    def __str__(self):
        return str(self.logical_uid) if self.logical_uid else ''