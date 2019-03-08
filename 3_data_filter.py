#%%
name_list1=["wpb","afp","cna","ltw","nyt","xin","apw"]
data=[]          
for name in name_list1:
    with open('3_'+name+'_eng.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            else:
               
                data.append(line) 
                    
data1 = " ".join(data).split("\n \n ")
data1 = [[e.split() for e in sents.split('\n')] for sents in data1]

#%%
from nltk.util import ngrams
from collections import Counter

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
    
punct=set(['a','b','c','d','e','f','g',
           'h','i','j','k','l','m','n',
           'o','p','q','r','s','t',
           'u','v','w','x','y','z',
           "'",',','.',' '])
    
def puncts_filter(sent):
    string = " ".join(sent)
    for char in string:
        if char not in punct:
            #print string
            return 0
    return 1

bigram_data = []
for cluster in data1:
    bigram_cluster = []
    for sent in cluster:
        bigram_cluster.append([bi[0]+'_'+bi[1] for bi in ngrams(sent, 2)])
    bigram_data.append(tag_num(bigram_cluster))

#%%
sent1_repeat = set()
sent2_repeat = set()
data2=[]
for i in range(len(data1)):
    '''
    m=0
    for sent in data1[i]:
        if puncts_filter(sent)==0:
            m=1
            break
    if m==0:
        continue
    '''
    if " ".join(data1[i][0]) in sent1_repeat or  " ".join(data1[i][1]) in sent2_repeat:
        continue
    else:
        sent1_repeat.add(" ".join(data1[i][0]))
        sent2_repeat.add(" ".join(data1[i][1]))
    
    temp=[]
    for j in range(1, len(bigram_data[i])):
        temp.append(similarity(bigram_data[i][0], bigram_data[i][j]))
    
    mark=0    
    for k in range(len(temp)):
        if temp[k][0]<0.22 or temp[k][1] <0.18 or temp[k][0]>0.65 or temp[k][1]>0.65:
            mark=1
            break
    
    if mark==0:
        data2.append(data1[i])
        
data3 = []
for clus in data2:
    if len(clus)>4:
        continue
    mark=1
    for s in clus:
        if len(s)<15:
            mark=0
            break
    if mark==1:
        data3.append(clus)     
print len(data3)       
l=[len(e) for e in data3]
print Counter(l)

#%%  
with open('./final_data_14w.txt','w') as f:
    for sents in data3:
        for e in sents:
            f.writelines(" ".join(e))
            f.writelines('\n')
        f.writelines('\n')
        


