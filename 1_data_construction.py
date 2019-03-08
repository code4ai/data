import nltk
name_list=["wpb_eng","afp_eng","apw_eng","cna_eng","ltw_eng","nyt_eng","xin_eng"]

text_total=[]
for filename in os.listdir(name_list[1]):
    if filename == '.DS_Store' or filename[-3:]=='.gz':
        continue
    
    print 'processing the file' + np.str(filename)
    new_file = open(os.path.join(name_list[1], filename))
    f = BeautifulSoup(new_file,"html.parser")
    documents = f.find_all(attrs={"type": "story"})
    
    text_cluster = []
    for each_doc in documents:
        sent_cluster = []
        for sent in each_doc.find('text').find_all('p'):
            sent_cluster+=nltk.sent_tokenize(sent.get_text())
        
        sent_cluster = [nltk.word_tokenize(s.lower()) for s in sent_cluster]
        text_cluster.append([" ".join(sent) for sent in sent_cluster])
    
    text_total.append(text_cluster)

with open('~/2_raw_afp.txt', 'w') as f:
    for each_text in text_total:
        for sent_cluster in each_text:
            for sent in sent_cluster:
                f.writelines(sent.encode('utf-8'))
                f.writelines('\n')
            f.writelines('\n')
            