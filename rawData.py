import collections
import csv
import enum

line_counter = 0
header = []
orders_raw = []

firstTimeOfList = ""
lastTimeOfList = ""

def fileopen():
    global line_counter
    global header
    global orders_raw

    global firstTimeOfList
    global lastTimeOfList

    fileAddr = "UltraCalls.csv"
    #fileAddress = "C:\\Users\\DayDream\\Desktop\\HND\\UltraCalls.csv"

    # 파일 오픈
    with open(fileAddr, 'r') as f:
        data = csv.reader(f)
        for line in data:
            #data = f.readline()
            #print(data) # data에 파일을 한 줄씩 불러옴
            if not data: break 
            if line_counter == 0:
                #header = line.split(",") # 맨 첫 줄은 header로 저장
                header = line
                line_counter += 1
            else:
                #orders_raw.append(data.split(","))
                if line[4] == "울트라콜":
                    orders_raw.append(line)
                    line_counter += 1

    # 표본 모집 기간 산출
    firstTimeOfList = orders_raw[0][0]
    lastTimeOfList = orders_raw[-1][0]


def printOrders(self):
    print (header, "\n")
    for i in orders_raw:
        print(i)

"""
# data menu
class orderParse(enum.Enum):
    orderDate = 0 # 주문시각
    orderNum = 1 # 주문번호
    adType = 2 # 광고상품그룹, 울트라콜
    campID = 3 # 캠페인ID
    product = 4 # 주문내역
    price = 5 # 결제금액
    payType = 6 #결제타입
    deliveryType = 7 # 수령방법, 배달
"""

fileopen()