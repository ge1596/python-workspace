#문제1

for i in range(0,5): #end 사용
    print(f'상위포문 {i}일때 하위 포문 : ', end = ' ')
    for k in range(0,5):
        print(f'{i*k}',end = ' ')
    print()
print('='*10)

#문제2

for i in range(0,5):
    for j in range(1,6):
        print(j + (5*i) , end = '\t')
    print()
print('='*10)

#문제3

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
print('='*10)


#문제4

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
print('='*10)
