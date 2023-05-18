### 선택 정렬 1

## 함수
import random
def  findMinIndex(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if ( ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

## 변수
before = [ random.randint(33, 190) for _ in range(8)]
after = []
## 메인
print('정렬 전-->', before)
for _ in range(len(before)) :
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del (before[minPos])


print('정렬 후-->', after)


### 선택 정렬 2

## 함수
import random
def selectSort(ary) :
    n = len(ary) # 배열 개수
    for i in range(0, n-1, 1) : # Cycle
        minIdx = i
        for k in range(i+1, n, 1) :
            if (ary[minIdx]> ary[k]) :
                minIdx = k
        ary[i], ary[minIdx] = ary[minIdx], ary[i] # 교환
    return ary

## 변수
dataAry = [ random.randint(33, 190) for _ in range(40)]

## 메인
print('정렬전 -->', dataAry)
dataAry = selectSort(dataAry)
print('정렬후-->', dataAry)