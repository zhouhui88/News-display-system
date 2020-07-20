

import jieba
# import string
# import sys
# import os
import pymysql


db = pymysql.connect(host='******', port=3306, user='******', password='******', db="******", charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)
db2 = pymysql.connect(host='******', port=3306, user='******', password='******', db="******", charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)
cursor1 = db.cursor()
cursor2 = db2.cursor()
sql1 = "select date,star_num from newsanalysis_weibohot"
sql2 = "insert into newsanalysis_weibohot_count(date,count)values(%s,%s)"
cursor1.execute(sql1)
results = cursor1.fetchall()

n = 0
all_count = 0
for result in results:
    n = n + 1
    if n % 50 == 0:
        cursor2.execute(sql2,(rq,all_count))
        all_count = 0
    rq = result["date"]
    # for n in range(0, 50):
    count = result["star_num"]
    all_count = all_count + count
    print(str(rq) + "：" + str(count) + "=" + str(all_count))


        #print("这是第50次打印"+str(all_count))
        #cursor.execute(sql2,(all_count))
cursor1.close()
cursor2.close()
db2.commit()





















