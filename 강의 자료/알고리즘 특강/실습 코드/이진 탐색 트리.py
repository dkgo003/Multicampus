### 이진 탐색 트리 1

## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스'] # 여러분 데이터

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] : # ['레드벨벳', '마마무', ...
    node = TreeNode()
    node.data = name

    current = root
    while True :
        if ( name < current.data  ) :
            if ( current.left == None) :
                current.left = node
                break
            else :
                current = current.left
        else :
            if ( current.right == None) :
                current.right = node
                break
            else :
                current = current.right

    memory.append(node)

print('이진 탐색 트리 구성 완료!')


### 이진 탐색 트리 2

## 함수
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스'] # 여러분 데이터

## 메인
node=TreeNode()
node.data = nameAry[0]
root = node
memory.append(node) # 안 중요. 없어도됨.

for name in nameAry[1:] : # ['레드벨벳', '마마무', ....
    node = TreeNode()
    node.data  = name

    current = root
    while True :
        if ( name < current.data ) :
            if ( current.left == None) :
                current.left = node
                break
            current = current.left
        else :
            if ( current.right == None) :
                current.right = node
                break
            current = current.right

    memory.append(node)  # 안 중요. 없어도됨.

print('이진 탐색 트리~ 구성 완료!')

#findName = '마마무'
findName = '바바부'
current = root

while True :
    if ( findName == current.data ) :
        print(findName, '찾았음~~ ㅎㅎ')
        break
    elif ( findName < current.data ) :
        if (current.left != None) :
            current = current.left
        else :
            print(findName, '없어요 ㅠㅠ')
            break
    else :
        if (current.right != None) :
            current = current.right
        else :
            print(findName, '없어요 ㅠㅠ')
            break


### 이진 탐색 트리 (성능확인)

## 함수
import random
class TreeNode() :
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수
memory = []
root = None
#nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스'] # 여러분 데이터
nameAry = [random.randint(0,1000000000000000) for _ in range(1000000)]

## 메인
node=TreeNode()
node.data = nameAry[0]
root = node
memory.append(node) # 안 중요. 없어도됨.

for name in nameAry[1:] : # ['레드벨벳', '마마무', ....
    node = TreeNode()
    node.data  = name

    current = root
    while True :
        if ( name < current.data ) :
            if ( current.left == None) :
                current.left = node
                break
            current = current.left
        else :
            if ( current.right == None) :
                current.right = node
                break
            current = current.right

    memory.append(node)  # 안 중요. 없어도됨.

print('이진 탐색 트리~ 구성 완료!')

#findName = '마마무'
findName = random.choice(nameAry)
current = root
count = 0

while True :
    count += 1
    if ( findName == current.data ) :
        print(findName, '찾았음~~ ㅎㅎ')
        break
    elif ( findName < current.data ) :
        if (current.left != None) :
            current = current.left
        else :
            print(findName, '없어요 ㅠㅠ')
            break
    else :
        if (current.right != None) :
            current = current.right
        else :
            print(findName, '없어요 ㅠㅠ')
            break

print(count, '번만에 찾음')

