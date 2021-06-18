import requests, json, time, os, re, sys
sys.path.append('.')
requests.packages.urllib3.disable_warnings()
try:
    from pusher import pusher
except:
    pass

cookie = os.environ.get("cookie_zhiyou")

def run(*args):
    msg = ""
    s = requests.Session()
    s.headers.update(
        {
            'Connection' : 'keep-alive',
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Host' : 'bbs.zhiyoo.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'Origin' : 'http://bbs.zhiyoo.net',
            'Referer' : 'http://bbs.zhiyoo.net/plugin.php?id=dsu_paulsign:sign',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language' : 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept-Encoding' : 'gzip, deflate',
            'Cookie': cookie

        }
        )
    response = s.get(url="http://bbs.zhiyoo.net/plugin.php?id=dsu_paulsign:sign", verify=False)
    formhash = re.findall(r'<input type="hidden" name="formhash" value="(.*?)"', response.text)[0]
    # 签到
    url = "http://bbs.zhiyoo.net/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1"
    payload=f'formhash={formhash}&qdxq=yl'
    r = s.post(url, data=payload, verify=False, timeout=120)
    # print(r.text)
    if '成功' in r.text:
        msg += re.compile(r'恭喜你签到成功!获得随机奖励 金币 \d+ 元.').search(r.text)[0]
    elif '已经签到' in r.text:
        msg += '您今日已经签到，请明天再来！'
    else:
        msg += '签到失败，可能是cookie失效了！'
        pusher("智友邦  签到失败，可能是cookie失效了！！！", r.text[:200])
    return msg + '\n'

def main(*args):
    msg = ""
    global cookie
    if "\\n" in cookie:
        clist = cookie.split("\\n")
    else:
        clist = cookie.split("\n")
    i = 0
    while i < len(clist):
        msg += f"第 {i+1} 个账号开始执行任务\n"
        cookie = clist[i]
        msg += run(cookie)
        i += 1
    print(msg[:-1])
    return msg[:-1]


if __name__ == "__main__":
    if cookie:
        print("----------智友邦开始尝试签到----------")
        main()
        print("----------智友邦签到执行完毕----------")
