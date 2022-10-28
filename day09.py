st = '''  

ls = []
for i in range(3):
    value = input(f'{i+1}.번째 입력 : ')
    ls.append(value)
print(ls)

for i in range( len(ls) ):
    print( ls[i] )
    
for i in ls: #ls = [11,22,33,44] 이런 방법도 있다
    print(i)

arr = ls

#ls = []
ls.clear()
print( arr )    
'''
#''는 문장 한줄만 넣을 수 있고 '''는 엔터까지 포함해서 여러줄을 넣을 수 있음

#print(st)

ls = [30,20,5,10]
print( type(ls) )
print('기본값 : ',ls)

ls.append(1111) # 마지막에 값 추가
print('append : ',ls)

ls.pop() #마지막에 있는것을 빼냄
print('pop : ',ls)

ls.reverse()  #값을 뒤집어 줌
print('reverse : ',ls)

ls.sort()
print('sort : ',ls)

del( ls[2] ) #특정 위치의 값을 제거
print('del 2 : ' ,ls)

#result = ls.index(20)
result = ls.count(10)  # 값의 갯수 (없으면 0)
print('index 10 : ', result)

ls.insert(2,2000)  #특정 위치에 값을 추가
print('insert 2,2000 : ', ls)

ls.remove( 2000 ) #해당하는 값을 제거
print('remove 2000 : ',ls)

ls01 = [10,20,30]
ls02 = [40,50,60]
ls = ls01 + ls02
print( ls )

ls02.extend( ls01 )#내가 붙이고자 하는 리스트를 기준으로 사
print('ls02 : ' , ls02)
print('-'*20)

'''           
ls = []
while True:
    print("1.이름추가 2.모든 이름 보기 3.삭제")
    num = int(input(">>>> : "))
    if num == 1:
        name = input('이름 입력 : ')
        if ls.count(name) != 0:
            print('존재하는 이름')
        else:
            ls.append( name )
            print("저장 되었습니다")
        
    elif num ==2:
        print( ls )
        for n in ls:
            print("이름 : ",n)
    elif num == 3:
        name = input('삭제 이름 입력 : ')
        if ls.count(name) != 0:
            ls.remove( name )
            print(f"{name}님은 삭제 되었습니다!!!")
        else:
            print(f"{name} 존재하지 않습니다")
    else:
        print('프로그램 종료')
        break
'''
List = ['김개똥',"2002년입사",'잘못된 사항','등급B']
print( List)
#removeName = input("삭제 입력 : ")
#List.remove( removeName )
del(List[2])
print( List)
ls = List.copy()
for i in range(3):
    changeName = input("추가할 이름 입력 : ")
    ls[0] = changeName
    #removeName = ls[0]
    #ls.insert(0, changeName )
    #ls.remove(removeName)
    #print(ls)
    List.extend(ls)

print(List)
print("="*10)
print(len(List))
cnt = 1
for i in range( len(List) ):
    print(List[i], end="/")
    if cnt%3 == 0 :
        print()
    cnt += 1

'''
List = ['김개똥',"2002년입사",'잘못된 사항','등급B']
print( List)
#removeName = input("삭제 입력 : ")
#List.remove( removeName )
del(List[2])
print( List)
ls = List.copy()
for i in range(3):
    changeName = input("추가할 이름 입력 : ")
    ls[0] = changeName
    #removeName = ls[0]
    #ls.insert(0, changeName )
    #ls.remove(removeName)
    #print(ls)
    List.extend(ls)

print(List)
print("="*10)
print(len(List))
for i in range( len(List) ):
    if i%3 == 0 :
        print()
    print(List[i], end="/")
'''

ls = [ [1,2,3,],[4,5,6],[7,8,9] ] # ,를 잘 구분해야함 (안쪽에 몇개의 값이 있던지 ,를 기준으로 보면 됨)
'''
print( ls[2][1] ) # 2번째의 1번째 값

print( ls[0][2] )
print( ls[1] )
print( ls[2] )
'''
ls = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

for i in range(3): #range(len(ls))
    for k in range(4): #range(len(ls[i]))
        print(ls[i][k],end='\t')
    print()
print('='*10)
for i in ls:
    for k in i:
        print(k,end='\t')
    print()
