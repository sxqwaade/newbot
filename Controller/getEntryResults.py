# -*- coding: UTF-8 -*- #
import requests
from concurrent.futures import ThreadPoolExecutor
from Model.MySqlDao import *


def getEntryRes(tup):
    token, nkOid, id = tup
    headers = {"authorization": "Bearer " + token}
    try:
        response = requests.get("https://api.nike.com/launch/entries/v2/" + nkOid, headers=headers).json()
    except:
        # ban ip
        return [id,False]
    try:
        if response["waitingReason"] == "OUT_OF_STOCK":
            return [id,'fail']
    except Exception:
        # Something Error
        pass
    try:
        result = response["result"]
    except:
        return [id,'waiting']
    if result["status"] == "WINNER":
        return [id,'success']
    elif result["status"] == "NON_WINNER":
        return [id,'fail']

def getEntryResults1(limit = ''):
    orders = MySqlDao()
    if limit != '':
        list = orders.rows("SELECT * FROM `nikeorder` where results is null limit "+limit)
    else:
        list = orders.rows("SELECT * FROM `nikeorder` where results is null limit ")
    while 1:
        if len(list) == 0:
            break
        for re in list:
            if (re[2]):
                headers = {"authorization": "Bearer " + re[2]}
                try:
                    response = requests.get("https://api.nike.com/launch/entries/v2/" + re[1], headers=headers).json()
                except:
                    print ("ban ip")
                try:
                    if response["waitingReason"]=="OUT_OF_STOCK":
                        print ("NonWinner")
                        orders.exec("UPDATE `nikeorder` SET `results`='fail' WHERE orderid = '"+re[1]+"'")
                    print (response["waitingReason"])
                except Exception:
                    print (response)
                try:
                    result = response["result"]

                except:
                    continue
                if result["status"] == "WINNER":
                    print ("[nkBot]Draw Enrty username:"+re[5])
                    orders.exec("UPDATE `nikeorder` SET `results`='success' WHERE orderid = '"+re[1]+"'")
                elif result["status"] == "NON_WINNER":
                    print ("NonWinner")
                    orders.exec("UPDATE `nikeorder` SET `results`='fail' WHERE orderid = '"+re[1]+"'")


orders = MySqlDao()

def getEntryResults():
    orderList = orders.rows("SELECT * FROM `nikeorder` where results is null ")
    entryLoop(orderList)

def updateOrders(ids,result):
    id = ",".join(ids)
    orders.exec("UPDATE `nikeorder` SET `results`='" +result+ "' WHERE id in (" + id + ")")

def entryLoop(orderList):
    if len(orderList) == 0:
        return 0
    if len(orderList) == 0:
        return 0
    data = []
    for li in orderList:
        if (li[2]):
            data.append((li[2],li[1],li[0]))
    if len(data):
        pool = ThreadPoolExecutor()
        res = list(pool.map(getEntryRes, data))
        success = []
        fail = []
        orderList = []
        try:
            for re in res:
                if re[1] == 'success':
                    success.append(re[0])
                if re[1] == 'fail':
                    fail.append(re[0])
                if re[1] == 'waiting':
                    orderList.append(success)
        except:
            return 0
        updateOrders(success,'success')
        updateOrders(fail,'fail')
        entryLoop(orderList)

