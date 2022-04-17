#!/usr/bin/python
# -*- coding: utf-8 -*-
import twstock as t
import pandas as p

number = input('輸入股票代碼: ')
stock = t.realtime.get(number)

print(stock['success'])
print(stock['info'])
print('股票代碼', '地區', '股票名稱', '公司全名','現在時間', '最新成交價', '成交量', '累計成交量', '最佳5檔賣出價', '最佳5檔賣出量', '最佳5檔買進價', '最佳5檔買進量', '開盤價', '最高價', '最低價')
for name in stock['info']:
	print(stock['info'][name], end=' ')