### 최솟값 찾기

## 함수
import random
def  findMinIndex(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if ( ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx

## 메인
#testAry = [55, 88, 33, 77]
testAry = [ random.randint(33, 190) for _ in range(8)]

## 전역
print(testAry)
minPos = findMinIndex(testAry)
print('최솟값-->', testAry[minPos])