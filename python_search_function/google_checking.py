# เอา keyword ไป serach  ได้เเล้วเเต่ต้องการให้ return ออกมาเป็น url หรือ หน้าเว็บ
# import webbrowser
# while(True) :
#     new = 2
#     taburl = "https://www.google.com/search?q="
#     term = input("text : ")
#     webbrowser.open(taburl+term,new=new)

#function นี้ไม่ผ่าน
import urllib.parse
import urllib.request
    url = "https://www.google.com/search?"
    values = {'q':'python programing tutorials'}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data)
    resp =urllib.request.urlopen(req)
    respData = resp.read()

    print(respData)