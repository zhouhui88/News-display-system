import requests
import json
import pandas
import re
import MySQLdb
from segAnalysis import get_content



# def news163_conn():
#     conn = MySQLdb.connect('******', '******', '******', '******', charset="utf8", use_unicode=True)
#     cursor = conn.cursor()
#     sql1 = """
#         select title from 01_domestic_news
#     """
#     cursor.execute(sql1)
#     data1 = cursor.fetchone()
#     polar, confd, text = get_content(str(data1))
#     polar1="1"
#     print(data1[0])
#     print("情感倾向："+str(polar))
#     sql2 = "update 01_domestic_news set analysis='%s' where title like '%s'" % (str(polar1), data1[0])
#     print(sql2)
#     cursor.execute(sql2)
#     conn.commit()
#     conn.close()

# news163_conn()

def cir_163(table_name):

    conn = MySQLdb.connect('******', '******', '******', '******', charset="utf8", use_unicode=True)
    cursor = conn.cursor()
    sql1 = """
         select title from {}
            """.format(table_name)
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    # print(data1)
    n = 0
    for data in data1:
        title = data[0]

        polar, confd, text = get_content(title)
        sql2 = "update {} set analysis='%s' where title like '%s'".format(table_name) % (str(polar), title)
        cursor.execute(sql2)
        conn.commit()
        n += 1

        print(str(table_name)+"第"+str(n)+"条数据情感分析完成:"+str(polar))
    conn.close()




table = [("08_sports"),("09_stock_financing"),("10_fund_financing"),("16_science_technology"),("20_digital"),("22_new_era"),]

for table_name in table:
    cir_163("newsanalysis_news")

























