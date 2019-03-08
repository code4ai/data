# -*- coding: utf-8 -*-
from nltk.util import ngrams
from collections import Counter
name_list=["2_raw_wpb","2_raw_afp","2_raw_cna","2_raw_ltw","2_raw_nyt","2_raw_xin","2_raw_apw"]

def data_read(name):
    data = []
    with open('./'+name+'.txt','r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
                data.append(line)
    
    data = " ".join(data).split("\n \n ")
    punct = ["``", "''", '"', '-', ':', '[', ']', '--', '{' ,'}', '...', '_', '(', ')']
    for i in range(len(data)):
        for char in punct:
            data[i] = data[i].replace(char, ' ')
        data[i] = [" ".join(sent.split()) for sent in data[i].split('\n')]
    return data

def tag_num(data):
    data1=[]
    for d in data:
        dict_d = Counter(d)
        temp=[]
        for item in dict_d.items():
            for i in range(item[1]):
                temp.append(item[0]+'_'+str(i))
        data1.append(set(temp))
    return data1

def similarity(bi_gram_set1, bi_gram_set2):
    sent_inter = bi_gram_set1.intersection(bi_gram_set2)
    try:
        overlap1 = len(sent_inter)/float(len(bi_gram_set1))
        overlap2 = len(sent_inter)/float(len(bi_gram_set2))
    except:
        overlap1 = 0
        overlap2 = 0
    
    return overlap1, overlap2

def group_related_sents(sent_cluster, length_1=15, length_i=10, over_r1=0.20, over_r2=0.10):
    if sent_cluster == [] or len(sent_cluster[0].split())<length_1 :
        return 0
    
    bigram_cluster = []
    for sent in sent_cluster:
        if len(sent_cluster[0].split())<length_i:
            continue
        bigram_cluster.append([ bi[0]+'_'+bi[1] for bi in ngrams(sent.split(), 2)])
    bigram_set_cluster = tag_num(bigram_cluster)
    assert len(sent_cluster)==len(bigram_set_cluster)
    related_to_sent1 = [0]
    for i in range(1, len(bigram_set_cluster)):
        overlap1, overlap2 = similarity(bigram_set_cluster[0], bigram_set_cluster[i])
        if len(sent_cluster[i].split())>=length_i and (overlap1>over_r1 and overlap2>over_r2) \
            and (overlap1<0.9 and overlap2<0.9):
            related_to_sent1.append(i)
    return [sent_cluster[index] for index in related_to_sent1]
    
if __name__ == "__main__":
    num=0
    for name in name_list:
        related_sents=[]
        data = data_read(name)
        for sent_cluster in data:
            num+=1
            if num%10000==0:
                print "finished %d sentences"%num
            res = group_related_sents(sent_cluster)
            if res!=0 and len(res)>=2:
                related_sents.append(res)
        
        print name+"# of related sents from %s: %d"%(name, len(related_sents))
        print "\n"
    
        with open('./3_'+name[5:]+'.txt','w') as f:
            for sents in related_sents:
                for s in sents:
                    f.writelines(str(s))
                    f.writelines('\n')
                f.writelines('\n')
        