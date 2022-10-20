#문제1

num = int( input('수 입력 : '))
if num % 3 == 0 :
    print(num,"은 3의 배수")
if num % 2 == 0:
    print(num,"은 짝수")
if num % 2 != 0: # num%2 == 1
    print(num,"은 홀수")
num1 = int(input('큰수 비교 수 입력 : '))
num2 = int(input('큰수 비교 수 입력 : '))
if num1 > num2:
    #print(num1,"큰 수")
    max_ = num1
if num2 > num1:
    #print(num2,"큰 수")
    max_ = num2
print(max_,"큰 수")

num1 = int(input('절대값 수 입력 : '))
if num1 > 0:
    print(num1,"의 절대값은 : ",num1)
if num1 < 0:            #num1 * -1 => -num1
    print(num1,"의 절대값은 : ", num1 * -1)
print('\n')

#문제2
    
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

