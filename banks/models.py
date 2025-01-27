from django.db import models

class Bank(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=11, unique=True)
    branch_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.branch_name} - {self.ifsc}"
