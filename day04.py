'''
if 조건식:
    종속문장
else:
    종속문장
다음문장
'''
#num = int(input('수 입력 : '))
num = 1
if num == 1:
    print('1입력')
else:
    print('그 외의 값 입력')
print("다음 문장들 실행")

#save_id = input('저장할 id 입력 : ')
save_id='aaa'
print('인증 프로그램')
#input_id = input('비교할 id 입력 : ')
input_id='aaa'
if save_id == input_id:
    print('인증 통과')
else:
    print('인증 실패')

num = 9
if num % 3 == 0:
    if num % 2 == 0:
        print("num 2,3의 배수 입니다.")
        print("num 짝수이며 3의 배수 입니다.")
    else:
        print('num 3의 배수이며 짝수는 아니다.')
else:
    print('num은 3의 배수가 아닙니다.')
print("다음 문장들 실행")

#1 kbyte = 1024byte , 1 mbyte = 1024 kbyte, 1gbyte = 1024 mbyte


GByte = int(input('GByte 입력 : '))
MByte = GByte * 1024
KByte = MByte * 1024
Byte = KByte * 1024

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

'''
if 조건식:
    종속문장
elif 조건식:
    종속문장
elif ,,,,

else:
    종속문장
'''

num = int(input("수 입력 : "))
if num > 100:
    print("100보다 크다")
elif num > 50:
    print("50보다 크다")
elif num > 0:
    print("0보다 크다")
else:
    print("그 외의 값 입력")
print("다음 문장들 실행")


name = input("이름 : ")
st_id = int(input("학번 : "))
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))
sum_ = kor + eng + mat
avg = sum_ / 3

print(f'{name}')
print(f'{st_id}')
if avg >= 90:
    print('학점 : A')
elif avg >= 80:
    print('학점 : B')
elif avg >= 70:
    print('학점 : C')
elif avg >= 60:
    print('학점 : D')
else:
    print('학점 : F')

print("다음 문장들 실행")

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

while True:         #반복문
    print('='*20)
    print('1.데이터 입력')
    print('2.데이터 출력')
    print('3.종료')
    print('='*20)
    
    num = int(input('>>> : '))
    if num == 1:
        data = input("데이터 입력: ")
    elif num == 2:
        print("입력 데이터 : ",data)
    else:
        print("종료 합니다")
        break
        
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
