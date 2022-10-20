'''
관계연산자
- >, <. <=,,,,,
- 참(True) 또는 거짓(False)을 표현
'''

su1 = 3.1; su2 =3
print('sul >= su2 :', su1 >= su2)
print('sul < su2 :', su1 < su2)
print('sul == su2 :', su1 == su2)
print('sul != su2 :', su1 != su2)

'''
복합대입 연산자
+= , -= , *= ,,,
 예)
 a=10; => a = a + 100
       => a = a * 100 => a *= 100
'''

su1 = su2 = 5
su1 += 1; # su1(6) = su1(5) + 1
print('su1 += 1 => ' , su1)

su1 -= 1; # su1(5) = su1(6) - 1
print('su1 -= 1 => ' , su1)

su1 *= 1; # su1(25) = su1(5) (5)su2
print('su1 *= 1 => ' , su1)

su1 //= 1; # su1(5) = su1(25) // (5)su2
print('su1 //= 1 => ' , su1)

su1 %= 1; # su1(0) = su1(5) % (5)su2
print('su1 %= 1 => ' , su1)

su1 = 5; su2 = 3;
su1 **= su2 # su1(125) = su1(5) ** (3)su2
su1 -= 2 # su1(123) = su1(125) - 2
print('su1 / 4 : ', su1 / 4)
print('su1 // 4 : ', su1 // 4)
print('su1 % 4 : ', su1 % 4)

'''
논리 연산자
- 참 또는 거짓 표현
- and, or, not
- or : 값 or 값 => 하나라도 참이면 결과는 참
- and : 값 and 값 => 하나라도 거짓이면 거짓
                     모두가 참일 때 참
- not : not 값 => 결과값을 반전 시켜준다
'''

print( False or False )
print( (10>20) or (10%2 == 0) )

print( False and True )
print( True and True )

a = 100
#10 < 20 and 10 < 30   /    10 <20 <30은 안됨 기본적으로 2항연산
print( a>10 and a%2==0 )

print( not True )
print( not False )

'''
제어문
- if, 반복문, break, continue
사용 예)
if 조건식:
  종속문장

'''

print('1.쉬운 게임')
print('2.어려운 게임')
print('3.게임 종료')
#num = int(input('>>>> : '))
num = 1
if num == 1:
    print('쉬운 게임이 실행 됩니다')
if num == 2:
    print('어려운 게임이 실행 됩니다')
if num == 3:
    print('게임을 종료 합니다')
print('다음문장')
print("="*20)

num1 = 10; num2 = 15
if num1 > num2:
    print('참인경우 실행')
    print('참인경우 실행')
    print('참인경우 실행')
    print('참인경우 실행')
    print('참인경우 실행')
    print('참인경우 실행')
print('다음 문장 실행')

num = int(input('수를 입력해주세요 : '))
if num % 3 == 0:
    print(f'{num}은(는) 3의 배수입니다')
if num % 3 != 0:
    print(f'{num}은(는) 3의 배수가 아닙니다')
print('\n')

num = int(input('수를 입력해주세요 : '))
if num % 2 == 0:
    print(f'{num}은(는) 짝수입니다.')
if num % 2 == 1: #num %2 != 0
    print(f'{num}은(는) 홀수입니다.')
print('\n')

num1 = int(input('첫번째 수를 입력해주세요 : '))
num2 = int(input('두번째 수를 입력해주세요 : '))
if num1 > num2:
    print(f'두 수 중 큰 수는 {num1}입니다.')
if num1 < num2:
    print(f'두 수 중 큰 수는 {num2}입니다.')
print('\n')

num = int(input('절대값 수를 입력해주세요 : '))
if num >= 0:
    print(num,'의 절대값 : ', num)
if num < 0:
    print(num, '의 절대값 : ', num*-1)

day = int(input('날짜 입력 : '))
if day % 7 == 1:
    print(f'{day}일은 월요일입니다.')
if day % 7 == 2:
    print(f'{day}일은 화요일입니다.')
if day % 7 == 3:
    print(f'{day}일은 수요일입니다.')
if day % 7 == 4:
    print(f'{day}일은 목요일입니다.')
if day % 7 == 5:
    print(f'{day}일은 금요일입니다.')
if day % 7 == 6:
    print(f'{day}일은 토요일입니다.')
if day % 7 == 0: 
    print(f'{day}일은 일요일입니다.')
print('\n')

num1 = int(input('첫번째 수 : '))
num2 = int(input('두번째 수 : '))
num3 = int(input('세번째 수 : '))
if num1 > num2 and num1 > num3:
    print(f'세 수 중 가장 큰 수는 {num1}입니다.')
if num2 > num1 and num2 > num3:
    print(f'세 수 중 가장 큰 수는 {num2}입니다.')
if num3 > num1 and num3 > num2:
    print(f'세 수 중 가장 큰 수는 {num2}입니다.')
print('\n')

num1 = int(input('첫번째 수 : '))
num2 = int(input('두번째 수 : '))
if num1 > num2 and num1 % 2 == 0:
    print(num1,'은 크며 짝수다')
if num2 > num1 and num2 % 2 ==0:
    print(num2,'은 크며 짝수다')
print('\n')

num1 = int(input('첫번째 수 : '))
num2 = int(input('두번째 수 : '))
sum_ = num1 + num2
if sum_ % 2 ==0 and sum_%3 ==0: #sum_ % 6 == 0
    print('짝수이며 3의 배수다')
