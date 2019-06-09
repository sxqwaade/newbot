import urllib.request
import urllib.parse
import socket
import json

def Get(url, data={}, headers={}, timeout=5, proxy=False):
    socket.setdefaulttimeout(timeout)
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url = url,data = data,headers = headers, method = 'GET')
    if proxy:
        opener = GetProxyOpener()
        urllib.request.install_opener(opener)
    result = urllib.request.urlopen(req)
    html = result.read().decode('utf-8')
    return Response(html)

def Post(url, data={}, headers={}, timeout=5, proxy=False):
    socket.setdefaulttimeout(timeout)
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url = url,data = data,headers = headers,method = 'POST')
    if proxy:
        opener = GetProxyOpener()
        urllib.request.install_opener(opener)
    result = urllib.request.urlopen(req)
    html = result.read().decode('utf-8')
    return Response(html)

class Response():
    text = ''
    def __init__(self, html): # real signature unknown
        self.text = html
    def json(self):
        return json.loads(self.text.replace("'","\""))


def GetProxyOpener():
    # 代理服务器
    proxyHost = "dyn.horocn.com"
    proxyPort = "50000"

    # 代理隧道验证信息
    proxyUser = "4XI31631256276396130"
    proxyPass = "YUHlEave4wDyclPr"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxy_handler = urllib.request.ProxyHandler({
        "http": proxyMeta,
        "https": proxyMeta,
    })
    return urllib.request.build_opener(proxy_handler)
