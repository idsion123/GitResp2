from django.shortcuts import render,redirect,reverse,HttpResponse
from django.db.models import Q
from .forms import UserRegisterForm,UserLoginForm,UserForgetForm,UserResetForm,User_ChangeImageForm,User_ChangeInfoForm,User_ChangeEmailForm,User_ResetEmailForm
from . import models
from .models import UserProfile,EmailVerifyCode
from  django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.core.mail import send_mail
from tools.sent_email_tool import sent_email_code
from .models import BannerInfo
from orgs.models import OrgInfo,Teacherinfo
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from courses.models import CourseInfo
from datetime import datetime
from django.http import JsonResponse
from operations.models import  UserCourse,UserLove,UserMessage
from tools.decorators import login_decorator
# Create your views here.
def index(request):
    all_banners=BannerInfo.objects.all().order_by('-add_time')[:5]
    all_orgs=OrgInfo.objects.all()
    all_courses=CourseInfo.objects.all()
    return render(request,'index.html',{'base_type':'base','all_banners':all_banners,'all_orgs':all_orgs,'all_courses':all_courses})

def user_register(request):
    if request.method=='GET':
        #实例化form类，为了验证码
        user_register_form = UserRegisterForm()
        return render(request,'users/register.html',{'user_register_form':user_register_form})
    else:
        user_register_form=UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email=user_register_form.cleaned_data['email']
            password=user_register_form.cleaned_data['password']
            user_list=UserProfile.objects.filter(Q(username=email)|Q(email=email))

            if user_list:
                return render(request,'users/register.html',{'msg':'用户已存在'})
            else:
                a=UserProfile()
                a.username=email
                a.set_password(password)
                a.email=email
                a.save()
                #给用户邮箱发送邮件
                sent_email_code(email,1)
                return HttpResponse('请尽快前往您的邮箱激活，否则无法登录！')
                # return redirect(reverse('index'))
        else:
            return render(request, 'users/register.html', {'user_register_form': user_register_form})
def user_login(request):
    if request.method=='GET':
        return render(request,'users/login.html')
    else:
        userlogin_form=UserLoginForm(request.POST)

        if userlogin_form.is_valid():
            email=userlogin_form.cleaned_data['email']
            password=userlogin_form.cleaned_data['password']
            print(email,password)
            user=auth.authenticate(password=password,username=email)
            print(user)
            if user:
                if user.is_start:
                    auth.login(request,user)
                    #当登陆成功时加入一条消息
                    a =UserMessage()
                    a.message_man=request.user.id
                    a.message_content='欢迎登陆'
                    a.save()
                    url=request.COOKIES.get('url','/')
                    ret=redirect(url)
                    ret.delete_cookie('url')
                    return ret
                else:
                    return HttpResponse('请去邮箱中激活，否则无法登录')
            else:
                return render(request,'users/login.html',{'msg':'邮箱或者密码有错'})
        else:
            return render(request, 'users/login.html', {'userlogin_form':userlogin_form })

class CustomBackend(ModelBackend):
    """邮箱也能登录"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
def user_logout(request):
    auth.logout(request)
    return redirect(reverse('index'))
def user_active(request,code):
    if code:
        print(code)
        email_vel_list=models.EmailVerifyCode.objects.filter(code=code)
        if email_vel_list:
            print(email_vel_list)
            email_ver=email_vel_list[0]
            email=email_ver.email
            user_list=models.UserProfile.objects.filter(username=email)
            if user_list:
                print(user_list)
                user=user_list[0]
                user.is_start=True
                user.save()
                return redirect(reverse('users:user_login'))
        else:
            pass
    else:
        pass

def user_forget(request):
    if request.method =='GET':
        user_forget_form=UserForgetForm()
        return render(request,'users/forgetpwd.html',{'user_forget_form':user_forget_form})
    else:
        user_forget_form = UserForgetForm(request.POST)
        if user_forget_form.is_valid():
            email =user_forget_form.cleaned_data['email']
            user_list=models.UserProfile.objects.filter(username=email)
            if user_list:
                user=user_list[0]
                sent_email_code(email,2)
                return HttpResponse('请尽快去您的邮箱重置密码')
            else:
                msg='用户不存在'
                return render(request,'users/forgetpwd.html',{'msg':msg})
        else:
            return render(request, 'users/forgetpwd.html', {'user_forget_form': user_forget_form})
def user_reset(request,code):
    if code:
        if request.method == 'GET':
            return render(request,'users/password_reset.html', {'code':code})
        else:
            user_reset_form = UserResetForm(request.POST)
            print(1)
            if user_reset_form.is_valid():
                print(user_reset_form.cleaned_data)
                password = user_reset_form.cleaned_data['password']
                repassword = user_reset_form.cleaned_data['repassword']
                if password == repassword:
                    email_vel_list = EmailVerifyCode.objects.filter(code=code)
                    print(email_vel_list)
                    if email_vel_list:
                        email_vel = email_vel_list[0]
                        email = email_vel.email
                        print(email)
                        user_list = UserProfile.objects.filter(username=email)
                        if user_list:
                            user = user_list[0]
                            print(user.password)
                            print(user)
                            user.set_password(password)
                            user.save()
                            print(user.password)
                            return redirect(reverse('users:user_login'))
                        else:
                            pass
                    else:
                        pass
                else:
                    msg='两次密码不正确'
                    return render(request,'users/password_reset.html',{'msg':msg,'code':code})
            else:
                 return render(request, 'users/password_reset.html', {'user_reset_form': user_reset_form,'code':code})

@login_decorator
def user_info(request):
    return render(request,'users/usercenter-info.html',{'type':'info'})

def user_changeimage(request):
    #instance 指明实例是什么，做修改的时候我们要知道给哪个实例做修改，如果不指名会被当成创建实例，我们只有一张图片一定会报错
    user_changeimageform=User_ChangeImageForm(request.POST,request.FILES,instance=request.user)
    if user_changeimageform.is_valid():
        user_changeimageform.save(commit=True)
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status': 'fail'})
def user_changeinfo(request):
    user_changeinfo_form=User_ChangeInfoForm(request.POST,instance=request.user)
    if user_changeinfo_form.is_valid():

        user_changeinfo_form.save(commit=True)
        return JsonResponse({'status':'ok','msg':'修改成功'})
    else:
        return JsonResponse({'status': 'fail','msg':'修改失败'})

def user_changeemail(request):
    """
    当用户点击获取验证码的时候，会通过这个函数处理，发送邮箱验证码
    :param request: http请求对象
    :return: 返回json 数据，在模板页面中进行处理
    """
    user_changeemail_form=User_ChangeEmailForm(request.POST,instance=request.user)
    if user_changeemail_form.is_valid():
        email=user_changeemail_form.cleaned_data['email']
        user_list=UserProfile.objects.filter(Q(email=email)|Q(username=email))
        if  user_list:
            return JsonResponse({'status': 'fail', 'msg': '邮箱已经绑定'})
        else:
            #我们在发送邮箱验证码之前，应该去验证码的表去看看有么有往当前邮箱发送邮箱验证码的验证码
            email_ver_list=EmailVerifyCode.objects.filter(email=email,send_type=3)
            #如果发送过验证码，我们就拿到最近发送的验证码
            if email_ver_list:
                email_ver=email_ver_list.order_by('-add_time')[0]
                #判断当前时间与最近发送验证码的时间之差
                if (datetime.now()-email_ver.add_time).seconds>60:
                    sent_email_code(email,3)
                    email_ver.delete()
                    return JsonResponse({'status': 'ok', 'msg': '尽快去邮箱当中获取验证码'})
                else:
                    return JsonResponse({'status': 'fail', 'msg': '请不要重复发送验证码,1分钟后重试'})
            else:
                sent_email_code(email, 3)
                return JsonResponse({'status': 'ok', 'msg': '尽快去邮箱当中获取验证码'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '您的邮箱有问题'})

def user_resetemail(request):
    user_resetemail_form=User_ResetEmailForm(request.POST)
    if user_resetemail_form.is_valid():
        email=user_resetemail_form.cleaned_data['email']
        code=user_resetemail_form.cleaned_data['code']
        email_ver_list=EmailVerifyCode.objects.filter(email=email,code=code,send_type=3)
        if email_ver_list:
            email_ver=email_ver_list[0]
            if (datetime.now()-email_ver.add_time).seconds<60:
                request.user.email =email
                request.user.name=email
                request.user.save()
                return JsonResponse({'status': 'ok', 'msg': '邮箱修改成功'})
            else:
                return JsonResponse({'status': 'fail', 'msg': '验证码失效，请重新发送验证码'})
        else:
            return JsonResponse({'status': 'fail', 'msg': '邮箱或者验证码有错误'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '邮箱或者验证码不合法'})
def user_mycourse(request):
    mycourse=UserCourse.objects.filter(study_man=request.user)
    courses=[course.study_course for course in mycourse]
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(courses, 8)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request,'users/usercenter-mycourse.html',{'courses':courses,'pages':pages,'type':'course'})

def user_fav_org(request):
    orgs_objs=UserLove.objects.filter(love_man=request.user,love_status=True,love_type=1)
    orgs=[org.love_id for org in orgs_objs]
    org_list=OrgInfo.objects.filter(id__in=orgs)
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(org_list, 4)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request, 'users/usercenter-fav-org.html', {'org_list': org_list, 'pages': pages, 'type': 'fav'})

def user_fav_teacher(request):
    teacher_objs = UserLove.objects.filter(love_man=request.user, love_status=True, love_type=3)
    teachers=[teacher.love_id for teacher in teacher_objs]
    teacher_list=Teacherinfo.objects.filter(id__in=teachers)
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(teacher_list, 4)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request, 'users/usercenter-fav-teacher.html', {'teacher_list': teacher_list, 'pages': pages, 'type': 'fav'})

def user_fav_course(request):
    course_objs = UserLove.objects.filter(love_man=request.user, love_status=True, love_type=2)
    courses=[course.love_id for course in course_objs]
    course_list=CourseInfo.objects.filter(id__in=courses)
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(course_list, 8)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request, 'users/usercenter-fav-course.html', {'course_list': course_list, 'pages': pages, 'type': 'fav'})
def user_mymsg(request):
    user_mymsgs=UserMessage.objects.filter(message_man=request.user.id)
    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(user_mymsgs, 5)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request,'users/usercenter-message.html',{'user_mymsgs': user_mymsgs, 'pages': pages, 'type': 'msg'})

def handler_404(request,exception):
    return render(request,'handler_404.html',context={'error':'访问有误:页面不存在'}, status=404)
def handler_500(request,exception):
    return render(request, 'handler_500.html', context={'error':'访问有误:服务器错误'}, status=500)
