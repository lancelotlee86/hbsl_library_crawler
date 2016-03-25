import requests
from bs4 import BeautifulSoup
import pymongo
import time
from datetime import date, datetime
from time import sleep
# from str2date import str2date

def str2date(date_str):
    d = time.strptime(date_str, '%Y/%m/%d')
    dd = datetime(*d[:3])
    return dd

client = pymongo.MongoClient("localhost", 27017)
db = client.ncwu_library

# 从数据库中遍历所有的学生的result_url，访问，解析数据，更新数据库

for i in range(201400101, 201400110):
    print(i)
    student_number = i

    # 找出该学生的result URL
    result = db.library_record.find_one( { 'student_number' : str(student_number) })
    result_url = result['result_url']

    # 直接访问该URL得到该学生借阅的图书信息
    s = requests.session()
    result_page = s.get(result_url)
    result_page = result_page.text.replace("\r", "").replace("\n", "").replace("\t", "")
    soup = BeautifulSoup(result_page)
    books_soup = soup.select('.sheet')   # a list, 每个class为sheet的div都是一本书
    books_count = len(books_soup)

    books = []  # 保存借阅的书籍信息，列表，每一个元素都是一个包含一本书信息的字典
    key = ['title', 'lend_date', 'return_deadline', 'renew_times', 'located']
    for book_soup in books_soup:
        items = book_soup.find_all('td')
        info = []
        for item in items:
            info.append(item.text.replace('\xa0', ''))
        info[0] = info[0][2:]   # 去掉标题的前缀
        info[1] = str2date(info[1])     # 转换时间格式
        info[2] = str2date(info[2])     # 转换时间格式
        books.append(dict(zip(key, info)))

    # 将获取的这个学生这一天的借阅信息放入mongodb
    db.library_record.update(
        {'student_number': str(student_number)},
        { '$addToSet':
            {
                'record': {
                    'date': datetime.now(),
                    'books_count': books_count,
                    'books': books
                }
            }
        },
        True
    )

    s.close()
    sleep(5)    # 等待5秒，防止被封ip
