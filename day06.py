for i in range(0,3,1): #i=0, i(0)<3, i=i+1
    print('상위for문 실행')
    for k in range(0,5,1): #k=0, k(0)<5, k=k+1
        print(f'이중 for문 i:{i}, k:{k}')
    print('상위for문 종료')
print('='*10)

# 구구단. 2*1=2

for i in range(2,10):
    for k in range(1,10):
        print(f'구구단 {i} * {k} = {i*k}') 
print('='*10)

for i in range(0,5): #end 사용
    print(f'상위포문 {i}일때 하위 포문 : ', end = ' ')
    for k in range(0,5):
        print(f'{i*k}',end = ' ')
    print()
print('='*10)

for i in range(0,5):
    for j in range(1,6):
        print(j + (5*i) , end = '\t')
    print()
print('='*10)

i = 0
while i<5:
    print(i, '종속 문장 실행')
    i += 1
print('다음 문장들 실행')
#for문으로 변경하세요.

for i in range(0,5):
    print(i,'종속 문장 실행')
print('='*10)

i=1
odd,even=0,0
while i<=10:
    if i%2 == 0:
        even += i
    else:
        odd += i
    i+=1
print('1~10까지의 짝수 합 : ',even)
print('1~10까지의 홀수 합 : ',odd)
#for문으로 변경

odd,even=0,0
for i in range(1,11):
    if i%2 == 0:
        even += i
    else:
        odd += i
print('1~10까지의 짝수 합 : ',even)
print('1~10까지의 홀수 합 : ',odd)
print('='*10)

'''
i=0
while i<5:
    if i == 3:
        break
        print('333333')
    print('i : ', i)
    i += 1
print('='*10)

i=0
while i<5:
    if i == 3:
        continue
        print('333333')
    print('i : ', i)
    i += 1
print('='*10)
'''

rice = 1000 * 100; mouse = 2; day=1
while True: # rice > 0:
    rice = rice - mouse * 20
    if day % 10 == 0:
        mouse *= 2
    print(f'{day}일 {mouse}마리 {rice}')
    if rice <= 0:
        break
    day += 1
print(f'{day}일 {mouse}마리')

money, j = 0,0
money = int(input('요금 투입 : '))
while True:
    print("==== 커피 자판기 ====")
    print("1.커피(200) 2.코코아(250) 3.반환 4.종료")
    j = int(input("메뉴 선택 : "))
    if j == 4:
        print("종료")
        break
    elif (j == 1 and money >= 200) or (j == 2 and money >= 250):
        print('맛있게 드세요')
        if j == 1:
            money -= 200
        else:
            money -= 250
    elif j == 3:
        print(money,"원 반환 금액")
        money = 0
    else:
        print("요금이 부족합니다")
