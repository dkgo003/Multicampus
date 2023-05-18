### 스택 (괄호검사) 1

## 함수
def isStackFull() :
    global SIZE, stack, top
    if ( top >= SIZE-1 ) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if ( isStackFull() ) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def  isStackEmpty() :
    global SIZE, stack, top
    if ( top <= -1 ) :
        return  True
    else :
        return False

def pop() :
    global SIZE, stack, top
    if ( isStackEmpty() ) :
        print('스택 텅~')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if ( isStackEmpty() ) :
        print('스택 텅~')
        return
    return stack[top]

## 변수
SIZE = 500
stack = [None for _ in range(SIZE)]
top = -1

## 메인
expr = '(A+B)-(C*D))'

for ch in expr :
    if (ch == '(') :
        push(ch)
    elif (ch == ')') :
        out = pop()
        if (out == None) :
            print('오류~~')
            exit()
    else :
        pass

if (isStackEmpty()) :
    print('정상!')
else :
    print('오류~~')

## 퀴즈 : ( < { 도 체크하기...
## '(<A+{B-C}/<D*F>>)'


### 스택 (괄호검사) 2

## 함수
def isStackFull() :
    global SIZE, stack, top
    if ( top >= SIZE-1 ) :
        return True
    else :
        return False

def push(data) :
    global SIZE, stack, top
    if ( isStackFull() ) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def  isStackEmpty() :
    global SIZE, stack, top
    if ( top <= -1 ) :
        return  True
    else :
        return False

def pop() :
    global SIZE, stack, top
    if ( isStackEmpty() ) :
        print('스택 텅~')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if ( isStackEmpty() ) :
        print('스택 텅~')
        return
    return stack[top]

## 변수
SIZE = 500
stack = [None for _ in range(SIZE)]
top = -1

## 메인
expr = '(A+B)-(C*D)()()()((()))'
expr = '(<A+(B-C)/<D*F>>)'

for ch in expr :
    if (ch == '(' or ch == '<') :
        push(ch)
    elif (ch == ')' or ch == '>') :
        out = pop()
        if (out == None) :
            print('오류2~~')
            exit()
        if (ch == ')' and out== '(' ) :
            pass
        elif (ch == '>' and out== '<' ) :
            pass
        else :
            print('오류3~~')
            exit()
    else :
        pass

if (isStackEmpty()) :
    print('정상!')
else :
    print('오류~~')

## 퀴즈 : ( <  도 체크하기...
## '(<A+(B-C)/<D*F>>)'