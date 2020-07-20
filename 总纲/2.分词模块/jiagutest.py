import requests
import json
import pandas
import re
import MySQLdb

# url = 'http://c.m.163.com/nc/article/headline/T1348647853363/0-100.html'

header = {
    'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
    'Connection': 'keep - alive',
}
conn = MySQLdb.connect('******', '******', '******', '******', charset="utf8", use_unicode=True)
cursor = conn.cursor()
news_total = []


# table_name = "1_domestic_news"
# catagory = "BA10TA81wangning"


def news163_connect(catagory, table_name):
    for n in range(0, 50):
        url_0 = 'https://3g.163.com/touch/reconstruct/article/list/{0}/{1}-20.html'.format(catagory, n)
        # url_1 = url_0
        mydata = requests.get(url_0, headers=header).text
        print(type(mydata))
        p1 = re.compile(r'[(](.*)[)]', re.S)
        mydata1 = re.findall(p1, mydata)
        # print(len(mydata1))
        # print(mydata1[0])
        # wbdata = requests.get(url, headers=header).text
        # data = json.loads(wbdata)
        data = json.loads(str(mydata1[0]))
        news = data[catagory]

        for item in news:
            docid = item['docid']
            source = item['source']
            title = item['title']
            priority = item['priority']
            digest = item['digest']
            time = item['ptime']

            try:
                url = item['url']
            except:
                url = ''
            newes_data = {
                'title': title,  # '标题'
                'time': time,  # '时间'
                'source': source,  # '来源'
                'digest': digest,  # '内容'
                'url': url  # 链接'
            }
            # news_total.append(newes_data)

            # print(type(df))
            insert_sql = """ 
                        replace into {}(title, time, source, digest,url) VALUES (%s, %s, %s, %s, %s)
                        """.format(table_name)

            cursor.execute(insert_sql, (
                item['title'], item["ptime"], item["source"], item["digest"], item["url"]))

        print("第" + str(n) + "页爬取完毕\n")
    # df = pandas.DataFrame(news_total, columns=['title', 'time', 'source', 'digest', 'url'])
    # df.to_excel("news_net_all.xlsx")
    conn.commit()


kinds = [("BD29LPUBwangning", "01_domestic_news")]

for (catagory, table_name) in kinds:
    news163_connect(catagory, table_name)
