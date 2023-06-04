from django.db import models
from django.conf import settings


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="课程名称", verbose_name="课程名称")
    introduction = models.TextField(help_text="课程介绍", verbose_name="课程介绍")
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="课程价格", verbose_name="课程价格")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, help_text="课程讲师",
                                verbose_name="课程讲师")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = "课程信息"
        ordering = ('price',)

    def __str__(self):
        return self.name


"""
drf序列化器的作用
1、验证处理request.data
2、验证器的参数
3、同时序列化多个参数
4、序列化的过程中添加
5、没有对无效的数据异常处理
"""

