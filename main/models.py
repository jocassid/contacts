from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=13)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

