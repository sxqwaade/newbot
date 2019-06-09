# -*- coding: utf-8 -*-
import uuid
class NikeAccount:
    def __init__(self,username,password,host,access_token):
        self.username = username
        self.password = password
        self.checkoutId = str(uuid.uuid4())
        self.paymentsId = str(uuid.uuid4())
        self.shippingId = str(uuid.uuid4())
        self.host = host
        self.recipientInfo = {"lastName": '达 ', "firstName": '刘'}
        self.addressInfo = {"state": 'CN-44', "city": '深圳市', "address1": '西乡街道永丰社区六区87号903', "postalCode": "518000","address2": "", "county": "宝安区", "country": "CN"}
        self.access_token = access_token
        self.contactInfo = {"phoneNumber": '18538092159', "email": '549705907@qq.com'}
        self.launchRecipient = {"lastName": '达', "firstName": '刘', "email": '549705907@qq.com',"phoneNumber": '18538092159'}
        self.launchAddress = {"state": 'CN-44', "city": '深圳市', "address1": '西乡街道永丰社区六区87号903', "county": "宝安区", "country": "CN"}
    def setOrderId(self,id):
        self.OrderId = id