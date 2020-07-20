# -*- coding: utf-8 -*-

import requests
import md5sign
from bs4 import BeautifulSoup
import json
import sys,importlib

importlib.reload(sys)


def get_content(plus_item):
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"  # API地址
    params = md5sign.get_params(plus_item)#获取请求参数
    url=url+'?'+params#请求地址拼接
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        allcontents=soup.select('body')[0].text.strip()
        allcontents_json=json.loads(allcontents)#str转成dict

        return allcontents_json["data"]["polar"],allcontents_json["data"]["confd"],allcontents_json["data"]["text"]
    except Exception as e:
        print('a'+ str(e))
        return 0,0,0


if __name__ == '__main__':
    polar, confd, text = get_content('高通：苹果专利侵权需赔偿3100万美元')
    print('情感倾向：'+str(polar)+'\n'+'程度：'+str(confd)+'\n'+'文本：'+text)
