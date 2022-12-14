# 오류 해결 과정 중심!! 

import csv

def show_profit(data):
    name = data[0] # 종목
    purchase_price = int(data[1]) # 매입가
    amount = int(data[2]) # 수량 
    target_price = int(data[3]) # 목표가 

    profit = (target_price - purchase_price) * amount # 수익금 
    profit_ratio = round((target_price/purchase_price - 1) * 100 , 2) # 수익률

    print(f"{name} {profit} {profit_ratio}%")

# 파일 열기

file = open("Python_web_development\Fastcampus_python_master\Part_001\Chapter_010\mystock.csv","r",encoding='UTF-8')

# 파일 데이터 읽기

reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)
file.close()