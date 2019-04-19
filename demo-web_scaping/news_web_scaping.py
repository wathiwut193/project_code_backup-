import requests

get_url = input("enter url : ")
url = get_url
data = requests.get(url)
# print(data.status_code)
# print(data.text)

from bs4  import BeautifulSoup
soup = BeautifulSoup(data.text,'html.parser')
#print(soup.prettify())

x = soup.find_all("p")
text=' '
for i in x:
    text +=  i.text


a=open('news_output2.txt',mode='w+',encoding='utf-8')
a.writelines(text)
a.close()

