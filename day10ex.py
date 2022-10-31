#문제1

ls_1 = []
ls_2 = []
value = 1

for i in range(3):
    for j in range(4):
        ls_1.append( value )
        value += 1
    ls_2.append( ls_1 )
    ls_1 = []
print(ls_2)
    
for i in ls_2:
    #print( i )
    for k in i :
        print(k,end=' ')
    print()

ls_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print( len(ls_2) )
print( len(ls_2[0]) )
print( len(ls_2[1]) )

for i in range(len(ls_2)):
    for k in range(len(ls_2[i])):
        print( ls_2[i][k] , end= ' ')
    print()

for i in range(3):
    for k in range(4):
        print( ls_2[i][k] , end= ' ')
    print()
print('=' * 20)

#문제2
ls = [
    [['이름'],['나이'],['주소'],['지울값'],['연봉']],
    [['홍길동'],['20살'],['산골자기'],['지우세요'],['5000']],
    [['김개똥'],['30살'],['지구촌'],['지우세요'],['4500']]
    ]
#ls[1][4][0] = str(int(int(ls[1][4][0]) * 1.1))
#ls[2][4][0] = str(int(int(ls[2][4][0]) * 1.1))
                  
for i in range( len(ls) ):
    for j in range( len(ls[i]) ):
        if j%3==0 and j != 0:
            del(ls[i][j])
            if i != 0:
                ls[i][j][0] = str(int(int(ls[i][j][0]) * 1.1))
                
for i in ls:
    #print(i)
    for k in i:
        print(k,end=' ')
    print()
