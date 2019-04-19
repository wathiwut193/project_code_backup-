from pythainlp.tag import pos_tag
from pythainlp.corpus import wordnet
from pythainlp.corpus import stopwords
from pythainlp.util import normalize
import deepcut
import  re
import string
from nltk import RegexpParser

with open("news_input/7.txt", 'r', encoding='utf-8') as readfile:
    msg = readfile.read()
    #msg.split('\"')
    #msg = re.sub(r'\"\"','',msg)
    def text_precessing(msg):
        # ลบ เครื่องหมายคำพูด (punctuation)p
        # for punctuation in string.punctuation:
        #        msg = re.sub(r'\{}'.format(punctuation),'',msg)

        # ลบ separator เช่น \n \t
        msg = ' '.join(msg.split())
        print(msg)
        th_stop = tuple(stopwords.words('thai'))
        tokens = deepcut.tokenize(msg,custom_dict="custom_dict.txt")

        print("ตัดคำ"+str(tokens))

         # Remove stop words ภาษาไทย
        tokens = [i for i in tokens if not i in th_stop]
        print("ลบ stopword "+str(tokens))

        # หารากศัพท์ภาษาไทย
        # tokens_temp = []
        # for i in tokens:
        #       w_syn = wordnet.synsets(i)
        #       if (len(w_syn) > 0) and (len(w_syn[0].lemma_names('tha')) > 0):
        #             tokens_temp.append(w_syn[0].lemma_names('tha')[0])
        #       else:
        #             tokens_temp.append(i)
        # tokens = tokens_temp
        # print("รากศัพท์"+str(tokens))
        # ลบตัวเลข
        # tokens = [i for i in tokens if not i.isnumeric()]
        #
        # print("ลบตัวเลข"+str(tokens))
        # ลบช่องว่าง
        # tokens = [i for i in tokens if not ' ' in i]
        # print("ลบช่องว่าง"+str(tokens))
                #pos_tag(tokens,engine='unigram',corpus='orchid')
        return tokens


if __name__ == '__main__':
    #เรียกใช้  function ตัดคำเเละลบ stop word
    prepo = text_precessing(msg)
    #ทำ pos tag
    postag = pos_tag(prepo, engine='perceptron', corpus='orchid')
    #postag1 = pos_tag(prepo,engine='perceptron',corpus='orchid')
    #postag2 = pos_tag(prepo,engine='artagger',corpus='orchid')

    print("ติด postag "+str(postag))
    #print("")
    #print(postag1)
    #print("")
    #print(postag2)


    #ทำ chunking parser
