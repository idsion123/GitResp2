from django.shortcuts import render
from .forms import UserAskForm,UserCommentForm
from django.http import JsonResponse
from . import models
from orgs.models import OrgInfo,Teacherinfo
from courses.models import CourseInfo
from tools.decorators import login_decorator
# Create your views here.
def user_ask(request):
    user_ask_form=UserAskForm(request.POST)
    if user_ask_form.is_valid():
        user_ask_form.save(commit=True)
        return  JsonResponse({'status':'ok','msg':'查询成功'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '查询失败'})
@login_decorator
def user_love(request):
    love_id=request.GET.get('love_id','')
    love_type=request.GET.get('love_type','')
    if love_id and love_type:
        #如果收藏的id和type同時存在，那么我们要先去收藏表查看有没有这项收藏记录
        love =models.UserLove.objects.filter(love_man=request.user,love_id=int(love_id),love_type=int(love_type))
        if love:
            #如果本来就已经存在收藏这个东西的记录，那么我们需要判断收藏的状态，如果收藏状态为真，代表之前收藏过，并且现在的页面上显示取消收藏，代表这次点击是为了取消收藏
            if love[0].love_status:
                love[0].love_status=False
                love[0].save()
                if int(love_type) ==1:
                    org=OrgInfo.objects.filter(id=int(love_id))[0]
                    org.love_num =org.love_num-1
                    org.save()
                if int(love_type)==2:
                    course=CourseInfo.objects.filter(id=int(love_id))[0]
                    course.love_num =course.love_num-1
                    course.save()
                if int(love_type) == 3:
                    teacher =Teacherinfo.objects.filter(id=int(love_id))[0]
                    teacher.love_num=teacher.love_num-1
                    teacher.save()
                return JsonResponse({'status':'ok','msg':'收藏'})
            else:
                #如果收藏状态为假，代表之前收藏过，并且现在的页面上应显示的是收藏，代表这次点击是为了收藏
                love[0].love_status=True
                love[0].save()
                if int(love_type) ==1:
                    org=OrgInfo.objects.filter(id=int(love_id))[0]
                    org.love_num =org.love_num+1
                    org.save()
                if int(love_type)==2:
                    course=CourseInfo.objects.filter(id=int(love_id))[0]
                    course.love_num =course.love_num+1
                    course.save()
                if int(love_type) == 3:
                    teacher =Teacherinfo.objects.filter(id=int(love_id))[0]
                    teacher.love_num=teacher.love_num+1
                    teacher.save()
                return JsonResponse({'status': 'ok', 'msg': '取消收藏'})
        else:
            #如果没哟收藏过，代表表没有这个记录，所以需要创建对象，然后把记录状态改为ture
            a=models.UserLove()
            a.love_man=request.user
            a.love_id=int(love_id)
            a.love_type=int(love_type)
            a.love_status=True
            a.save()
            if int(love_type) == 1:
                org = OrgInfo.objects.filter(id=int(love_id))[0]
                org.love_num = org.love_num + 1
                org.save()
            if int(love_type) == 2:
                course = CourseInfo.objects.filter(id=int(love_id))[0]
                course.love_num = course.love_num + 1
                course.save()
            if int(love_type) == 3:
                teacher = Teacherinfo.objects.filter(id=int(love_id))[0]
                teacher.love_num = teacher.love_num + 1
                teacher.save()
            return JsonResponse({'status': 'ok', 'msg': '取消收藏'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '收藏失败'})
def user_comment(request):
    user_comment_form=UserCommentForm(request.POST)
    if user_comment_form.is_valid():
        course=user_comment_form.cleaned_data['comment_course']
        content=user_comment_form.cleaned_data['comment_content']
        a=models.UserComment()
        a.comment_man=request.user
        a.comment_course_id=course
        a.comment_content=content
        a.save()
        return JsonResponse({'status': 'ok','msg': '评论成功'})
    else:
        return JsonResponse({'status':'fail', 'msg': '评论失败'})

def user_delete(request):
    love_id = request.GET.get('love_id', '')
    love_type = request.GET.get('love_type', '')
    if love_id and love_type:
        love = models.UserLove.objects.filter(love_man=request.user, love_id=int(love_id), love_type=int(love_type))
        if love:
            love[0].love_status=False
            love[0].save()
            return  JsonResponse({'status': 'ok','msg': '取消成功'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '取消失败'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '取消失败'})

def msg_delete(request):
    delete_id=request.POST.get('delete_id')
    if delete_id:
        msg=models.UserMessage.objects.filter(id=int(delete_id))[0]
        if msg:
            msg.message_status=True
            msg.save()
            return  JsonResponse({'status': 'ok','msg': '已读'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '读取失败'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '读取失败'})