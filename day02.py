flt = 123.567
print( flt ) 
print( 'round(flt) : ',round(flt) )
print( 'round(flt,1) : ',round(flt,1) )
print( 'round(flt,2) : ',round(flt,2) )
print('\n')

py = 100
c = 50
java= 70
sum_ = py + c + java
print("합 : ",sum_)
print("평균 : ",round(sum_/3,2))
print('\t')

station = 11
minite = 37
average = minite / station

print('역의 평균 시간 : ', round(average,2))
print('\t')

oneFloorHeight = 500.23
avgFloorHeight = 260
cntFloor = 13

buildingHeight = oneFloorHeight + cntFloor*avgFloorHeight
print('건물 높이 : ',round(buildingHeight/100,3))

flt = 123.123
print(flt + 20)

st = '파'; st1 = '이썬'
print( st + st1 )

num = 100
print( type(num) ) #문자의 타입 확인
print( type(1.123) )
st = "안녕하세요"
print( type(st) )

print( type(str(num)) )
print( '안녕하세요'+ str(num) ) #문자의 타입 변경

su = 100
num = '100'
flt = "1.111"

print( su + int(num) )
print( su + float(flt) )
print( int(float(flt) ))
print( str(su) + num )

num = input ('숫자 입력 : ')
print( '입력 받은 수 : ', num )

name = input('이름 입력: ')
age = input('나이 입력 : ')
print(f'{name}님의 나이는 {age}살 입니다')

print("두 수의 합을 구해 줍니다!!!")
n1 = input('수입력 : ')
n2 = input('수입력 : ')
n3 = int(n1) + int(n2)
print('두 수의 합 : ',n3)
print(f'두 수의 합 {n1} + {n2} = {n3}')
n3 = n1 + n2
print('{}+{}={}'.format(n1,n2,n3)) #형 변환은 해당 줄에서만 적용

name = input('이름 입력 : ')
age = int( input('나이 입력 : ') ) #입력 받을때부터 형 변환을 하면 끝까지 유지
flt = float(float(input('실수 입력 : ')))
print(f'{name}, type:{ type(name) }')
print(f'{age}, type:{ type(age) }')
print(f'{flt}, type:{ type(flt) }')

print( age- 1 )

thisyear = int(input('올해의 년도를 4자리로 입력하세요 : '))
year = int(input('태어난 년도를 4자리로 입력하세요 : '))
age = thisyear - year
print(f'당신의 나이는 {age}살 입니다')
print('\n')

weight1 = float(input('첫 번째 물건의 무게를 입력하시오 : '))
weight2 = float(input('두 번째 물건의 무게를 입력하시오 : '))
more = 600 - (weight1 + weight2)
print(f'현재 엘리베이터에 허용 무게는 {more}kg입니다.')
