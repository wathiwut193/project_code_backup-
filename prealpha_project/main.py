import deepcut
import requests
from bs4 import BeautifulSoup
import re
import regex
import numpy as np
import codecs
import time
from pymongo import MongoClient


# function get news from website thairath only
def get_news(URL):
    data = requests.get(URL)
    soup = BeautifulSoup(data.text, 'html.parser')
    header = soup.find_all("h1")
    date_news = soup.find_all("div", {"class": "css-1cxbv8p evs3ejl7"})
    content = soup.find_all("p")

    text = ''
    for i in header:
        text += i.text
    for z in date_news:
        text += z.text
    for j in content:
        text += j.text

    return text


def word_tokenize(text):
    data = deepcut.tokenize(text, custom_dict='/dictionary/custom_dict.txt')
    return data


def get_dictionary():
    return


def date_time_tag_object(text):
    regex_time = r"(([0-1][\d]|[2][0-4])\s?(:|.)([0-5][\d])\s?(นาฬิกา|น\.|น)|(ช่วง|ตอน)(เช้า|ค่ำ|เย็น|ดึก|บ่าย|สาย|กลางดึก))"
    regex_date = (
        r"(([1-9]|[0-2][\d]|[3][0-1])\s?(/|-)?(ม\.ค\.|มกราคม|มกรา|ก\.พ\.|กุมภาพันธ์|กุมภา|มี\.ค\.|มีนาคม|มีนา|เม\.ย\.|"
        "เมษายน|เมษา|พ\.ค\.|พฤษภาคม|พฤษภา|มิ\.ย\.|มิถุนายน|มิถุนา|ก\.ค\.|กรกฎาคม|กรกฎา|ส\.ค\.|สิงหาคม|สิงหา|ก\.ย\.|"
        "กันยายน|กันยา|ต\.ค\.|ตุลาคม|ตุลา|พ\.ย\.|พฤศจิกายน|พฤศจิกา|ธ\.ค\.|ธันวาคม|ธันวาคม)\s?(/|-)?(พ.ศ.|ค.ศ.|พศ|คศ)?\s?"
        "(\d\d\d\d|\d\d)?|([1-9]|[0-2][\d]|[3][0-1])\s?(/|-|.)([0][\d]|[1][0-2])\s?(/|-|.)(\d\d\d\d|\d\d))")
    matches_time = regex.sub(regex_time, r'<time>\1</time>', text)
    read_text = matches_time
    matches_date = regex.sub(regex_date, r'<date>\1</date>', text)
    read_text += matches_date
    count = 0
    for matchNum, match in enumerate(matches_time):
        count += 1
        if match.group() == '<time>ช่วงเช้า</time>' or match.group() == '<time>ตอนเช้า</time>':
            print('เวลา : <time>06:00 น. - 08:59 น.</time>')
        elif match.group() == '<time>ช่วงสาย</time>' or match.group() == '<time>ตอนสาย</time>':
            print('เวลา : <time>09:00 น. - 10:59 น.</time>')
        elif match.group() == '<time>ช่วงเที่ยง</time>' or match.group() == '<time>ตอนเที่ยง</time>':
            print('เวลา : <time>11:00 น. - 12:59 น.</time>')
        elif match.group() == '<time>ช่วงบ่าย</time>' or match.group() == '<time>ตอนบ่าย</time>':
            print('เวลา : <time>13:00 น. - 15:59 น.</time>')
        elif match.group() == '<time>ช่วงเย็น</time>' or match.group() == '<time>ตอนเย็น</time>':
            print('เวลา : <time>16:00 น. - 18:59 น.</time>')
        elif match.group() == '<time>ช่วงค่ำ</time>' or match.group() == '<time>ตอนค่ำ</time>':
            print('เวลา : <time>19:00 น. - 20:59 น.</time>')
        elif match.group() == '<time>ช่วงดึก</time>' or match.group() == '<time>ตอนดึก</time>':
            print('เวลา : <time>21:00 น. - 02:59 น.</time>')
        elif match.group() == '<time>ช่วงกลางดึก</time>' or match.group() == '<time>ตอนกลางดึก</time>':
            print('เวลา : <time>01:00 น. - 03:59 น.</time>')
        elif match.group() == '<time>ช่วงเช้ามืด</time>' or match.group() == '<time>ตอนเช้ามืด</time>':
            print('เวลา : <time>03:00 น. - 05:59 น.</time>')
        else:
            print(str('เวลา : ') + match.group())
    return read_text


def person_tag(text):
    return


def check_location_wrong_fail():
    return

def phare_data_to_dict():
    data = {
        
    }
if __name__ == '__main__':
    # connect to database on mongodb atlas cloud
    database = "mongodb+srv://student:m789789123@cluster0-ds9da.mongodb.net/test?retryWrites=true"
    client = MongoClient(database, connectTimeout=200)
    # check status to connect
    print(client.status)
    # show list data base
    print(client.list_database_names())
    # use database client
    datanews = client.datanews
    print(datanews.list_collection_names())


    # URL = input("Enter URL:")
    # print(get_news(URL))
