#문제1

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
print('='*20)

#문제2

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
print('='*20)

#문제3

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
