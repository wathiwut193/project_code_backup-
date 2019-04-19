from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import deepcut
import re
import requests
from bs4 import BeautifulSoup
print('Text For URL')
data = requests.get('https://www.9mot.com/')
soup = BeautifulSoup(data.text,'html.parser')
url = []
for url_prepare in soup.find_all("a", {"class": "more-link"}):
    url.append(url_prepare['href'])
print(url)
# url = ["https://www.9mot.com/2016/12/maecham-chianmai-rice-terrace/",
# "https://www.9mot.com/2016/10/dream-home-stay-pabongpiang/",
# "https://www.9mot.com/2014/10/chiangmai-rice-terrace/",
# "https://www.9mot.com/2013/01/small-trip-big-proud/",
# "https://www.9mot.com/2014/10/review-dusit-d2-chiangmai/"]
# url = []
# for i in range(0,5):
#     url_input = input("Enter url: ")
#     url.append(url_input)
data_set = []
for i in range(0, len(url)):
    data = requests.get(url[i])
    soup = BeautifulSoup(data.text, 'html.parser')
    text = soup.find_all("h1") # <- ค่าที่ใช้ในการค้นหา
    data_set.extend(text)

with open("Text.txt", "w+", encoding="cp874" , ) as writefile:
    for i in data_set:
        text_sh = i.text
        print(text_sh)

        writefile.write(text_sh)
    writefile.close()
    print('..............................................................................................................................................................................................................')
    word_cut = deepcut.tokenize(text_sh)

with open("Text.txt","r",encoding="cp874")as readfile:
    word_cut = readfile.read()
    #pattern for filter text
    pattern = re.compile(r"[^\u0E00-\u0E7F']|^'|'$|''|\u0E46|'")

    #ตามหาอักขระพิเศษทั้งหมดจากชุดคำ
    char_to_remove = re.findall(pattern, word_cut)

    #ทำการสร้างข้อมูลชุดใหม่ขึ้นมาโดยไม่มีอักขระพิเศษที่อยู่ใน char_to_remove
    list_with_char_removed = [char for char in word_cut if not char in char_to_remove]

    result_string = ''.join(list_with_char_removed)
    result_string = result_string.split(' ')
    word_cut2 = deepcut.tokenize(result_string)

    readfile.close()
    W = open("Text.txt", 'w+')
    W.write(''.join(word_cut2))
    W.close()

    Re = open("Text.txt", 'r')
    data = deepcut.tokenize(Re.read())
    Re.close()

print('Deepcut : ' ,data)

# R = open("message.txt", 'r' ,encoding ="cp874")
# R2 = open("message2.txt" , 'r' ,encoding ="cp874")
# text = R.read().split(' ')
# text2 = R2.read().split(' ')
# R.close()
# R2.close()
#
# W = open("message_write.txt", 'w+')
# W2 = open("message_write2.txt", 'w+')
# W.write(''.join(text))
# W2.write(''.join(text2))
# W.close()
# W2.close()
#
# Re = open("message_write.txt", 'r')
# Re2 = open("message_write2.txt", 'r')
#
# data = deepcut.tokenize(Re.read())
# data += deepcut.tokenize(Re2.read())
#
# Re.close()
# Re2.close()
#
# print(data)
vectorizer = TfidfVectorizer(analyzer=lambda x:x.split(','))
X = vectorizer.fit_transform(data)

true_k = 4
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=10)
model.fit(X)

print('..............................................................................................................................................................................................................')
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
cluster = []


for i in range(true_k):
     text = ''
     print("Cluster %d:" % (i)),
     for ind in order_centroids[i, :10]:
         text += terms[ind] + ' '

     arr = text.split(' ')
     arr.pop()
     cluster.extend(arr)
     print(text)

print('..............................................................................................................................................................................................................')

found = 2

cnt = {}
for s in cluster:
    if s in cnt:
        cnt[s] += 1
    else:
        cnt[s] = 1
print('Count words : ',cnt)
print('..............................................................................................................................................................................................................')
# arr = []
# for att, value in cnt.items():
#     arr.append([att, value])
# print(arr)
max = []
for att, value in cnt.items():
    if (len(max) == 0):
        max.append([att, value])

    tempMax = max[0][1]
    tempAtt = att
    if (value > tempMax):
        max = []

    if (value >= tempMax):
        count = 0
        for i in range(len(max)):
            if (max[i][0] == att):
                max[i][1] = max[i][1] + 0
                break;
            else:
                count = count + 1

        if (count == len(max)):
            max.append([tempAtt, value])

print('Maximum : ' , max)
print('..............................................................................................................................................................................................................')

min = []
for att, value in cnt.items():
    if (len(min) == 0):
        min.append([att, value])

    tempMin = min[0][1]
    tempAtt = att
    if (value < tempMin):
        min = []

    if (value <= tempMin):
        count = 0
        for i in range(len(min)):
            if (min[i][0] == att):
                min[i][1] = min[i][1] + 1
                break;
            else:
                count = count + 1

        if (count == len(min)):
            min.append([tempAtt, value])

print('Minimum : ' , min)
# print("\n")
# print("Prediction")
#
# Y = vectorizer.transform(["ไม่"])
# prediction = model.predict(Y)
# print(prediction)
#
# Y = vectorizer.transform(["ไฝว้"])
# prediction = model.predict(Y)
# print(prediction)

