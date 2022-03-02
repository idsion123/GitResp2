from django.shortcuts import render
from . import models
from  operations.models import UserLove
from tools.pagenation import Pagenation
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
from django.db.models import Q
from tools.page import Page
def org_list(request):
    all_orgs=models.OrgInfo.objects.all()
    all_cities=models.CityInfo.objects.all()
    sort_orgs=all_orgs.order_by('-love_num')[:3]

    #全局搜索功能的过滤
    keywords=request.GET.get('keywords','')
    if keywords:
        all_orgs=all_orgs.filter(Q(name__icontains=keywords)|Q(desc__icontains=keywords)|Q(detail__icontains=keywords))



    #按照机构类别进行过滤筛选
    cate =request.GET.get('ct','')
    if cate:
        all_orgs=all_orgs.filter(category=cate)
    #按照机构地址进行过滤筛选
    cityid =request.GET.get('cityid','')
    if cityid:
        all_orgs=all_orgs.filter(city_info_id=int(cityid))
    # 按照学习人数进行排序
    sort = request.GET.get('sort', '')
    if sort:
        all_orgs = all_orgs.order_by('-' + sort)

    # #分页功能
    page=Page(request,all_orgs,3,cate,cityid,sort,keywords)
    return render(request,'orgs/org-list.html',{'all_orgs':all_orgs,'pages':page.pages,'all_cities':all_cities,'sort_orgs':sort_orgs,'page_html':page.page_html,'cate':cate,'cityid':cityid,'sort':sort,'base_type':'org','keywords':keywords})
def org_detail(request,org_id):
    if org_id:
        org=models.OrgInfo.objects.filter(id=int(org_id))[0]
        org.click_num +=1
        org.save()
        lovestatus=False
        #在返回页面数据的时候，需要返回收藏这个机构的状态，根据状态让模板页面显示收藏还是取消收藏，而不能让页面固定显示收藏
        if request.user.is_authenticated:
            love=UserLove.objects.filter(love_man=request.user,love_id=int(org_id),love_type=1,love_status=True)
            if love:
                lovestatus=True

        return render(request,'orgs/org-detail-homepage.html',{'org':org,'detail_type':'home','lovestatus':lovestatus,'base_type':'org'})
def org_detail_course(request,org_id):
    if org_id:
        org=models.OrgInfo.objects.filter(id=int(org_id))[0]
        all_courses=org.courseinfo_set.all()
        lovestatus = False
        # 在返回页面数据的时候，需要返回收藏这个机构的状态，根据状态让模板页面显示收藏还是取消收藏，而不能让页面固定显示收藏
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True
        page = Page(request, all_courses, 3, cate='', cityid='', sort='',keywords='')
        return render(request,'orgs/org-detail-course.html',{'org':org,'pages':page.pages,'page_html':page.page_html,'detail_type':'course','lovestatus':lovestatus,'base_type':'org'})
def org_detail_desc(request,org_id):
    if org_id:
        org=models.OrgInfo.objects.filter(id=int(org_id))[0]
        lovestatus = False
        # 在返回页面数据的时候，需要返回收藏这个机构的状态，根据状态让模板页面显示收藏还是取消收藏，而不能让页面固定显示收藏
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user,love_id=int(org_id),love_type=1,love_status=True)
            if love:
                lovestatus = True

        return render(request,'orgs/org-detail-desc.html',{'org':org,'detail_type':'desc','lovestatus':lovestatus,'base_type':'org'})
def org_detail_teachers(request,org_id):
    if org_id:
        org=models.OrgInfo.objects.filter(id=int(org_id))[0]
        lovestatus = False
        # 在返回页面数据的时候，需要返回收藏这个机构的状态，根据状态让模板页面显示收藏还是取消收藏，而不能让页面固定显示收藏
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True
        all_teachers =models.Teacherinfo.objects.filter(work_company=org)
        page = Page(request, all_teachers, 3, cate='', cityid='', sort='')
        return render(request,'orgs/org-detail-teachers.html',{'org':org,'pages':page.pages,'page_html':page.page_html,'detail_type':'teachers','lovestatus':lovestatus,'base_type':'org'})

def teacher_list(request):
    all_teachers=models.Teacherinfo.objects.all()
    sort_teachers=all_teachers.order_by('-love_num')[:3]
    sort = request.GET.get('sort')
    if sort:
        all_teachers=all_teachers.order_by('-click_num')
    keywords = request.GET.get('keywords', '')
    if keywords:
        all_teachers = all_teachers.filter(Q(name__icontains=keywords))
    pa = Paginator(all_teachers, 3)
    pagenum = request.GET.get('pagenum', '')
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)
    return render(request,'teachers/teachers-list.html',{'all_teachers':all_teachers,'sort_teachers':sort_teachers,'pages':pages,'sort':sort,'base_type':'teachers','keywords':keywords})


def teacher_detail(request,teacher_id):
    if teacher_id:
        teacher =models.Teacherinfo.objects.filter(id=int(teacher_id))[0]
        teacher.click_num+=1
        teacher.save()
        top_teachers=models.Teacherinfo.objects.filter(work_company=teacher.work_company).order_by('-love_num')[:3]
        lovestatus = False
        lovestatus1 = False
        # 在返回页面数据的时候，需要返回收藏这个机构的状态，根据状态让模板页面显示收藏还是取消收藏，而不能让页面固定显示收藏
        if request.user.is_authenticated:
            love = UserLove.objects.filter(love_man=request.user, love_id=int(teacher.work_company.id), love_type=1, love_status=True)
            love1 = UserLove.objects.filter(love_man=request.user, love_id=int(teacher.id), love_type=3,love_status=True)
            if love:
                lovestatus = True
            if love1:
                lovestatus1=True
        pa = Paginator(teacher.courseinfo_set.all(), 3)
        pagenum = request.GET.get('pagenum', '')
        try:
            pages = pa.page(pagenum)
        except PageNotAnInteger:
            pages = pa.page(1)
        except EmptyPage:
            pages = pa.page(pa.num_pages)
        return render(request,'teachers/teacher-detail.html',{'teacher':teacher,'lovestatus':lovestatus,'lovestatus1':lovestatus1,'top_teachers':top_teachers,'pages':pages,'base_type':'teachers'})