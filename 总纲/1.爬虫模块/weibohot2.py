import requests
import datetime
import time
import pymysql
from bs4 import BeautifulSoup
import random
import sys
hottime =''
sql = "insert into weibohot2(date,title,star_num,rank,link)values(%s, %s, %s,%s,%s)"
db = pymysql.connect("******", "******", "******", "******")
cursor = db.cursor()
n= 0

def gethot():
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }
    try:
        
        global hottime
        hottime = datetime.datetime.now().strftime("%Y%m%d.%H")
        hotweb = requests.get(url, headers=header, timeout=10)
    except:
        print(hottime+':http Error')
    else:
        soup = BeautifulSoup(hotweb.text, "html.parser")
        star_num = ''
        top = ''
        num = 0
        for ans in soup.find_all(attrs={'class': 'td-02'}):
            tag = ans.find('span')

            if tag is not None:

                top = ans.find('a').text

                link1 = ans.find('a').get('href')
                link = str('https://s.weibo.com') + str(link1)
                star_num = int(tag.get_text())
                num = num + 1
                cursor.execute(sql, (hottime, top, star_num, num, link))

        return top, star_num, num, link

errorcount=0#5次错误跳出循环
while True:
    try:
        gethot()
        # ret = gethot()
        # top = ret[0]
        # star_num = ret[1]
        # print(ret)





        # cursor.execute(sql, (hottime, top, star_num))
    except Exception as e:
        errorcount += 1
        db.rollback()
        print(hottime+":执行MySQL: %s 时出错：%s" % (sql, e))
        if(errorcount == 5):
            break
        else:
            time.sleep(10)
            continue
    else:
        db.commit()
        time.sleep(random.randint(28800, 28801))#每次sleep随机450-550秒




