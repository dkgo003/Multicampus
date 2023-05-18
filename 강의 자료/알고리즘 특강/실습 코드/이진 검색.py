### 이진 검색

## 함수
import random
def binSearch(ary, fData) :
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end) :
        mid = (end + start) // 2
        if ( ary[mid] == fData) :
            pos = mid
            break
        elif ( ary[mid] < fData) :
            start = mid + 1
        else :
            end = mid - 1
    return pos

## 변수
dataAry = [ random.randint(33, 190) for _ in range(10)]
findData = random.choice(dataAry) # 할머니 키
dataAry.sort()

## 메인
print('배열-->', dataAry)
position = binSearch(dataAry, findData)
if (position == -1) :
    print(findData, '없어요 ㅠ')
else :
    print(findData,'가', position, '위치에 있어요.')


### 이진 검색(성능)

## 함수
import random
def binSearch(ary, fData) :
    global count
    pos = -1
    start = 0
    end = len(ary)-1
    while (start <= end) :
        count += 1
        mid = (end + start) // 2
        if ( ary[mid] == fData) :
            pos = mid
            break
        elif ( ary[mid] < fData) :
            start = mid + 1
        else :
            end = mid - 1
    return pos

## 변수
dataAry = [ random.randint(1,10000000000) for _ in range(10000000)]
findData = random.choice(dataAry) # 할머니 키
dataAry.sort()
count = 0

## 메인
print('배열-->', dataAry[:20])
position = binSearch(dataAry, findData)
if (position == -1) :
    print(findData, '없어요 ㅠ')
else :
    print(findData,'가', position, '위치에 있어요.(', count, '번)')
