from django.db import models

# Create your models here.
# 书信息
class BookInfo(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

# 管理员信息
class PeopleInfo(models.Model):
    name = models.CharField(max_length=30)
    gender = models.BooleanField()
    book =models.ForeignKey(BookInfo,on_delete=models.CASCADE)