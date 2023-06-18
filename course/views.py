from django.shortcuts import render
from rest_framework import status
# drf的函数式编程
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
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


@api_view(["GET", "PUT", "DELETE"])
def course_detail(request, pk):
    """
    获取、更新、删除一个课程
    :param request:
    :param pk:
    :return:
    """
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
    else:
        # 查到了课程信息，相关的操作发放到else
        if request.method == "GET":
            course = CourseSerializers(instance=course)
            return Response(data=course.data, status=status.HTTP_200_OK)
        if request.method == "PUT":
            course = CourseSerializers(instance=course, data=request.data)
            if course.is_valid():
                course.save()
                return Response(data=course.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=course.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == "DELETE":
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


"""
类视图
"""


class CourseList(APIView):

    def get(self, request):
        """
        :param request:
        :return:
        """
        course_queryset = Course.objects.all()
        # 注意这里的many参数，当查询是是用的是all()，即使只有一条数据，设置为True也不会有任何影响，但是如果是get或first进行查询，就不需要设置many参数
        course = CourseSerializers(instance=course_queryset, many=True)  # instance是查询集
        return Response(data=course.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:
        :return:
        """
        course = CourseSerializers(data=request.data)
        if course.is_valid():
            # 这里需要加上teacher参数
            course.save(teacher=self.request.user)
            print(f"request.data的数据类型是：{type(request.data)},course.data的数据类型是：{type(course.data)}")
            return Response(course.data, status=status.HTTP_201_CREATED)
        else:
            return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return

    def get(self, request, pk):
        """

        :param request:
        :param pk:
        :return:
        """
        obj = self.get_object(pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
        course = CourseSerializers(instance=obj)
        return Response(data=course, status=status.HTTP_200_OK)

    def post(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)

        course = CourseSerializers(instance=obj, data=request.data)

        if course.is_valid():
            course.save()
            return Response(data=course.data, status=status.HTTP_201_CREATED)
        return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"})
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
