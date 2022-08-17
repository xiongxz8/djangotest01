from django.contrib import admin

# Register your models here.
# 注册用户的数据类
from books.models import BookInfo,PeopleInfo

admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
