"""
Create on 22 /1 /2019 11:57

@Coder Wathiwut Kongjan
"""
import deepcut
import time
import re



def newsreader():
    start_time =time.time()

    """
    How :
        Read text for file .txt and Cut word

    Reference :
        Dictionary custom by add compond word from Wikipedia
    """

    read_news = open("news/input/news_1.txt",'r',encoding='utf-8')
    word_cut = deepcut.tokenize(read_news.read(), custom_dict='compond_word.txt')
    #print(word_cut)

    clean_word = []
    for word in word_cut:
        word = ''.join(word.split())
        word = word.replace(',','')
        word = word.replace(':', '')

        clean_word.append(word)
    print(clean_word)

    writenews = open("news/output/1_ตัด.txt",'w+',encoding='utf-8')
    writenews.write('|'.join(word_cut))
    #print(word_cut)


    print(len(word_cut))
    read_news.close()
    writenews.close()




    finnish_time = time.time()
    print(finnish_time-start_time)

newsreader()