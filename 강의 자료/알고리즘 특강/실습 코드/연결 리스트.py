### 연결 리스트 1

## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

## 변수


## 메인
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5



print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
print(node1.link.link.link.link.data, end=' ')


### 연결 리스트 2

## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

## 변수

## 메인
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# newNode = Node()
# newNode.data = '재남'
# newNode.link = node2.link
# node2.link = newNode

node2.link = node3.link
del(node3)


print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')
# print(node1.link.link.link.link.link.data, end=' ')


### 연결 리스트 3

## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

## 변수
memory = []
head, pre, current = None, None, None
dataAry = ['다현', '정연', '쯔위', '사나', '지효']  # 실무에서는 내맘대로 데이터 사용.

## 메인
node = Node()
node.data = dataAry[0]
head = node
memory.append(node) # 안 중요 (빼도 됨)

for data in dataAry[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)  # 안 중요 (빼도 됨)

printNodes(head)


### 연결 리스트 4

## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, pre, current
    # Case1 : 머리 앞에 삽입하는 경우(다현, 화사)
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)  # 안 중요 (빼도 됨)
        return
    # Case2 : 중간 노드 앞에 삽입하는 경우(사나, 솔라)
    current = head
    while(current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)  # 안 중요 (빼도 됨)
            return
    # Case3 : 없는 노드 앞에 삽입하는 경우(재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)  # 안 중요 (빼도 됨)
    return



## 변수
memory = []
head, pre, current = None, None, None
dataAry = ['다현', '정연', '쯔위', '사나', '지효']  # 실무에서는 내맘대로 데이터 사용.

## 메인
node = Node()
node.data = dataAry[0]
head = node
memory.append(node) # 안 중요 (빼도 됨)

for data in dataAry[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)  # 안 중요 (빼도 됨)

printNodes(head)

## 데이터 삽입
# insertNode('다현', '화사') # 찾을데이터, 삽입할데이터
# printNodes(head)

# insertNode('사나', '솔라') # 찾을데이터, 삽입할데이터
# printNodes(head)

insertNode('재남', '문별') # 찾을데이터, 삽입할데이터
printNodes(head)


### 연결 리스트 5

## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, pre, current
    # Case1 : 머리 앞에 삽입하는 경우(다현, 화사)
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)  # 안 중요 (빼도 됨)
        return
    # Case2 : 중간 노드 앞에 삽입하는 경우(사나, 솔라)
    current = head
    while(current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)  # 안 중요 (빼도 됨)
            return
    # Case3 : 없는 노드 앞에 삽입하는 경우(재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)  # 안 중요 (빼도 됨)
    return

def deleteNode(deleteData) :
    global memory, head, pre, current
    # Case1 : 머리를 삭제할 경우 (다현)
    if (deleteData == head.data) :
        current = head
        head = head.link
        del(current)
        return
    # Case2 : 중간을 삭제할 경우 (쯔위)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == deleteData) :
            pre.link = current.link
            del(current)
            return
    # Case3 : 없는 노드를 삭제할 경우(재남)
    return


## 변수
memory = []
head, pre, current = None, None, None
dataAry = ['다현', '정연', '쯔위', '사나', '지효']  # 실무에서는 내맘대로 데이터 사용.

## 메인
node = Node()
node.data = dataAry[0]
head = node
memory.append(node) # 안 중요 (빼도 됨)

for data in dataAry[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)  # 안 중요 (빼도 됨)

printNodes(head)

## 데이터 삽입
# insertNode('다현', '화사') # 찾을데이터, 삽입할데이터
# printNodes(head)

# insertNode('사나', '솔라') # 찾을데이터, 삽입할데이터
# printNodes(head)

# insertNode('재남', '문별') # 찾을데이터, 삽입할데이터
# printNodes(head)

# deleteNode('다현') # 삭제할 데이터
# printNodes(head)

deleteNode('쯔위') # 삭제할 데이터
printNodes(head)

deleteNode('재남') # 삭제할 데이터
printNodes(head)


### 연결 리스트 6

## 함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, pre, current
    # Case1 : 머리 앞에 삽입하는 경우(다현, 화사)
    if (findData == head.data) :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)  # 안 중요 (빼도 됨)
        return
    # Case2 : 중간 노드 앞에 삽입하는 경우(사나, 솔라)
    current = head
    while(current.link != None) :
        pre = current
        current = current.link
        if (current.data == findData) :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)  # 안 중요 (빼도 됨)
            return
    # Case3 : 없는 노드 앞에 삽입하는 경우(재남, 문별)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)  # 안 중요 (빼도 됨)
    return

def deleteNode(deleteData) :
    global memory, head, pre, current
    # Case1 : 머리를 삭제할 경우 (다현)
    if (deleteData == head.data) :
        current = head
        head = head.link
        del(current)
        return
    # Case2 : 중간을 삭제할 경우 (쯔위)
    current = head
    while (current.link != None) :
        pre = current
        current = current.link
        if (current.data == deleteData) :
            pre.link = current.link
            del(current)
            return
    # Case3 : 없는 노드를 삭제할 경우(재남)
    return

def findNode(findData) :
    global memory, head, pre, current
    # 찾는 데이터가 머리인 경우
    current = head
    if (current.data == findData) :
        return current
    while (current.link != None) :
        current = current.link
        if (current.data == findData) :
            return current
    return Node()

## 변수
memory = []
head, pre, current = None, None, None
dataAry = ['다현', '정연', '쯔위', '사나', '지효']  # 실무에서는 내맘대로 데이터 사용.

## 메인
node = Node()
node.data = dataAry[0]
head = node
memory.append(node) # 안 중요 (빼도 됨)

for data in dataAry[1:] : # ['정연', '쯔위', ...
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)  # 안 중요 (빼도 됨)

printNodes(head)

## 데이터 삽입
# insertNode('다현', '화사') # 찾을데이터, 삽입할데이터
# printNodes(head)

# insertNode('사나', '솔라') # 찾을데이터, 삽입할데이터
# printNodes(head)

# insertNode('재남', '문별') # 찾을데이터, 삽입할데이터
# printNodes(head)

# deleteNode('다현') # 삭제할 데이터
# printNodes(head)

# deleteNode('쯔위') # 삭제할 데이터
# printNodes(head)
#
# deleteNode('재남') # 삭제할 데이터
# printNodes(head)

retNode = findNode('사나')
print(retNode.data, '뮤비가 나옵니다. 쿵짝쿵짝~~')