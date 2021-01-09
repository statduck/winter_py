#===========================================================================================
#02-1 숫자형
#===========================================================================================

#정수형
a = 123
a = -178
a = 0

#실수형
a = 1.2
a = -3.45
a = 4.24E10 #E는 지수
a = 4.24e-10

#8진수와 16진수
a = 0o177 #8진수는 0o 또는 0O로 시작
a = 0x8ff #16진수는 0x로 시작

#사칙연산
a = 3
b = 4
a + b
a * b
a / b
a ** b
3 % 7 #나머지 반환
7/4 
7//4 #몫 반환

#===========================================================================================
#02-2 문자열
#===========================================================================================

#문자열
"Hello World"
'Python is fun'
"""Life is too short, You need python"""
'''Life is too short, You need python'''

#multiline

multiline = "Life is too short\nYou need python" #방법1 이스케이프 코드 활용

multiline='''
Life is too short
You need python
''' #방법2 따옴표 세개 활용

print(multiline)

#문자열 연산

head = "Python"
tail = " is fun!"
head + tail

a = "Python"
a*2

#문자열 길이 구하기
a = "Life is too short"
len(a)

#문자열 인덱싱
a = "Life is too short, You need Python"
a[3]


#문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]

a = "Life is too short, You need Python"
a[0:4]

#슬라이싱으로 문자 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

#문자열 포맷팅

print("I eat %d apples." % 3) #숫자 대입
print( "I eat %s apples." % "five") #문자 대입

number = 3
print("I eat %d apples." % number) #숫자값을 가지는 변수 대입

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day)) #두개 이상의 값 대입

#포맷코드와 숫자 함께 사용하기

print("%10s" % "hi") #전체 길이가 10인 문자열 공간에서 대입되는 값을 오른쪽 정렬
print("%-10sjane." % 'hi')  #전체 길이가 10인 문자열 공간에서 대입되는 값을 왼쪽 정렬

print("%0.4f" % 3.42134234) #소숫점 표현하기, 4는 소수점 뒤에 나올 숫자의 개수를 나타냄
print("%10.4f" % 3.42134234) #숫자 3.421234234를 네 번째 자리까지만 표시하고 전체 길이가 10인 문자열 공간에서 오른쪽 정렬

#format 함수를 사용한 포매팅

print("I eat {0} apples".format(3)) #숫자 대입
print("I eat {0} apples".format("five")) #문자열 대입

number = 3
print("I eat {0} apples".format(number)) #변수대입

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day)) #두 개 변수 대입

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)) #이름으로 대입

print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3)) #인덱스 항목과 이름을 함께 대입

print("{0:<10}".format("hi")) #:<10 표현식으로 왼쪽정렬
print("{0:>10}".format("hi")) #:<10 표현식으로 오른쪽정렬
print("{0:^10}".format("hi")) #:^10 표현식으로 가운데정렬

print("{0:=^10}".format("hi")) #공백채우기
print("{0:!<10}".format("hi")) 

y = 3.42134234
print("{0:0.4f}".format(y)) #소수점 4자리까지만 표시하기

#f문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age = 30
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')  # 왼쪽 정렬
print(f'{"hi":>10}')  # 오른쪽 정렬
print(f'{"hi":^10}')  # 가운데 정렬

#문자열 관련 함수

a="hobby"
print(a.count('b')) #b의 개수 반환

a="Python is the best choice"
print(a.find('b')) #처음 나오는 위치 반환, 찾는 문자 없으면 -1 반환

a="Life is too short"
print(a.index('t')) #또다른 indexing방법

a="hi"
print(a.upper())
print(a.lower())

a="     hi"
print(a.lstrip())

a="hi    "
print(a.rstrip())

a="    hi    "
print(a.strip())

a = "Life is too short" #문자열 바꾸기
print(a.replace("Life", "Your leg"))

a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(':')) #공백을 기준으로 문자열 나누기(split)

#===========================================================================================
#02-3 리스트형
#===========================================================================================

#리스트는 숫자모음을 간단하게 표현 가능
odd = [1, 3, 5, 7, 9]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']] #리스트 자체를 요소값으로 가지는 것도 가능

#리스트 인덱싱
a = [1, 2, 3]
print(a)
print(a[0]) #리스트의 첫번째 요소
print(a[0]+a[2])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][0]) #리스트의 요소값으로 활용된 리스트의 하위요소값 반환

#리스트 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])

#리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

a = [1, 2, 3]
print(a*3) #리스트 반복
print(len(a)) #리스트 길이 구하기

print(str(a[2]) + "hi") #리스트의 숫자형과 문자열을 더해주려면 정수를 문자로 바꿔줘야 함

#리스트 수정과 삭제
a = [1, 2, 3]
a[2] = 4 #수정
print(a)

a = [1, 2, 3]
a[1] #삭제
print(a)

a = [1, 2, 3, 4, 5]
del a[2:] #슬라이싱을 활용하여 한꺼번에 삭제
print(a)

#리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5,6])
print(a)

#리스트 정렬(sort)
a = [1, 4, 3, 2] 
a.sort() #순서대로 정렬
print(a)

#리스트 뒤집기(reverse)
a = ['a', 'b', 'c']
a.reverse()
print(a)

#위치 반환
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))

#리스트에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4) #0번째 자리에 4 삽입
print(a)

#리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3) #첫번째로 나오는 3을 제거
print(a)

#리스트 요소 끄집어내기(pop)
a = [1,2,3]
print(a.pop()) #리스트의 맨마지막요소를 반환하고 해당 요소 삭제
print(a)

a =[1,2,3]
a.pop(1) #1번째 요소 반환 후 삭제
print(a)

#리스트 확장(extend)
a = [1,2,3]
a.extend([4,5]) #a리스트에 [4,5] 리스트 추가
print(a)

#===========================================================================================
#02-4 튜플 자료형
#===========================================================================================

#튜플은 리스트와 비슷하지만 []가 아닌 ()으로 요소를 둘러싸고 있으며 값을 바꿀 수 없다는 차이가 있음
t1 = ()
t2 = (1,) #자료를 하나만 가져도 쉼표 필요
t3 = (1, 2, 3)
t4 = 1, 2, 3 #괄호를 생략해도 무방
t5 = ('a', 'b', ('ab', 'cd'))

#튜플 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])

#튜플 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[1:]) #문자열, 리스트와 똑같음

#튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 + t2)

#튜플 곱하기
t2 = (3,4)
print(t2 * 3)

#튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
print(len(t1))

#===========================================================================================
#02-5 딕셔너리 자료형
#===========================================================================================

#딕셔너리는 Key와 Value를 한 쌍으로 가지는 자료형으로 순차적(sequence)이 아닌 Key를 통해 값을 반환
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)


#딕셔너리 쌍 추가, 삭제하기
a = {1: 'a'}
a[2] = 'b' #슬라이싱이 아닌 딕셔너리 쌍 추가
print(a)
a['name']=['pey']
print(a)
a[3]=[1,2,3]
print(a)
del a[1] #지정한 key 1에 대한 {key:value} 쌍 삭제
print(a)

#Key 사용하여 Value 얻기
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet']) 

#Key는 중복될 수 없으며 리스트도 사용 불가능. BUT 튜플은 Key로 사용 가능하다.

#딕셔너리 함수
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys()) #딕셔너리 a의 Key만을 반환
print(list(a.keys())) #dict_keys 객체를 리스트로 변환
print(a.values()) #딕셔너리의 Value만을 반환
print(a.items()) #딕셔너리의 Key와 Value를 쌍으로 묶은 "튜플"값 반환
a.clear() #딕셔너리 안의 모든 요소 삭제
print(a) 

a =  {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name')) #name에 해당하는 value 반환
print(a.get('foo', 'bar')) #미리 정해둔 default값 반환
print('name' in a) #해당 key가 딕셔너리 안에 있는지 조사 (in)
print('email' in a)

#===========================================================================================
#02-6 집합 자료형
#===========================================================================================

#집합 자료형은 집합 관련 처리를 위해 만들어짐
s1 = set([1,2,3])
print(s1)

s2= set("Hello")
print(s2) #문자열에 들어간 개별 문자값들 반환

#set은 중복을 허용하지 않으며 순서가 없어(unordered) 인덱싱으로 값을 얻을 수가 없다(딕셔너리와 마찬가지).
#set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환 후 사용

s1 = set([1,2,3])
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

#교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2) #교집합
print(s1.intersection(s2))

print(s1 | s2) #합집합
print(s1.union(s2))

print(s1 - s2) #차집합
print(s2- s1)  

#집합 자료형 관련 함수

s1 = set([1,2,3]) 
s1.add(4) #값 1개 추가하기(add)
print(s1)

s1 = set([1,2,3])
s1.update([4,5,6]) #값 여러개 추가하기(update)
print(s1)

s1 = set([1,2,3])
s1.remove(2) #x특정 값 제거(remove)
print(s1)

#===========================================================================================
#02-7 불 자료형
#===========================================================================================

#불(bool) 자료형은 참 또는 거짓을 나타내며 True, False 두 개 값만을 지님
a = True
b = False

print(type(a))
print(type(b))

print(1==1)
print(2 > 1)

bool('python')

#===========================================================================================
#02-8 변수
#===========================================================================================

a = 1
b = "python"
c = [1,2,3]

print(id(a)) #객체의 주소값을 알려주는 파이썬 내장함수

a = [1,2,3]
b = a

print(id(a))
print(id(b)) #id가 동일하게 나옴(객체가 같기 때문)
print(a is b)

a[1] = 4
print(a) #a에 값 변화를 주면 b도 변화가 반영된 채로 나옴
print(b)

#b변수를 생성할 때 a와 같은 값을 지니게 하면서 다른 주소를 주려면?
a = [1,2,3]
b = a[:] #1번 방법: [:] 이용하여 복사
a[1] = 4
print(a)
print(b)

from copy import copy #copy 모듈 활용
b = copy(a)
print(b is a)

#변수 만들기
a, b = ('python', 'life') #튜플로 변수 만들기
print(a, b)

(a, b) = 'python', 'life' #튜플은 괄호 생략 가능

[a,b] = ['python', 'life'] #리스트로 변수 만들기
print(a, b)

a = b = 'python'
print(a, b)

a = 3
b = 5
a, b = b, a
print(a, b)

#===========================================================================================
#02장 연습문제
#===========================================================================================

#Q1
a = 80
b = 75
c = 55
print((a+b+c)/3)

#Q2
print(13 % 2) #13은 나머지가 1이므로 홀수

#Q3
Gildong = "881120-1068234"
YYYYMMDD = Gildong[:6]
number = Gildong[7:]
print(YYYYMMDD)
print(number)

#Q4
pin = "881120-1068234"
print(pin[7])

#Q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#Q6
a = [1,3,5,4,2]
a = sort.a()
a = reverse.a()
print(a)

#Q07
a = ['Life', 'is', 'too', 'short']
b = " ".join(a)
print(b)

#Q08
a = (1, 2, 3)
a = a + (4,)
print(a)

#Q10
a = {'A':90, 'B': 80, 'C':70}
b = a.pop('B')
print(a)
print(b)

#Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set1 = set(a)
b = list(set1)
print(b)
