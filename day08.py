'''
list
- 하나의 자료형으로 여러개의 값을 저장할 수 있다
- [](대괄호) 표현되면 리스트로 생각하면 어느정도 맞다
- 각 각의 값에 접근하고자 할 경우 index를 이용한다.
- index는 0부터 시작한다
'''
print('aaa'+str(100))

ls = [500,200,300,400]
print( ls )
print( ls[0] )
print( ls[3] )

ls = [0,0,0]
ls[0] = int(input('값 입력 : '))
ls[1] = int(input('값 입력 : '))
ls[2] = int(input('값 입력 : '))
sum_ = ls[0] + ls[1] + ls[2]
print(ls)
print(sum_)

ls = [0,0,0]
sum_ = 0
print( 'len : ',len(ls) ) # 값의 갯수

for i in range( len(ls) ):
    ls[i] = int(input(str(i)+'값 입력 : ')) # f'{i} 값 입력 : ' 문자로 처리 해 줘야 연산 가능
    sum_ += ls[i]
print( ls )
print('합 : ',sum_)

ls = [10,20,30,40] #범위 지정 가
print('ls : ',ls)
print( ls[1:3] )  # 1번째 부터 3번째 전까지(2번까지)
print( ls[:2] ) # 제일 처음부터 2번째 전까지(1번까지)
print( ls[1:] ) # 1번째부터 끝까지
print( ls[:] ) # 처음부터 끝까지

import copy  #copy를 이용해서도 깊은 복사 사용 가능

import day01 #import : 다른 페이지의 값을 현재 페이지로 가져와서 실행 하는것


n = 100
print( n )
print( id(n) )
print('-'*20)

ls = [10,20,30]
#arr = ls
#arr = ls[:]     # 각각의 공간을 서로 가지려면 이렇게 저장해야함 ( 깊은 복사)
#arr = copy.deepcopy(ls) #copy를 사용한 깊은 복사
arr = ls.copy() #copy를 사용한 깊은 복사
print( id(ls) ) #같은 공간을 참조함 ( 얕은 복사 )
print( id(arr) )
ls[1] = 12345 # 누구로 변경해도 같이 변경됨
print(ls)  
print(arr)
print('-'*20)


ls = [10,20,30]
arr =[40,50,60]
print(ls)
print(arr)
str_ = ls + arr
print( str_ )
str_ = ls * 3
print( str_ )
print('-'*20)


'''
+ : 50 70 90
*3 : 30 60 90
'''

sum_ = [0,0,0]
mul = [0,0,0]
for i in range(len(ls)):
    sum_[i] = ls[i]+arr[i]
    mul[i] = ls[i] *3
print( sum_ )
print( mul)
print('-'*20)


a = 10; b = 20;
print(a,b)
a, b = b, a
print (a,b)
print('-'*20)


ls = [4,8,2,7,6]
for i in range(4):
    for j in range( i+1, 5):
        if ls[i] > ls[j]:
            ls[i], ls[j] = ls[j], ls[i]
print(ls)
print('-'*20)


score = [82,85,76,79,96]
rank = [1,1,1,1,1]
for i in range(5):
    for j in range(5):
        if score[i] < score[j]:
            rank[i] = rank[i] + 1
print(score,rank)

for i in range( len(rank) ):
    print(score[i],rank[i])
