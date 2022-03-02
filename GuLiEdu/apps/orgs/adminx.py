import xadmin
from .models import CityInfo,OrgInfo,Teacherinfo
# Create your models here.
class OrgInfoXadmin(object):
    list_display=['image_data','name','course_num','study_num','address','love_num','click_num','category','add_time','city_info']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']
    model_icon = "fa fa-university"

class CityInfoXadmin(object):
    list_display=['name','add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['name', 'add_time']
    model_icon="fa fa-paper-plane"





class TeacherinfoAadmin(object):
    list_display = ['image', 'name', 'work_year', 'work_position', 'work_style','work_company','age', 'love_num', 'click_num',
                    'add_time']
    model_icon = "fa fa-graduation-cap"
xadmin.site.register(OrgInfo,OrgInfoXadmin)
xadmin.site.register(CityInfo,CityInfoXadmin)
xadmin.site.register(Teacherinfo,TeacherinfoAadmin)