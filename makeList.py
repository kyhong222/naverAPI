import rawData

addrDetailList = []

def make_list():
    global addrDetailList
    data = rawData.orders_raw
    existFlg = 0

    for i in data:
        addr = i[-1]
        # 주소가 비어있다면 생략
        if addr == "":
            continue

        else:
            addr = addr.split(' ')[0] + " " + addr.split(' ')[1]
            allAddrDetailCount += 1

            # 이미 존재하는 주소인지 검색
            for j in addrDetailList:
                if (addr == j[0]): # 이미 존재하는 주소일경우
                    j[1] += 1
                    existFlg = 1
                    break
            
            # 새로운 주소인 경우
            if existFlg==0:
                addrDetailList.append([addr, 1])

            # 이미 존재하는 주소인 경우, 플래그 초기화
            else:
                existFlg = 0

    addrDetailList.sort(key=lambda x:x[0])