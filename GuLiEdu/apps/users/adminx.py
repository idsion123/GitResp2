import xadmin
from .models import BannerInfo,EmailVerifyCode
# class UserProfileXadmin(object):
#     list_display=['image','nick_name','birthday','gender','address','phone','add_time']
from xadmin import views
#配置时
class BaseXadminSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalXadminSettings(object):
    """xadmin 的全局配置"""
    site_title='谷粒教育后台管理系统'
    site_footer='尚硅谷it教育'
    menu_style = "accordion"  # 设置菜单折叠


class BannerInfoXadmin(object):
    list_display = ['image', 'url','add_time']
    search_fields=['image','url']
    list_filter=['image','url']
    model_icon="fa fa-futbol-o"

class EmailVerifyCodeXadmin(object):
    list_display = ['code', 'email','send_type','add_time']
    model_icon="fa fa-envelope"

# xadmin.site.register(UserProfileXadmin)
xadmin.site.register(BannerInfo,BannerInfoXadmin)
xadmin.site.register(EmailVerifyCode,EmailVerifyCodeXadmin)
#注册全局样式类
xadmin.site.register(views.CommAdminView,GlobalXadminSettings)
#设置主题类
xadmin.site.register(views.BaseAdminView,BaseXadminSetting)