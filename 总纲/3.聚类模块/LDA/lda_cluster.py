# coding=utf-8
import os, sys
import importlib

importlib.reload(sys)

from gensim.models import LdaModel, TfidfModel, LsiModel
from gensim import similarities
from gensim import corpora


def create_data(corpus_path):
    sentences = []
    sentence_dict = {}
    count = 0
    for line in open(corpus_path, encoding="utf-8"):
        # print line
        line = line.strip().split('\t')
        #print(len(line))
        if len(line) == 1:
            sentence_dict[count] = line[0]
            count += 1
            sentences.append(line[0].split(' '))
        else:
            break
    
    dictionary = corpora.Dictionary(sentences)
    
    corpus = [dictionary.doc2bow(text) for text in sentences]
    
    tfidf = TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    return sentence_dict, dictionary, corpus, corpus_tfidf


def lda_model(sentence_dict, dictionary, corpus, corpus_tfidf, cluster_keyword_lda):
    lda = LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=11)
    f_keyword = open(cluster_keyword_lda, 'w+', encoding="utf-8")
    for topic in lda.print_topics(5, 10):
        print('****' * 5)
        words = []
        for word in topic[1].split('+'):
            word = word.split('*')[1].replace(' ', '')
            words.append(word)
        f_keyword.write(str(topic[0]) + ' ' + ','.join(words) + '\n')
   
    corpus_lda = lda[corpus_tfidf]
    for doc in corpus_lda:
        print(len(doc), doc)
    return lda


def lsi_model(sentence_dict, dictionary, corpus, corpus_tfidf, cluster_keyword_lsi): 
    lsi = LsiModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=10)
    f_keyword = open(cluster_keyword_lsi, 'w+', encoding="utf-8")
    for topic in lsi.print_topics(5, 10):
        print("话题："+str(topic[0]))
        words = []
        for word in topic[1].split('+'):
            word = word.split('*')[1].replace(' ', '')
            words.append(word)
        f_keyword.write(str(topic[0]) + ' ' + ','.join(words) + '\n')

    return lsi


if __name__ == "__main__":
    corpus_path = "../../newsanalysis_news163_star.dat"
    cluster_keyword_lda = '../../newsanalysis_news163_star_lda.txt'
    cluster_keyword_lsi = '../../newsanalysis_news163_star_lsi.txt'
    sentence_dict, dictionary, corpus, corpus_tfidf = create_data(corpus_path)
    lsi_model(sentence_dict, dictionary, corpus, corpus_tfidf, cluster_keyword_lsi)
    lda_model(sentence_dict, dictionary, corpus, corpus_tfidf, cluster_keyword_lda)
