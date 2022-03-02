import xadmin
from .models import *
from .models import CourseInfo,VideoInfo,SourceInfo,LessonInfo
class CourseInfoXadmin(object):
    list_display=['image','name','study_time','study_num','level','love_num','click_num','desc','category','course_notice','course_need','teacher_tell','teacherinfo','orginfo','add_time']
    search_fields = ['name', 'add_time','category']
    list_filter = ['name', 'add_time','category']
    model_icon="fa fa-book"

class LessonInfoXadmin(object):
    list_display=['name','courseinfo','add_time']
    model_icon="fa fa-columns"

class VideoInfoXadmin(object):
    list_display = ['name', 'study_time','video','lessoninfo', 'add_time']
    model_icon ='fa fa-video-camera'


class SourceInfoXadmin(object):
    list_display=['name','down_load','course_info','add_time']
    model_icon ="fa fa-file"

xadmin.site.register(CourseInfo,CourseInfoXadmin)
xadmin.site.register(LessonInfo,LessonInfoXadmin)
xadmin.site.register(VideoInfo,VideoInfoXadmin)
xadmin.site.register(SourceInfo,SourceInfoXadmin)