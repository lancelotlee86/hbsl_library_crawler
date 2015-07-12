import requests
from bs4 import BeautifulSoup
from pymongo import *
import time
from datetime import date, datetime
# from str2date import str2date

def str2date(date_str):
    d = time.strptime(date_str, '%Y/%m/%d')
    dd = datetime(*d[:3])
    return dd

con = Connection()
db = con['hbsl_library_crawler']

# 先用一个学生，以后想办法遍历所有学生
student_number = '201315414'
student_password = student_number

s = requests.session()

# 主页面
url_hbsl_home = "http://m.5read.com/967"
r1 = s.get(url_hbsl_home)

hbsl_home_JSESSIONID = r1.cookies['JSESSIONID']
maid = r1.cookies['maid']
mgid = r1.cookies['mgid']
mduxiu = r1.cookies['mduxiu']
msign_dsr = r1.cookies['msign_dsr']
xc = r1.cookies['xc']

# 进入登陆页面，获取JSESSION
headers2 = {
    'Host': 'mc.m.5read.com',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
    'Referer': 'http://m.5read.com/967',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'JSESSIONID=J34J4I21LI56J6124F489BAECC78AE4C.irdmbl72b; mgid=' + mgid + '; maid=' + maid + '; msign_dsr=' + msign_dsr + '; mduxiu=' + mduxiu + '; xc='+ xc
}# JESSIONID 好像是随机的都可以，试试以后做一个32位的随机字符串生成
r2 = s.get("http://mc.m.5read.com/user/login/showLogin.jspx", headers = headers2)
JSESSIONID = r2.cookies['JSESSIONID']

# 提交登陆表单
headers3 = {
    'Host': 'mc.m.5read.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://mc.m.5read.com/user/login/showLogin.jspx?backurl=%2Fuser%2Fuc%2FshowUserCenter.jspx',
    'Cookie': 'JSESSIONID=' + JSESSIONID + '; mgid=274; maid=967; msign_dsr='+ msign_dsr + '; mduxiu=' + mduxiu + '; xc=' + xc + '; Hm_lvt_d2fe4972d5c5737ef70e82fe0c8deaee=1433310649; Hm_lpvt_d2fe4972d5c5737ef70e82fe0c8deaee=1433311081',
    'Connection': 'keep-alive'
    }
# 这里面是post的参数
payload = {
    'schoolid': '967',
    'backurl': '',
    'userType': '0',
    'username': student_number,
    'password': student_password
    }
r3 = s.post("http://mc.m.5read.com/irdUser/login/opac/opacLogin.jspx", data = payload, headers = headers3, allow_redirects=False)
# 现在已经登陆进去，并且将用户与 JSESSIONID 绑定了
# 下面这3个信息应该是和登陆者个人相关的
mmr_enc = r3.cookies['mmr_enc']
mmr_uid = r3.cookies['mmr_uid']
mmr_userid = r3.cookies['mmr_userid']
#_3gemail = r3.cookies['_3gemail']

# 进入个人借阅信息页面
headers4 = {
    'Host': 'mc.m.5read.com',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36',
    'Referer': 'http://mc.m.5read.com/user/uc/showOpacinfo.jspx',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'JSESSIONID=' + JSESSIONID + '; mgid=274; maid=967; msign_dsr=' + msign_dsr + '; mduxiu=' + mduxiu + '; xc=' + xc + '; mmr_enc=' + mmr_enc + '; mmr_userid=' + mmr_userid + '; mmr_uid=' + mmr_uid + '; 3gemail=""; Hm_lvt_d2fe4972d5c5737ef70e82fe0c8deaee=1433310649; Hm_lpvt_d2fe4972d5c5737ef70e82fe0c8deaee=1433311427'
}
r4 = s.get("http://mc.m.5read.com/cmpt/opac/opacLink.jspx?stype=1", headers = headers4)

''' 登出header 不能用
headers5 = {    # logout header
    'Host': 'mc.m.5read.com',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
    'Referer': 'http://mc.m.5read.com/user/uc/showUserCenter.jspx',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'JSESSIONID=' + JSESSIONID + '; mgid=274; maid=967; msign_dsr='+ msign_dsr + '; mduxiu=' + mduxiu + '; xc=' + xc + '; mmr_enc=' + mmr_enc + '; mmr_uid=' + mmr_uid + '; mmr_userid=' + mmr_userid,
}
'''
# 登出，不知是否真的登出了
r5 = s.get('http://mc.m.5read.com/user/logout/logout.jspx')

# 以下是解析提取数据
result_page = r4.text.replace("\r", "").replace("\n", "").replace("\t", "")
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
    info[1] = str2date(info[1])
    info[2] = str2date(info[2])
    books.append(dict(zip(key, info)))

# 将获取的这个学生这一天的借阅信息放入mongodb
db.record.update(
    {'student_number': student_number},
    { '$addToSet': {
        'record': {
            'date': datetime.now(),   # 稍后换成date类型
            'books_count': books_count,
            'books': books
        }}
    }
)
s.close()
