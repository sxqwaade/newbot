# -*- coding: UTF-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor
from Controller.getProxy import *
from Model.MySqlDao import *
from Model import httpRequest
from Tools.Logger import Logger

TimeOut = 5

def accessToken(tup):
    id, token, client_id, isHost = tup
    url = 'https://api.nike.com/idn/shim/oauth/2.0/token'
    data = {
        # 'client_id':'HlHa2Cje3ctlaOqnxvgZXNaAs7T9nAuH',
        'client_id':client_id,
        'grant_type':'refresh_token',
        'ux_id':'com.nike.commerce.snkrs.ios',
        'refresh_token':token
    }
    try:
        if isHost:
            a = httpRequest.Post(url=url,data=data,proxy=True,timeout=TimeOut)
            # a = requests.post('https://api.nike.com/idn/shim/oauth/2.0/token',json=data,verify=False,proxies=proxies, timeout=TimeOut)
        else:
            a = requests.post('https://api.nike.com/idn/shim/oauth/2.0/token',json=data,verify=False, timeout=TimeOut)
    except Exception:
        return "[nkBot]"+str(id)+">代理连接失败!"
    try:
        access_token = a.json()['access_token']
    except Exception:
        account = MySqlDao()
        account.exec("UPDATE `nikeaccount` SET `token`= 'fail',`accessTime`='"+ str(time.time())+"' WHERE id = "+str(id))
        return "[nkBot]"+str(id)+">Update Access Token Fail:"+str(a.json())
    account = MySqlDao()
    account.exec("UPDATE `nikeaccount` SET `token`= '"+access_token+"',`accessTime`='"+ str(time.time())+"' WHERE id = "+str(id))
    return "[nkBot]"+str(id)+">Update Access Token Success!"

def mulAcToken(isHost,limit=''):
    print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))
    logger = Logger('AccessToken')
    account = MySqlDao()
    # res = account.rows("select * from nikeaccount where id >50 and id <= 100")
    if limit != '':
        res = account.rows("select * from nikeaccount limit "+limit)
    else:
        res = account.rows("select * from nikeaccount")
    print("[nkBot]>get " + str(len(res)) + " accounts Access Token")
    data = []
    for re in res:
        if re[4] and re[8]:
            data.append((re[0],re[4],re[8],isHost))
    if len(data):
        pool = ThreadPoolExecutor()
        res = list(pool.map(accessToken, data))
        logger.write(res)
    else:
        pass