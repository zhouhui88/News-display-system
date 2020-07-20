import MySQLdb


def table2table(table_name1,table_name2):
    conn1 = MySQLdb.connect('******', '******', '******', '******', charset="utf8", use_unicode=True)
    conn2 = MySQLdb.connect('******', '******', '******', '******', charset="utf8", use_unicode=True)
    cursor1 = conn1.cursor()
    cursor2 = conn2.cursor()
    sql1 = "select * from {}".format(table_name1)
    sql2 = "insert into {}(id,title,time,source,digest,url,analysis)values(%s,%s, %s, %s,%s,%s,%s)".format(table_name2)
    cursor1.execute(sql1)
    results = cursor1.fetchall()
    for result in results:
        id = result[0]
        title = result[1]
        time = result[2]
        source = result[3]
        digest = result[4]
        url = result[5]
        analysis = result[6]
        cursor2.execute(sql2, (id, title, time, source, digest, url, analysis))
        conn2.commit()
    conn1.close()
    conn2.close()


tables = [("05_star_entertainment", "newsanalysis_news163_star"), ("08_sports", "newsanalysis_news163_sport"),("09_stock_financing", "newsanalysis_news163_stock"),("10_fund_financing", "newsanalysis_news163_fund"),
         ("16_science_technology", "newsanalysis_news163_tech"),
         ("20_digital", "newsanalysis_news163_digit"),
         ("22_new_era", "newsanalysis_news163_era")]



table2table("01_domestic_news", "newsanalysis_news")
















