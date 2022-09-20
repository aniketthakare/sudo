from django.db import models

# Create your models here.
class customers(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    emailid=models.CharField(max_length=25)
    mobile_no=models.IntegerField()

    def str(self):
        return self.first_name