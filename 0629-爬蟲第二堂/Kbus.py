# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 13:46:45 2023

@author: s9571
"""

import requests
import io
import xml.sax

busID = list() #公車編號
busRoute = list() #路線
busStart = list() #起點站
busEnd = list() #終點站

class KBusHandler(xml.sax.ContentHandler):
    #tag是XML的標籤、attr是屬性
    def startElement(self, tag, attr):
        if tag == 'Route':
            busID.append(attr['ID'])
            busRoute.append(attr['nameZh'])
            busStart.append(attr['departureZh'])
            busEnd.append(attr['destinationZh'])
            
class KBusStop(xml.sax.ContentHandler):
    def startElement(self, tag, attr):
        if tag == "Stop":
            print('站牌:', attr["nameZh"])
            
if __name__ == '__main__':
    parser = xml.sax.make_parser()
    
    bus = KBusHandler()
    parser.setContentHandler(bus)
    url = "https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetRoute.xml"
    data = requests.get(url)
    data.encoding = "utf-8"
    data = data.text #將data變成文字
    busObj = io.StringIO(data)
    parser.parse(busObj)
    
    print('高雄市公車編號:',busID)
    bID = input('請輸入欲查詢的編號:')
    if busID.count(bID) > 0:
        index = busID.index(bID)
        #print(busID[index])
        print('路線名稱:', busRoute[index])
        print('起始站:', busStart[index])
        print('終點站:', busEnd[index])
    
    
    
    routeurl = 'https://ibus.tbkc.gov.tw/xmlbus/StaticData/GetStop.xml' #網址最後面?之後的參數都刪除掉
    param = dict()
    param['routeIDs'] = bID
    result = requests.get(routeurl, params=param)
    result.enconding = 'utf-8'
    result = result.text
    
    Stop = KBusStop()
    parser.setContentHandler(Stop)
    
    #即時解析
    routeInfo = io.StringIO(result)
    parser.parse(routeInfo)
    
    '''
    作業1-1:顯示目前公車所在的站牌，去程及回程都要
    GoBack="1"是去程、"2"是回程
    1-2:顯示兩種行程有哪些站牌
    '''