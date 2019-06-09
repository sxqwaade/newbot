
from Controller.getAccessToken import *
from Controller.launchEntry import *
from Controller.getEntryResults import *
from Model.NikeItem import *
from Controller.registerAccount import registerFromTxtWithRefreshToken


# 更新token
def tk(limit = ''):
    mulAcToken(False,limit)
    return 0

# 参加抽签
def ent(limit):
    itemUrl = 'https://www.nike.com/cn/launch/t/ldwaffle-sacai-varsity-blue-varsity-red-del-sol/'
    sizeList = [8,8.5,9,10]
    isHost = False
    itemList = []
    for size in sizeList:
        itemList.append(NikeItem(itemUrl, size))
    mulLaunchEntry(itemList, isHost, limit)

# 查询结果
def check():
    print('开始查询')
    getEntryResults()


def reg():
    print('开始导入')
    registerFromTxtWithRefreshToken()

def back():
    getEntryResults1()

if __name__ == '__main__':
    tk()




