### 큐 1

## 함수

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
# enQueue() 삽입
rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'
print('출구<--', queue, '<--입구')
# deQueue() 추출
front += 1
data = queue[front]
queue[front] = None
print('손님 이쪽으로 : ', data)
front += 1
data = queue[front]
queue[front] = None
print('손님 이쪽으로 : ', data)
front += 1
data = queue[front]
queue[front] = None
print('손님 이쪽으로 : ', data)


print('출구<--', queue, '<--입구')


### 큐 2

## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ( rear >= SIZE-1 ) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if ( isQueueFull() ) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data


## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

enQueue('재남')
print('출구<--', queue, '<--입구')


### 큐 3

## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ( rear >= SIZE-1 ) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if ( isQueueFull() ) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if ( front == rear ) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if ( isQueueEmpty() ) :
        print('큐 텅~')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
enQueue('화사')
enQueue('솔라')
# enQueue('문별')
# enQueue('휘인')
# enQueue('선미')
# print('출구<--', queue, '<--입구')
#
# enQueue('재남')
print('출구<--', queue, '<--입구')

retData = deQueue()
print('*식사 손님 :', retData)

retData = deQueue()
print('*식사 손님 :', retData)

retData = deQueue()
print('*식사 손님 :', retData)

print('출구<--', queue, '<--입구')


### 큐 (기본버전)

## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ( rear >= SIZE-1 ) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if ( isQueueFull() ) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if ( front == rear ) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if ( isQueueEmpty() ) :
        print('큐 텅~')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if ( isQueueEmpty() ) :
        print('큐 텅~')
        return
    return queue[front+1]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
enQueue('화사')
enQueue('솔라')
# enQueue('문별')
# enQueue('휘인')
# enQueue('선미')
# print('출구<--', queue, '<--입구')
#
# enQueue('재남')
print('출구<--', queue, '<--입구')

retData = deQueue()
print('*식사 손님 :', retData)

print('## 준비하세요 :', peek())

retData = deQueue()
print('*식사 손님 :', retData)

retData = deQueue()
print('*식사 손님 :', retData)

print('출구<--', queue, '<--입구')