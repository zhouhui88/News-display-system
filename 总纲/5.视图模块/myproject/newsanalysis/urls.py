from django.urls import re_path, include
from newsanalysis import views
app_name = '[myproject]'
urlpatterns = [
    re_path(r'^index$', views.index, name='index'),
    re_path(r'^login$', views.login),
    re_path(r'^register$', views.register, name='register'),
    re_path(r'^sina_top50$', views.sina_top50, name='sina_top50'),
    re_path(r'^news_163$', views.news_163, name='news_163'),
    re_path(r'^toutiao_news$', views.toutiao_news, name='toutiao'),
    re_path(r'^news_163_domic$', views.news_163_domic, name='news_163_domic'),
    re_path(r'^news_163_fore$', views.news_163_fore, name='news_163_fore'),
    re_path(r'^news_163_star$', views.news_163_star, name='news_163_star'),
    re_path(r'^news_163_sport$', views.news_163_sport, name='news_163_sport'),
    re_path(r'^news_163_stock$', views.news_163_stock, name='news_163_stock'),
    re_path(r'^news_163_fund$', views.news_163_fund, name='news_163_fund'),
    re_path(r'^news_163_tech$', views.news_163_tech, name='news_163_tech'),
    re_path(r'^news_163_digit$', views.news_163_digit, name='news_163_digit'),
    re_path(r'^news_163_era$', views.news_163_era, name='news_163_era'),
    re_path(r'^keyword_search$', views.keyword_search, name='keyword_search'),
    re_path(r'^tendency$', views.tendency, name='tendency'),
    re_path(r'^point_analysis$', views.point_analysis, name='point_analysis'),
    re_path(r'^media_analysis$', views.media_analysis, name='media_analysis'),

]
