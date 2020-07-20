
from jieba import analyse

tfidf = analyse.extract_tags
inputfile_name = "../163news_domest.dat"
keywords_output = "../163news_keyword.dat"
for line in open(inputfile_name, encoding="utf-8"):

    text = line

    keywords = tfidf(text, allowPOS=('ns', 'nr', 'nt', 'nz', 'nl', 'n', 'vn', 'vd', 'vg', 'v', 'vf', 'a', 'an', 'i'))

    result = []

    for keyword in keywords:
        result.append(keyword)

    # print(result)
    fo = open(keywords_output, "a+", encoding="utf-8")

    for j in result:
        fo.write(j)
        fo.write(' ')

    fo.write('\n')
    fo.close()

print("Keywords Extraction Done!")
