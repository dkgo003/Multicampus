### 순차 검색

## 함수
import random
def  seqSearch(ary, fData) :
    pos = -1
    for i in range(len(ary)) :
        if ( ary[i] == fData ) :
            pos = i
            break
    return pos

## 전역
dataAry = [ random.randint(33, 190) for _ in range(8)]
findData = random.choice(dataAry) # 누나 키

## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)
if (position == -1) :
    print(findData, '없어요 ㅠㅠ')
else :
    print(findData,'는', position, '번째 있어요. ^^')


### 순차 검색 (정렬)

## 함수
import random
def  seqSearch(ary, fData) :
    pos = -1
    for i in range(len(ary)) :
        if ( ary[i] == fData ) :
            pos = i
            break
        elif ( ary[i] > fData) :
            break
    return pos

## 전역
dataAry = [ random.randint(33, 190) for _ in range(8)]
findData = random.choice(dataAry) # 누나 키
dataAry.sort()
findData= 40

## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)
if (position == -1) :
    print(findData, '없어요 ㅠㅠ')
else :
    print(findData,'는', position, '번째 있어요. ^^')

