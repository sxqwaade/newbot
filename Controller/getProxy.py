# _*_ coding:utf-8 _*_
import json
import requests
from Controller.tunnelHorocn import  *
MaxProxyCounts = 5
proxyAPI = "https://proxy.horocn.com/api/proxies?order_id=3ZKE1631228429969215&num="+str(MaxProxyCounts)+"&format=json&line_separator=win&can_repeat=yes"
ProxyCount = 0
ProxyList = []
proxyUrl = "http://api3.xiguadaili.com/ip/?tid=558658608095386&num=1&delay=1&filter=on"
wandou = "http://api.wandoudl.com/api/ip?app_key=d0194613527bdce17fa055829abd45fd&pack=0&num=1&xy=1&type=1&lb=\r\n&mr=2&"

def testProxy(host,isHttps = True):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    # url = 'https://www.nike.com/cn/zh_cn'
    url = 'https://www.baidu.com'
    # proxies是requests中的代理 choice是随机使用一个IP 这里http 和 https最好都写上
    if isHttps :
        proxy = {'http': host,'https':host}
    else:
        proxy = {'http': host}
    try:
        request = requests.get(url, proxies=proxy, headers=head,timeout=3)
    except Exception:
        print(host + ' ERROR!')
        return False
    print(host + ' OK!')
    return True

def getProxy():
    global ProxyCount
    global ProxyList
    if ProxyCount == 0:
        r = requests.get(proxyAPI).content
        json_str = json.loads(r)
        print(json_str)
        for h in json_str:
            try:
                host = 'http://'+h['host'] +':'+h['port']
            except Exception:
                continue
            if testProxy(host):
                ProxyList.append(host)
                ProxyCount += 1
            else:
                continue
        if ProxyCount == 0:
            return getProxy()
    print(ProxyList)
    ProxyCount -= 1
    return ProxyList[ProxyCount]

def getSingleProxy():
    host = getTunnelHost()
    if not testProxy(host=host,isHttps=False):
        return getSingleProxy()
    else:
        return {'http': host}

def getWandou():
    host = requests.get(wandou).content
    if not testProxy(host):
        print ("Fail:"+host)
        return getWandou()
    else:
        return host