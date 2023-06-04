from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

course_dict = {
    "name": "课程名称",
    "introduction": "课程介绍",
    "price": 0.11
}


# 使用django原生的 FBV编写API接口
@csrf_exempt
def course_list(request):
    if request.method == "GET":
        # return HttpResponse(json.dumps(course_dict), content_type="application/json")
        return JsonResponse(course_dict)
    if request.method == "POST":
        course = json.loads(request.body.decode('utf-8'))
        # return JsonResponse(course, status=False)
        return HttpResponse(json.dumps(course), content_type='application/json')


# django的cbv
@method_decorator(csrf_exempt, name='dispatch')
class CourseList(View):
    def get(self, request):
        return JsonResponse(course_dict)

    def post(self, request):
        course = json.loads(request.body.decode('utf-8'))
        # return JsonResponse(course, status=False)
        return HttpResponse(json.dumps(course), content_type='application/json')


"""
使用原生的，需要自己实现排序、认证、接口权限、限流等
"""
