from django.db import models

# Create your models here.

# user model


class UserModel(models.Model):
    
    user_id = models.IntegerField(max_length=32)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    create_at = models.DateTimeField()

    def isExist(self):
        return False

# order model


class OrderModel(models.Model):
    # 32 length for business
    business_id = models.CharField(max_length=32)
    uid = models.CharField(max_length=16)
    create_at = models.DateTimeField()
