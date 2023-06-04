# -*- coding: utf-8 -*-
"""
@Project ：tutorial 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：meng
@Date    ：2023/6/4 17:46 
"""
# 导入序列化类和模型类
from rest_framework import serializers
from .models import Course
# 导入用户的模型类
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        module = User
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    # 获取teacher的名称
    # teacher = serializers.CharField(source='teacher.username')
    # 外键字段只读
    teacher = serializers.ReadOnlyField(source='teacher.username')

    class Meta:
        model = Course
        # 需要排除的字段
        # exclude = ("id",)
        # # 指定模型中需要进行序列化的字段
        # fields = ('name', 'introduction', 'price', 'teacher')
        # 对模型中所有的字段进行序列化
        fields = '__all__'
        # 对于外键字段的序列化可以设置深度
        depth = 2

# class CourseSerializers(serializers.ModelSerializer):
#     # 外键字段只读
#     teacher = serializers.ReadOnlyField(source='teacher.username')
#
#     class Meta:
#         model = Course
#
#         # # 指定模型中需要进行序列化的字段
#         # 再接口返回时，返回请求的url，url说默认值，可以在settings.py中设置URL_FIELD_NAME使全局生效
#         fields = ('name', 'url', 'introduction', 'price', 'teacher', 'created_at', 'updated_at')




if __name__ == '__main__':
    print('Python')
