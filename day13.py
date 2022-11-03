st = '    파이썬   '
print(f"*{st}*")

st = st.strip()
print(f"*{st}*")

if st == '파이썬':
    print('참')
else:
    print('거짓')
st = '---파이썬---'
print( st )
print( st.strip("-") )
print( st.rstrip("-") )
print( st.lstrip("-") )

st = 'Never ever give up'
print( st )
li = st.split()
print( li )

st = 'Never:ever:give:up'

li = st.split(",")
print( li )


st = '안녕하세요 오늘 2020/2/23 날씨는 error 춥다'
#[안녕하세요, 오늘 ,2020/2/23, 날씨는, error, 춥다]  공백을 기준으로 리스트로 저장
sp_li = st.split()
#year = [2020, 2, 23]
year = sp_li[2].split("/")
#[안녕하세요, 오늘, 날씨는, 춥다]
del(sp_li[4])
del(sp_li[2])

sp_li.insert(2,year[0]+'년'+year[1]+'월'+year[2]+'일') #값을 추가

print(sp_li)
st = ''
for i in sp_li:
    st += i+' '
print( st )

st = '''
안녕 하세요
반갑 습니다
추워요
'''
print( st.split('\n') )
print('='*20)
print(st.splitlines() )

st = '123'
re = '%'
print( re.join(st) )
print( '안녕'.join(st) )

li = ['123','안녕','하세요']
print( 'aaa'.join(li))

st = 'python'
print(st)
print(st.center(10))
print(st.center(10,'-'))
print(st.ljust(10))
print(st.rjust(10))
print(st.zfill(10))

accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"

replaceAB = accountBook.split(',')#,기준으로 리스트로 저장
k=0
for i in replaceAB:
    replaceAB[k]=i.lstrip() #각 문자열의 왼쪽 공백 삭제 후 저장(_coffee,_food,_dress)
    k+=1
kk='$ '
print('item'.ljust(10),end='')
print('date'.ljust(10),end='')
print('$(price)'.ljust(10))
for i in range(len(replaceAB)):
    z=replaceAB[i].split() #공백을 기준으로 리스트로 저장
    for k in range(len(z)):
        if k == 0 :
            print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력
        elif k ==1 :
            print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력
        elif k == 2 : 
            print("{:,}".format(int(z[k])).join(kk).ljust(10)) 

