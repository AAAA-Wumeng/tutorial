from django.contrib import admin

# Register your models here.

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ('name', 'introduction', 'price', 'teacher')
    # 可以搜索的字段
    search_fields = list_display
    list_filter = list_display
