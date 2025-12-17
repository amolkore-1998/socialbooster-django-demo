from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    source = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
