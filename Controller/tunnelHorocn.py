# 代理服务器
proxyHost = "dyn.horocn.com"
proxyPort = "50000"

# 代理隧道验证信息
proxyUser = "RCQE1631244181475683"
proxyPass = "YUHlEave4wDyclPr"


def getTunnelHost():
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }
    return proxyMeta

