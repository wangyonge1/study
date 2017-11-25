#_*_ coding:utf=8 _*_
from django.conf.urls import url
import views

urlpatterns = [

    url(r'^index/$',views.index),
    url(r'^article/(?P<article_id>[0-9]+)/$',views.article_page,name='article_page'),
    #正则表达式意思：给分组起了别名article_id(应与views.article_page函数的参数名一致)，匹配到的【0-9】数字会传给article_id
    url(r'^edit_page/(?P<article_id>[0-9]+)/$',views.edit_page,name='edit_page'),
    url(r'^edit/action/$',views.edit_action,name='edit_action'),
]