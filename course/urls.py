# -*- coding: utf-8 -*-
"""
@Project ：tutorial 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：meng
@Date    ：2023/6/4 22:30 
"""
from django.urls import path, include
from course import views

urlpatterns = [
    # Function Based View
    path("fbv/list/", views.course_list, name="fbv-list"),
    path("fbv/detail/<int:pk>/", views.course_detail, name='fbv-detail')

]

if __name__ == '__main__':
    print('Python')
