
import jieba
# import string
# import sys
# import os
import pymysql

jieba.load_userdict("SogouLabDic.txt")
jieba.load_userdict("dict_baidu_utf8.txt")
jieba.load_userdict("dict_pangu.txt")
jieba.load_userdict("dict_sougou_utf8.txt")
jieba.load_userdict("dict_tencent_utf8.txt")
jieba.load_userdict("my_dict.txt")

stopwords = {}.fromkeys([line.rstrip() for line in open('Stopword.txt', encoding='UTF-8')])

db_name = "graduate"
table_name = "newsanalysis_news163_star"
row_name = "title"
outputfile_name = "../newsanalysis_news163_star.dat"

def get_data():
    print("连接MySql数据库...")

    db = pymysql.connect(host='******', port=3306, user='******', password='******', db=db_name, charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)

    cursor = db.cursor()
    sql_2 = "select {} from {} ".format(row_name, table_name)
    cursor.execute(sql_2)
    result_middle_1 = cursor.fetchall()
    for result_middle_2 in result_middle_1:
        result_middle = result_middle_2[row_name]  
        seg = jieba.lcut(result_middle)
        fo = open(outputfile_name, "a+", encoding='utf8')
        result = []
        for i in seg:

            if i not in stopwords:
                result.append(i)

            # fo = open("/Users/kimmeen/Downloads/P_Weibo/%s"%user_id, "w")

        for j in result:
            fo.write(j)
            fo.write(' ')

        fo.write('\n')
        if not fo.close():
            fo.close()
    db.close()
    print("解析完成!")


if __name__ == '__main__':

    print("进程开始...")
    get_data()

    print("Done!")
