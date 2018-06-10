# @Time    : 18-6-5 下午2:19
# @Author  : anhuafeng
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from .views import index,lista1,SearchView,show
urlpatterns = [
    url(r'^index/$',index,name='index'),
    url(r'^lists/$',lista1,name='list'),
    url(r'^search/$',SearchView.as_view(),name='search'),
    url(r'^show/$',show,name='show'),
    url(r'^tags/(?P<tcv>[0-9]+)/$',lista1,name='tags'),
    url(r'^xiangqing/(?P<sh>[0-9]+)/$',show,name='show_x'),
    url(r'^fenlei/(?P<fen>[0-9]+)/$',lista1,name='fenlei'),
]