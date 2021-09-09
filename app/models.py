from django.db import models

class student(models.Model):
    ID=models.IntegerField(max_length=20)
    Roll_no=models.IntegerField(max_length=20)
    Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Name

