from django.db import models
# Create your models here.
class Members(models.Model):
    email = models.CharField(primary_key=True, null=False , editable=False, max_length = 100)
    name = models.CharField(max_length = 250)
    number = models.CharField(max_length = 20)
    pin = models.CharField(max_length = 20)

    def __str__(self):
        return '{}'.format(self.email)   

class Support(models.Model):
    email = models.CharField(primary_key=True, null=False , editable=False, max_length = 100)
    def __str__(self):
        return '{}'.format(self.email)   

class Opinion(models.Model):
    p_id = models.CharField(null=False , editable=False, max_length = 100)
    opinion = models.TextField()
    def __str__(self):
        return '{}'.format(self.p_id)   

class Contact(models.Model):
    name = models.CharField(max_length = 250)
    email = models.CharField(null=False , editable=False, max_length = 100)
    number = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 20)
    message = models.TextField()

    def __str__(self):
        return '{}'.format(self.email)   
