'''
Tuple
- 중복된 데이터를 가질 수 없다.
- 데이터 변경이 불가능  (한번 저장이 되면 변경이 불가능 - 신뢰성을 가지는 정보)
- index로 접근 가능하다
- 소괄호가 있으면 튜플로 보면 된다.
'''

tp = (10,20,30)
print( 'tp : ', tp)
print('tp[0] : ', tp[0])
print( 'type(tp) : ', type(tp) )
print( 'len(tp) : ', len(tp) )

#tp[0] = 1000 #개별적으로 변경이 불가능
tp = (111,222,333,444) #통째로는 변경 가
print('tp : ', tp)
print('='*20)

tp = (10)
print(type(tp))

tp = (10,)
print(type(tp))

tp = 10,
print(type(tp))

'''
packing : 압축(여러개의 값을 가지고 있다)
'''

pack = 1,2, "패킹"
print("패킹 : ", pack)
print( type(pack) )

a,b,c = pack #언팩
print( a,b,c )

a, *b = pack #첫번째 값은 a에, 나머지값은 b에 저장해주겠다
print(a,b)
print(type(a), type(b))

pack = 10,20,10,10,30
print( pack.count(10) ) #해당 값의 갯수
print( pack.index(20) ) #해당 값의 위치

print('='*20)
str_  = 'Have a nice day' 
print(str_[0])
print(str_[1])

li = [1,2,3,4]
print( li[-1] )
print(str_[-1] )

for i in range( len(str_) ):
    print( str_[i], end = ' ' )
print()
for i in str_:
    print(i, end = " " )
print()
print(str_[7:11])

str_ = "python test. 그리고 programming 할만하다 ^^"
print(str_)
print("upper : ", str_.upper() ) #대문자로 변경해줌
print("lower : ",str_.lower() ) #소문자로 변경해줌
print("swapcase : ",str_.swapcase() ) #대소문자 변환
print("title : ",str_.title() ) #첫글자만 대문자 변환


str_ = 'NevEr -eVer 110gIVe up'

str_1 = str_.title()
print(str_)
print(str_1)
print('='*20)

st = 'Have a nice day'
print(st.count('a'))  #해당 값의 갯수
print(st.count('day'))
print(st.count('dak'))

print(st.startswith('Ha')) # ~로 시작하는 단어가 있는지
print(st.startswith('ha'))
 
print(st.endswith('ay')) # ~로 끝나는 단어가 있는지
print(st.endswith('dday'))

st = 'It is a fun Python class'

print(len(st))
print(st.count('a'))
print(st.count('s'))
print('='*20)

st= 'Have a nice day'
print(st)

print(st.find('day'))  #해당 값의 위치
print(st.index('day')) #해당 값의 위치

print(st.find('kkk')) #해당 값이 없으면 -1
#print(st.index('kkk')) #해당 값이 없으면 에러

print( st.find('a') ) #첫번째 a의 위치만 알려줌
print( st.find('a',2) ) # 2번째 index부터 찾아줌
print( st.find('a',6) )
print( st.find('a',14) )

c = st.find('a',2)
print(c)
c = st.find('a',c+1)
print(c)
print('='*20)

st = 'Have a nice day Have a nice day Have a nice day'

li = list()
cnt = 0
while True:
    cnt = st.find('a', cnt)
    if cnt != -1:
        li.append(cnt)
    else:
        break
    #print(cnt)
    cnt += 1
print('a 개수 : ',st.count('a'))
print('index : ',li) 

li = ['AbCe test123','.acd efg','a123 TEST 123','123 TEst']

for i in li:
    #print( i )
    lo = i.lower()
    if lo.startswith('ab') or lo.endswith('test'):
        print(i)

st = '2015/04/02'

print(st)
st1 = st.replace("/",".")
print(st)
print(st1)
print( st.replace(st[0:4],"2022"))

st = '''
김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018 05월 14일
'''

st = st.replace("-",":")
i = 0

for k in range(st.count(":")):
    i = st.find(":",i+1)
    st = st.replace(st[i+1:i+5],"1999")
print(st)
        
 


#replace, find, startswith
