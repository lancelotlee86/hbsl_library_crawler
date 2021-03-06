import requests
import pymongo
import time
from time import sleep

client = pymongo.MongoClient("localhost", 27017)
db = client.ncwu_library

for i in range(201400101, 201400110):   # 日后可以访问api，获取下一个
    print(i)
    student_number = i
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

    # 输出查询用的result_url
    print(r4.url)
    db.library_record.update(
        {'student_number' : str(student_number)},
        { '$set' :
              {'result_url' : r4.url }
        }
    )


    s.close()
    sleep(5)    # 等待5秒，防止被封ip
