from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
class Page(Paginator):
    def __init__(self, request,object_list,per_page,cate,cityid,sort,keywords):
        Paginator.__init__(self, object_list, per_page, orphans=0,
                 allow_empty_first_page=True)
        #data 为传输的分页内容，per_page为每页显示的内容
        pagenum = request.GET.get('pagenum', '')
        pa = Paginator(object_list,per_page)
        try:
            pages = pa.page(pagenum)
        except PageNotAnInteger:
            pages = pa.page(1)
        except EmptyPage:
            pages = pa.page(pa.num_pages)
        page_list=['<div class ="pageturn"><ul class ="pagelist">']
        if pages.has_previous():
            page_list.append('<li class ="long"><a href="?pagenum={}&cate={}&cityid={}&sort={}&keywords={}">上一页</a> </li>'.format(pages.previous_page_number,cate,cityid,sort,keywords))
        for number in pages.paginator.page_range:
            if number ==pages.number:
                page_list.append('<li class ="active"> <a href="?pagenum={}&cate={}&cityid={}&sort={}&keywords={}">{}</a></li>'.format(number,cate,cityid,sort,keywords,number))
            else:
                page_list.append('<li> <a href="?pagenum={}&cate={}&cityid={}&sort={}&keywords={}">{}</a></li>'.format(number,cate,cityid,sort,keywords,number))
        if pages.has_next():
            page_list.append('<li class ="long"><a href="?pagenum={}&cate={}&cityid={}&sort={}&keywords={}">下一页</a></li>'.format(pages.next_page_number,cate,cityid,sort,keywords))
        page_list.append('</ul></div>')
        self.page_html = ''.join(page_list)
        self.pages=pages








