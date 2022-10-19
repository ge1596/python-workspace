#문제1

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
print('\t')

#문제2

su = 100
num = '100'
flt = "1.111"

print( su + int(num) )
print( su + float(flt) )
print( str(su) + num )

#문제3

print("두 수의 합을 구해 줍니다!!!")
n1 = input('수입력 : ')
n2 = input('수입력 : ')
n3 = int(n1) + int(n2)
print(f'두 수의 합 {n1} + {n2} = {n3}')

#문제4

thisyear = int(input('올해의 년도를 4자리로 입력하세요 : '))
year = int(input('태어난 년도를 4자리로 입력하세요 : '))
age = thisyear - year
print(f'당신의 나이는 {age}살 입니다')
print('\n')

weight1 = float(input('첫 번째 물건의 무게를 입력하시오 : '))
weight2 = float(input('두 번째 물건의 무게를 입력하시오 : '))
more = 600 - (weight1 + weight2)
print(f'현재 엘리베이터에 허용 무게는 {more}kg입니다.')

#문제5

height = float(input('키를 입력하세요 : '))
standardweight = (height - 100) * 0.9
print(f'표준 체중은 {standardweight}입니다.')
print('\n')

height = float(input('키를 입력하세요 : '))
weight = float(input('현재체중을 입력하세요 : '))

obesity = (weight / standardweight ) * 100
print('표준 체중은 {}이고 비만도는 {}입니다.'.format(standardweight,round(obesity,2)))
print('\n')

#문제6

name = input('학생 이름 : ')
kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int (input('수학 점수 : '))
sum_ = kor +eng + mat
avg = sum_ / 3

print('=================학생 정보======================')
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*47)
print('{}\t{}\t{}\t{}\t{}\t{}'.format(name,kor,eng,mat,sum_,round(avg,2)))

