### 선형 리스트 1

## 함수 선언부

## 전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
print(katok)

# 데이터 추가 : 모모가 카톡 1회
katok.append(None)  # 빈칸 추가
katok[5] = '모모'
print(katok)


### 선형 리스트 2

## 함수 선언부

## 전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드부
print(katok)

## 데이터 추가 : 모모가 카톡 1회
katok.append(None)  # 빈칸 추가
katok[5] = '모모'
print(katok)

## 데이터 삽입 : 미나가 카톡을 연속 40회(3등)
# 1단계 : 빈칸 추가
katok.append(None)
# 2단계 : 3등 위치까지 한칸씩 뒤로 이동
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
# 3단계 : 3등칸에 새 친구 입력
katok[3] = '미나'
print(katok)

## 데이터 삭제 : 사나가 카톡을 차단 (4등 위치 제거)
# 1단계 : 사나 지우기 (4등 지우기)
katok[4] = None
# 2단계 : 4등 이후의 친구를 한칸씩 앞으로
katok[4] = katok[5]
katok[5] = None
katok[5] = katok[6]
katok[6] = None
# 3단계 : 빈 마지막 칸을 통째로 제거
del(katok[6])
print(katok)


### 선형 리스트 3

## 함수
def add_data(friend) : # 데이터 추가 함수
    # 1단계 : 빈 칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 빈 칸에 친구 넣기
    katok[kLen-1] = friend

def insert_data(position, friend) : # 데이터 삽입 함수
    # 1단계 : 빈 칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 마지막 칸부터 하나씩 뒤로 이동. 삽입할 위치까지
    for i in range( kLen-1, position, -1 ) : # 핵심(어려움)
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 비워진 칸에 새 친구 입력
    katok[position] = friend


## 변수
katok=[]

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나') # 위치, 친구
print(katok)


# 선형 리스트 4

## 함수
def add_data(friend) : # 데이터 추가 함수
    # 1단계 : 빈 칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 빈 칸에 친구 넣기
    katok[kLen-1] = friend

def insert_data(position, friend) : # 데이터 삽입 함수
    # 1단계 : 빈 칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 마지막 칸부터 하나씩 뒤로 이동. 삽입할 위치까지
    for i in range( kLen-1, position, -1 ) : # 핵심(어려움)
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 비워진 칸에 새 친구 입력
    katok[position] = friend

def delete_data(position) : # 데이터 삭제 함수
    # 1단계 : 값 지우기
    katok[position] = None
    kLen = len(katok)
    # 2단계 : 지운 위치부터 마지막까지 한칸씩 당기기
    for i in range (position+1, kLen, 1) : # 핵심(어려움)
        katok[i-1] = katok[i]
        katok[i] = None
    # 3단계 : 마지막 칸 제거
    del (katok[kLen-1])

## 변수
katok=[]

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나') # 위치, 친구
print(katok)

delete_data(4) # 위치
print(katok)