from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_active_user = models.BooleanField(default=True)

    class Meta:
        db_table = "accounts"

    def __str__(self):
        return f"O nome da conta é {self.username}"
