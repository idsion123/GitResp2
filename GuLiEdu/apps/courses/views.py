from django.shortcuts import render
from .models import CourseInfo,LessonInfo,VideoInfo,SourceInfo
from operations.models import UserLove,UserCourse,UserComment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.db.models import Q
from tools.decorators import login_decorator
# Create your views here.
def course_list(request):
    all_courses=CourseInfo.objects.all().order_by('-add_time')
    sort_courses=all_courses.order_by('-love_num')[:3]
    sort='add_time'
    sort =request.GET.get('sort')
    if not sort:
        sort='add_time'
    pagenum = request.GET.get('pagenum', '')
    keywords = request.GET.get('keywords', '')
    if keywords:
        all_courses = all_courses.filter(
            Q(name__icontains=keywords) | Q(desc__icontains=keywords) | Q(detail__icontains=keywords))
    if sort:
        all_courses=all_courses.order_by('-'+sort)
    pa = Paginator(all_courses,9)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request,'courses/course-list.html',{'all_courses':all_courses,'sort_courses':sort_courses,'base_type':'course','sort':sort,'pages':pages,'keywords':keywords})
def course_detail(request,course_id):
    if course_id:
        course=CourseInfo.objects.filter(id=int(course_id))[0]
        course.click_num+=1
        course.save()
        relate_course=CourseInfo.objects.filter(category=course.category).exclude(id=course.id)[:2]
        lovestatus = False
        org_lovestatus=False
        # 在返回页面数据的时候，需要返回收藏这个机构的状态，根据状态让模板页面显示收藏还是取消收藏，而不能让页面固定显示收藏
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=int(course_id), love_type=2, love_status=True)
            love1 = UserLove.objects.filter(love_man=request.user, love_id=int(course.orginfo.id), love_type=1, love_status=True)
            if love:
                lovestatus = True
            if love1:
                org_lovestatus=True
        return render(request,'courses/course-detail.html',{'course':course,'relate_course':relate_course,'lovestatus':lovestatus,'org_lovestatus':org_lovestatus,'base_type':'course'})
@login_decorator
def course_video(request,course_id):
    if course_id:
        course = CourseInfo.objects.filter(id=int(course_id))[0]
        lessons =LessonInfo.objects.filter(courseinfo_id=course_id)
        usercourse_list=UserCourse.objects.filter(study_man=request.user,study_course=course)
        #当用户点击开始学习以后，代表这个这个用户学习了该课程，我们需要去判断用户学习课程的表有没有学习这门课程的记录，如果没有需要去加上这门记录，说明用户学习了这门课程
        if not usercourse_list:
            a=UserCourse()
            a.study_man=request.user
            a.study_course=course
            a.save()
            course.study_num+=1
            course.save()
            #第一步：从学习课程的表中查找当前人学习的所有课程
            usercourse_list=UserCourse.objects.filter(study_man=request.user)
            course_list=  [usercourse.study_course  for usercourse in usercourse_list]
            #第二步：根据拿到的所有课程，找到每个课程的机构
            org_list=[course.orginfo  for course in course_list]
            if course.orginfo not in org_list:
                course.orginfo.study_num+=1
                course.orginfo.save()



        #学过该课的同学还学过什么课程
        #第一步：我们需要从中间表用户课程表当中找到该课的所有对象
        usercourse_list=UserCourse.objects.filter(study_course=course)
        #第二步 根据找到的用户学习课程页表拿到所有学习这门课程的用户列表
        user_list= [usercourse.study_man  for usercourse in usercourse_list]
        #第三步 再根据找到的用户从中间的用户学习表中找到用户学习其他课程的整个对象,需要用exclude去除当前的课程
        usercourse_list=UserCourse.objects.filter(study_man__in=user_list).exclude(study_course=course)
        #从获取到的用户课程列表中拿到我们学习过的其他课程
        course_list=list(set([course.study_course for course in usercourse_list]))
        return render(request,'courses/course-video.html',{'course':course,'lessons':lessons,'course_list':course_list,'base_type':'course'})
@login_decorator
def course_comment(request,course_id):
    if course_id:
        course = CourseInfo.objects.filter(id=int(course_id))[0]
        lessons = LessonInfo.objects.filter(courseinfo_id=course_id)
        usercourse_list = UserCourse.objects.filter(study_man=request.user, study_course=course)
        # 当用户点击开始学习以后，代表这个这个用户学习了该课程，我们需要去判断用户学习课程的表有没有学习这门课程的记录，如果没有需要去加上这门记录，说明用户学习了这门课程
        if not usercourse_list:
            a = UserCourse()
            a.study_man = request.user
            a.study_course = course
            a.save()
        # 学过该课的同学还学过什么课程
        # 第一步：我们需要从中间表用户课程表当中找到该课的所有对象
        usercourse_list = UserCourse.objects.filter(study_course=course)
        # 第二步 根据找到的用户学习课程页表拿到所有学习这门课程的用户列表
        user_list = [usercourse.study_man for usercourse in usercourse_list]
        # 第三步 再根据找到的用户从中间的用户学习表中找到用户学习其他课程的整个对象,需要用exclude去除当前的课程
        usercourse_list = UserCourse.objects.filter(study_man__in=user_list).exclude(study_course=course)
        # 从获取到的用户课程列表中拿到我们学习过的其他课程
        course_list = list(set([course.study_course for course in usercourse_list]))
        all_user_comment=UserComment.objects.filter(comment_course=course)
        return render(request, 'courses/course-comment.html',
                      {'course': course, 'lessons': lessons, 'course_list': course_list,'all_user_comment':all_user_comment,'base_type':'course'})