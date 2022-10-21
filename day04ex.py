#문제1

num = int(input('1.Byte 2.KByte 3.MByte >>> '))

if num == 1:
    print(f'{GByte} : {Byte} byte')
if num == 2:
    print(f'{GByte} : {KByte} KByte')
if num == 3:
    print(f'{GByte} : {MByte} KByte')
print('\n')

save_id = input('저장할 ID 입력 : ')
save_pw = input('저장할 PW 입력 : ')
print('인증 프로그램 입니다')
input_id = input('ID 입력 : ')
input_pw = input('PW 입력 : ')
if save_id == input_id:
    if save_pw == input_pw:
        print('인증 통과 했습니다')
    else:
        print('비밀번호가 틀렸습니다')
else:
    print('등록되지 않은 아이디 입니다')
print('\n')

#문제2

name = input('이름 입력 : ')
su = input('학번 입력 : ')

print('3과목의 성적을 입력하시오')
kor = int(input('국어 성적 입력 : '))
eng = int(input('영어 성적 입력 : '))
math = int(input('수학 성적 입력 : '))
sum_ = kor + eng + math;avr = sum_ / 3

if avr >= 90:    result = 'A'
elif avr >= 80:    result = 'B'
elif avr >= 70:    result = 'C'
elif avr >= 60:    result = 'D'
else:    result = 'FFFFFFFF'

print('============== 학생 정보 ==================')
print('이름 : ',name,'\n학번 : ',su)
print('국 영 수 의 합 :',sum_,'\n평균 : ',avr,'\n등급 :',result)
print('\n')

#문제3번
''' 강사님 풀이
money=0
num = int(input('주문할 커피 개수 : '))
if num>10:
    money += 20000 + (num-10)*1500;
elif num>0 and num<=10:
    money = num*2000;
print(money,"원 입니다.\n");
'''

coffee = 2000
conum = int(input('주문할 커피의 개수 : '))

if conum > 10:
    coffee = 1500
    print('지불해야 할 총 금액 : {}원'.format(coffee * conum))
elif 0 < conum <= 10:
    print('지불해야 할 총 금액 : {}원'.format(coffee * conum))
else:
    print('잘못 입력하셨습니다.')
print('\n')

#문제4번

num = int(input('정수 입력 : '))
if num==0: 
    print(num,"은(는) 3의 배수도 4의 배수도 아닙니다");
elif num%3==0 and num%4==0: 
    print(num,"은(는)3의 배수 이면서,4의 배수입니다");
elif num%3==0:
    print(num,"은(는)3의 배수 입니다");
elif num%4==0:
    print(num,"은(는)4의 배수 입니다");
else: 
    print(num,"는 3의 배수도 4의 배수도 아님");
print('\n')

#문제5번

money=30000;
time = int(input("비행기 탄 시간(분): "))
time-=30
if time > 0:
   # money += (5000+((time-1)//10)*5000) 방법1
    if (time%10) == 0:
        money=money+time//10*5000
    else:
        money=money+time//10*5000+5000
print(money,"원 입니다.")
print('\n')

#문제6번

while True:
    print('='*30)
    print('{:^30}'.format("M E N U"))
    print('='*30)
    print('1.학생 이름 입력')
    print('2.성적 3과목(국,영,수) 입력')
    print('3.학생 이름 출력')
    print('4.합계 출력')
    print('5.평균 출력')
    print('6.종료')

    num = int(input(' >>> : '))
    if num == 1:
        name = input('학생 이름 입력 : ')
    elif num == 2:
        kor = int(input('국어 성적 입력 : '))
        eng = int(input('영어 성적 입력 : '))
        mat = int(input('수학 성적 입력 : '))
    elif num == 3:
        print('학생 이름 : ', name)
    elif num == 4:
        sum_ = kor + eng + mat
        print('성적 합계 : ', sum_)
    elif num == 5:
        avg = sum_ / 3
        print('성적 평균 : ', avg)
    elif num == 6:
        print('종료 합니다')
        break
    else:
        print('잘못 입력하셨습니다')
