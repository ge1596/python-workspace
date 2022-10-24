#문제1

for n in range(1, 31, 1):
    print(n , end="\t")
    if n%5 == 0:
        print()
print('\n')

#문제2

sum_ = 0
num = int( input('수 입력 : '))
for i in range(1, num+1 , 1):
    sum_ += i
print(f"1~{num}까지의 합 : {sum_}")


oddSum = 0; evenSum = 0
for i in range(1, num+1 , 1):
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i
print(f"1~{num}까지의")
print("짝수 합 : ",evenSum)
print("홀수 합 : ",oddSum)
print('\n')

#문제3

sum_ = 0; sum2 = 0;
for i in range(1,101):
    sum_ += i
    if i%3==0 and i%5!=0:
        sum2 += i
print( sum_ - sum2)
print('\n')

num1 = int(input('수 입력 : '))
num2 = int(input('수 입력 : '))

sum_ = 0
if num1 > num2:
    max_ = num1
    min_ = num2
    #n = -1
else:
    max_, min_ = num2, num1
    #n = 1
    
for i in range(min_, max_+1):
    sum_ += i
print(sum_)
print('\n')

for day in range(1, 31):
    if day == 1:
        won = 10
    else:
        won = won * 2
print(f'30날 입금할 금액 : {won}')
print('\n')

#문제4

st = "It is a fun Python class"
a = 0
s = 0
n = 0
for i in st:
    n += 1
    if i == 'a':
      a += 1
    elif i == 's':
        s += 1
print(f'a의 개수:{a} , s의 개수:{s}')
print(f'총 개수(공백포함) : {n}')
