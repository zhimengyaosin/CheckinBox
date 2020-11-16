# -*- coding: utf8 -*-
import requests, json, time, os

requests.packages.urllib3.disable_warnings()

cookie = os.environ.get("cookie_smzdm")

def smzdm_pc(*arg):
    try:
        msg = ""
        SCKEY = os.environ.get('SCKEY')
        s = requests.Session()
        s.headers.update({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'})
        t = round(int(time.time() * 1000))
        url = f'https://zhiyou.smzdm.com/user/checkin/jsonp_checkin?_={t}'

        headers = {
            "cookie" : cookie,
            'Referer': 'https://www.smzdm.com/'
            }

        r = s.get(url, headers=headers, verify=False)
        print(r.text)
        if r.json()["error_code"] != 0 and SCKEY:
            scurl = f"https://sc.ftqq.com/{SCKEY}.send"
            data = {
                    "text" : "smzdm  Cookie过期",
                    "desp" : r.text
                    }
            requests.post(scurl, data=data)
            print("smzdm cookie失效")
            msg += "smzdm cookie失效"
        else:
            msg += "smzdm签到成功"
    except Exception as e:
        print('repr(e):', repr(e))
        msg += '运行出错,repr(e):'+repr(e)
    return msg

if __name__ == "__main__":
    if cookie:
        print("----------什么值得买开始尝试签到----------")
        smzdm_pc()
        print("----------什么值得买签到执行完毕----------")

    
