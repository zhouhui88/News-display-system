from django.shortcuts import render, redirect,render_to_response
from django.urls import reverse
from newsanalysis.models import User,news,weibohot,toutiao,news163_digit,news163_era,news163_fore,news163_fund,news163_sport,news163_star,news163_stock,news163_tech,weibohot_count
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import MySQLdb


import json
from django.core import serializers
import re
from django.utils.safestring import mark_safe

# Create your views here.


# 首页
def index(request):
    items = news.objects.all()

    return render_to_response('newsanalysis/index.html', locals())


# 登录界面
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    if not all([username, password]):
        return render(request, 'newsanalysis/login.html', {'errmsg': '数据不完整'})

    user = User.objects.get(username=username, password=password)
    if user is not None:

        return redirect(reverse('myproject:index'))
    else:
        return render(request, 'newsanalysis/login.html', {'errmsg': '用户名或密码错误'})


# 注册页面
def register(request):
    if request.method == 'GET':
        return render(request, 'newsanalysis/register.html')
    else:
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        allow = request.POST.get('allow')
        if not all([username, password]):
            return render(request, 'newsanalysis/register.html', {'errmsg': '数据不完整'})

        if allow != 'on':
            return render(request, 'newsanalysis/register.html', {'errmsg': '请同意协议'})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'newsanalysis/register.html', {'errmsg': '用户名已存在'})
        user = User()
        user.username = username
        user.password = password
        user.save()

        return redirect(reverse('myproject:index'))


def sina_top50(request):
    items = weibohot.objects.all()
    cus_list = weibohot.objects.all()
    paginator = Paginator(cus_list, 50)
    page = request.GET.get('page')
    all_page = int(weibohot.objects.count()/50)
    star_allnum =0
    try:
        contacts = paginator.page(page)# 该变量为一页显示的数目的集合类
        for contact in contacts:
            star_allnum += contact.star_num

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/sina_top50.html', locals())


def news_163(request):
    items = news.objects.all()

    return render(request, 'newsanalysis/news_163.html', locals())



def toutiao_news(request):

    cus_list = toutiao.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/toutiao.html',locals())


def news_163_domic(request):
    cus_list = news.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/domestic_news.html',locals())


def news_163_fore(request):
    cus_list = news163_fore.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/foreign_news_news.html',locals())


def news_163_star(request):
    cus_list = news163_star.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/star_entertainment.html',locals())


def news_163_sport(request):
    cus_list = news163_sport.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/sports_news.html',locals())


def news_163_stock(request):
    cus_list = news163_stock.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/stock_financing_news.html',locals())


def news_163_fund(request):
    cus_list = news163_fund.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/fund_financing_news.html',locals())


def news_163_tech(request):
    cus_list = news163_tech.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/science_technology_news.html',locals())


def news_163_digit(request):
    cus_list = news163_digit.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/digital_news.html',locals())


def news_163_era(request):
    cus_list = news163_era.objects.all()
    paginator = Paginator(cus_list, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)  # 该变量为一页显示的数目的集合类


    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'newsanalysis/allnews_163/new_era_news.html',locals())


def keyword_search(request):
    return render(request, 'newsanalysis/keyword_search.html')


def tendency(request):
    info_dates = weibohot_count.objects.values_list("count",flat=True)
    info_dates2 = weibohot_count.objects.values_list("date", flat=True)
    p = list(info_dates)
    p2 = list(info_dates2)
    p3 = str(p2).replace("\'", "\"")
    return render(request, 'newsanalysis/tendency.html',locals())


def point_analysis(request):
    kinds1 = news163_era.objects.all()
    pos1 = 0
    neg1 = 0
    neu1 = 0
    for kind in kinds1:
        if kind.analysis == "0":
            neu1 = neu1 + 1
        elif kind.analysis == "1":
            pos1 = pos1 + 1
        else:
            neg1 = neg1 + 1

    kinds2 = news.objects.all()
    pos2 = 0
    neg2 = 0
    neu2 = 0
    for kind in kinds2:
        if kind.analysis == "0":
            neu2 = neu2 + 1
        elif kind.analysis == "1":
            pos2 = pos2 + 1
        else:
            neg2 = neg2 + 1

    kinds3 = news163_fore.objects.all()
    pos3 = 0
    neg3 = 0
    neu3 = 0
    for kind in kinds3:
        if kind.analysis == "0":
            neu3 = neu3 + 1
        elif kind.analysis == "1":
            pos3 = pos3 + 1
        else:
            neg3 = neg3 + 1

    kinds4 = news163_sport.objects.all()
    pos4 = 0
    neg4 = 0
    neu4 = 0
    for kind in kinds4:
        if kind.analysis == "0":
            neu4 = neu4 + 1
        elif kind.analysis == "1":
            pos4 = pos4 + 1
        else:
            neg4 = neg4 + 1

    kinds5 = news163_stock.objects.all()
    pos5 = 0
    neg5 = 0
    neu5 = 0
    for kind in kinds5:
        if kind.analysis == "0":
            neu5 = neu5 + 1
        elif kind.analysis == "1":
            pos5 = pos5 + 1
        else:
            neg5 = neg5 + 1

    kinds6 = news163_fund.objects.all()
    pos6 = 0
    neg6 = 0
    neu6 = 0
    for kind in kinds6:
        if kind.analysis == "0":
            neu6 = neu6 + 1
        elif kind.analysis == "1":
            pos6 = pos6 + 1
        else:
            neg6 = neg6 + 1

    kinds7 = news163_tech.objects.all()
    pos7 = 0
    neg7 = 0
    neu7 = 0
    for kind in kinds7:
        if kind.analysis == "0":
            neu7 = neu7 + 1
        elif kind.analysis == "1":
            pos7 = pos7 + 1
        else:
            neg7 = neg7 + 1

    kinds8 = news163_digit.objects.all()
    pos8 = 0
    neg8 = 0
    neu8 = 0
    for kind in kinds8:
        if kind.analysis == "0":
            neu8 = neu8 + 1
        elif kind.analysis == "1":
            pos8 = pos8 + 1
        else:
            neg8 = neg8 + 1

    kinds9 = news163_star.objects.all()
    pos9 = 0
    neg9 = 0
    neu9 = 0
    for kind in kinds9:
        if kind.analysis == "0":
            neu9 = neu9 + 1
        elif kind.analysis == "1":
            pos9 = pos9 + 1
        else:
            neg9 = neg9 + 1

    kinds10 = toutiao.objects.all()
    pos10 = 0
    neg10 = 0
    neu10 = 0
    for kind in kinds9:
        if kind.analysis == "0":
            neu10 = neu10 + 1
        elif kind.analysis == "1":
            pos10 = pos10 + 1
        else:
            neg10 = neg10 + 1

    kinds11 = weibohot.objects.all()
    pos11 = 0
    neg11 = 0
    neu11 = 0
    for kind in kinds11:
        if kind.analysis == 0:
            neu11 = neu11 + 1
        elif kind.analysis == 1:
            pos11 = pos11 + 1
        else:
            neg11 = neg11 + 1
    return render(request,'newsanalysis/point_analysis.html',locals())


def group(li1, li2, table1):
    conn = MySQLdb.connect('******', '******', '******', '******', charset="utf8", use_unicode=True)
    cursor = conn.cursor()
    sql = "SELECT  source,COUNT(source) FROM {} GROUP BY source".format(table1)
    cursor.execute(sql)
    results = cursor.fetchall()
    for result in results:
        li1.append(result[0])
        li2.append(result[1])

    conn.close()
    return li1, li2


def media_analysis(request):
    sou1 = []
    cou1 = []
    group(sou1, cou1, "newsanalysis_news163_era")

    sou2 = []
    cou2 = []
    group(sou2, cou2,"newsanalysis_news163_digit")

    sou3 = []
    cou3 = []
    group(sou3, cou3, "newsanalysis_news")

    sou4 = []
    cou4 = []
    group(sou4, cou4, "newsanalysis_news163_fore")

    sou5 = []
    cou5 = []
    group(sou5, cou5, "newsanalysis_news163_fund")

    sou6 = []
    cou6 = []
    group(sou6, cou6, "newsanalysis_news163_sport")

    sou7 = []
    cou7 = []
    group(sou7, cou7, "newsanalysis_news163_star")

    sou8 = []
    cou8 = []
    group(sou8, cou8, "newsanalysis_news163_stock")

    sou9 = []
    cou9 = []
    group(sou9, cou9, "newsanalysis_news163_tech")

    sou10 = []
    cou10 = []
    group(sou10, cou10, "newsanalysis_toutiao")



    return render(request,'newsanalysis/media_analysis.html',locals() )












