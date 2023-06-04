from django.shortcuts import render
from rest_framework import status
# drf的函数式编程
from rest_framework.decorators import api_view
from rest_framework.response import Response
from course.models import Course
from course.serializers import CourseSerializers


@api_view(["GET", "POST"])
def course_list(request):
    """
    获取课程信息，或者新增课程信息
    :param request:
    :return:
    """
    if request.method == "GET":

        # 序列化多个对象，所以需要将many设置为True
        course = CourseSerializers(instance=Course.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=course.data)
    elif request.method == "POST":
        # partial=True如果用户只传递了部分字段，那么就更新部分字段（这部分字段是非必填字段），但是需要注意models中对字段的定义
        course = CourseSerializers(data=request.data, partial=True)
        if course.is_valid():
            course.save(teacher=request.user)
            return Response(status=status.HTTP_201_CREATED, data=course.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=course.errors)
