#print(20 + 200)
#print('안녕하세요')
#print 괄호안의 내용을 출력하는 기능
print(100); print(2000)

'''
ESCAPE 문자
- 문자열 안에서 특수한 동작을 해주는 것
- \n : 엔터값과 비슷하다
- \t : tab크기만큼 커서를 오른쪽으로 이동
- \" : "(큰 따옴표) 출력
- \' : '(작은 따옴표 출력
'''

print("안\n녕\n하\n세\n요")
print('Have \t a \t good \t time')
print('1234567\t1\t12345678\t55')

print(" '안녕' """ )
print(" \"안녕\" ")

print(' ""안녕"" ')
print(' \'안녕\' ')

print(' \\ ' )
print(" c:/0.공유/")

print("\t\t#### 회비 정보 ####") 
print("="*55)
print("이름\t\t나이\t전화번호\t\t회비")
print("="*55)
print('홍길동\t\t\"15"\t010-123-1234\t￦20,000')
print('임꺽정\t\t\"20"\t010-234-2345\t￦30,000')
print('김말이\t\t\"28"\t010-345-3456\t￦50,000')
print("-"*55)
print("총합계\t\t\t\t\t￦100,000")
print("="*55)

print( "="*20 )


print( 2 * 123)
print( 120 / 3)

print( '안녕' , 123+100 )
print( '100' + '100' )
print( '안녕' + '하세요\n')

print( "12 + 54 =" ,12+54 ,'입니다') 
print( "268 - 42 =" ,268-42 ,'입니다')
print( "2 * 23 =" ,2*23 ,'입니다')
print( "120 / 3 =" ,120/3 ,'입니다') 

print('12+54=',12+54,'입니다')
print(f'12+54= {12+54} 입니다')

print('12+54= {} 입니다'.format(12+54) )
print('{} + {} = {}'.format(10,20,30) )
print('{2} + {1} = {0}'.format(10,20,30) ) #순서도 지정가능

print("{:,}".format(100000000000) ) # :,으로 알아서 숫자를 3자리씩 정렬

print("{:<10}왼쪽정렬{:0<10}".format('안녕','하세')) #비어있는 공간은 0으로 채움
print("{:>10}오른쪽정렬{:8>10}".format('안녕','하세')) #비어있는 공간은 8로 채움
print("{:^10}가운데정렬{:8^10}".format('안녕','하세')) #비어있는 공간은 8로 채움

'''
변수
- 데이터를 저장하기 위한 공간
- 데이터는 언제든지 변경 가능하다
변수 작명 규
- 의미를 부여해서 만든다
- 키워드(예약어)는 사용할 수 없다
- 한글로도 만들 수 있으나 영어로 만드세요
'''

num = 1000 # = : 대입연산자 ( 오른쪽에 있는 값을 왼쪽에 저장해주세요 )
print( num, "입니다" )
print( f'저장값 {num} 입니다' )
print( '저장값 {} 입니다'.format(num))

age = 30
print( age, "입니다" )
print( f'저장값 {age} 입니다' )
print( '저장값 {} 입니다'.format(age))

num = 33
print( num, "입니다" )
print( f'저장값 {num} 입니다' )
print( '저장값 {} 입니다'.format(num))

num = 5
print('변경후 :',num)

num = num + 100
print('연산 후 :',num)

num1 = 5
num2 = 10
sum_ = num1 + num2
print('n1 :',num1)
print('n2 :',num2)
print('sum :', sum_ )
#print( sum([1,2,3,4,5,6]) ) 이미 있는 변수명을 지정하려고 하면 문제가 생길 수 있다

num1 = 10
num2 = 20
sum_ = num1 + num2

print('    --- 출력 결과 ---')
print(f' num1({num1}) + num2({num2}) = {sum_}')
