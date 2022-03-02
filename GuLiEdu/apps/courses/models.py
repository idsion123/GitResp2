from django.db import models
from datetime import datetime
from orgs.models import OrgInfo,Teacherinfo
# Create your models here.
class CourseInfo(models.Model):
    image=models.ImageField(upload_to='course/',max_length=200,verbose_name='课程封面')
    name=models.CharField(max_length=20,verbose_name='课程名称')
    study_time=models.IntegerField(default=0,verbose_name='学习时常')
    study_num=models.IntegerField(default=0,verbose_name='学习人数')
    level=models.CharField(choices=(('gj','高级'),('zj','中级'),('cj','初级')),max_length=5,verbose_name='课程难度',default='cj')
    love_num =models.IntegerField(default=0,verbose_name='收藏量')
    click_num=models.IntegerField(default=0,verbose_name='访问量')
    desc=models.CharField(max_length=200,verbose_name='课程简介')
    detail=models.TextField(verbose_name='课程详情')
    category=models.CharField(choices=(('qd','前端'),('hd','后端'),('ai','人工智能')),verbose_name='课程类型',max_length=5)
    course_notice=models.CharField(max_length=200,verbose_name='课程公告')
    course_need=models.CharField(max_length=100,verbose_name='课程需知')
    teacher_tell=models.CharField(max_length=100,verbose_name='老师教导')
    teacherinfo=models.ForeignKey('orgs.Teacherinfo',verbose_name='所属老师',on_delete=models.CASCADE)
    orginfo=models.ForeignKey('orgs.OrgInfo',verbose_name='所属机构',on_delete=models.CASCADE)
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='课程信息'
        verbose_name_plural=verbose_name

class LessonInfo(models.Model):
    name=models.CharField(max_length=30,verbose_name='章节名称')
    courseinfo=models.ForeignKey('CourseInfo',verbose_name='所属课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='章节信息'
        verbose_name_plural=verbose_name

class VideoInfo(models.Model):
    name=models.CharField(max_length=30,verbose_name='视频名称')
    study_time=models.IntegerField(default=0,verbose_name='视频时常')
    video=models.FileField(('文件'),upload_to='video/',null=True,blank=True)
    lessoninfo=models.ForeignKey('LessonInfo',verbose_name='所属章节',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name

class SourceInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='资源名称')
    down_load=models.FileField(upload_to='source/',verbose_name='资源下载',max_length=200)
    course_info=models.ForeignKey('CourseInfo',verbose_name='所属课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资源信息'
        verbose_name_plural = verbose_name


