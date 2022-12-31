from django.db import models

class Notice(models.Model):
    title=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Date=models.DateField()

    def __str__(self):
        return self.title
    


