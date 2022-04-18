#!/usr/bin/python
# -*- coding: utf-8 -*-
import twstock
import pandas
import datetime

number = input('輸入股票代碼: ')
latest_stock = twstock.realtime.get(number) #最新資訊
stock = twstock.Stock(number) #股票資訊
price = stock.price #各日收盤價
high = stock.high #各日最高價
date = stock.date #各日日期

print('是否為最新資訊:','是' if latest_stock['success']==True else '否')

#取得個別資訊
print('%-15s %-15s' %('日期','收盤價'))
for i in range(len(date)):
	t = date[i].strftime('%Y年%m月%d日')
	p = stock.price[i]
	print('%-15s %-15s' %(t,str(p)))

print('股票代碼', '地區', '股票名稱', '公司全名','現在時間', '最新成交價', '成交量', '累計成交量', '最佳5檔賣出價', '最佳5檔賣出量', '最佳5檔買進價', '最佳5檔買進量', '開盤價', '最高價', '最低價')
for name in latest_stock['info']:
	print(latest_stock['info'][name], end=' ')