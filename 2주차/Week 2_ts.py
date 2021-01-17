#04-1 함수

def add(a,b):
    return a + b

a = 3
b = 4
c = add(a,b)
print(c)

#매개변수(parameter)와 인수(arguments)

def add(a,b):
    return a+b #a, b는 매개변수

print(add(3,4)) #3,4 는 인수

#일반적인 함수
def add(a, b): 
    result = a + b 
    return result
a = add(3, 4)
print(a)

#입력값이 없는 함수
def say(): 
    return 'Hi'  #괄호 안이 비어 있음

a = say()
print(a)

#결과값이 없는 함수
def add(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
 
print(add(3, 4)) #수행할 문장만 있지, 결과값인 "return" 부분이 없음

#입력값도 결괏값도 없는 함수
def say(): 
    print('Hi')
say()

#매개변수 지정하여 호출하기
def add(a, b):
    return a+b

result = add(a = 3, b = 7) 
print(result)

#입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args): 
    result = 0 
    for i in args: 
        result = result + i 
    return result  #매개변수 앞에 *를 붙이면 입력값을 모두 모아서 튜플로 만들어 줌

result = add_many(1,2,3)
print(result)
result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응선", 27, False)

#함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a +1
vartest(a)
print(a)

#함수 안에서 함수 밖의 변수를 변경하는 방법
def vartest(a): 
    a = a +1 
    return a #1. return사용

a = vartest(a) 
print(a)

a = 1 
def vartest(): 
    global a 
    a = a+1 #2. global 사용

vartest() 
print(a)

#lambda
add = lambda a, b: a+b
result = add(3, 4)
print(result)


#04-2 사용자 입력과 출력 

#프롬프트를 띄워서 사용자 입력 받기
number = input("숫자를 입력하세요: ")
print(number)

>>> print("life" "is" "too short") #+연산과 동일
lifeistoo short
>>> print("life"+"is"+"too short") #+연산과 동일
lifeistoo short
>>> print("life", "is", "too short") #띄어쓰기는 콤마로
life is too short

#05-1 클래스

result = 0

def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

#계산기가 많아지면 위 함수구조를 활용하기가 어렵다. 따라서 클래스를 활용한다. 다음 프로그램을 활용하면 함수 2개를 사용하는 것과 같은 결과값을 출력 가능하다.

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#사칙연산 클래스 만들기

a = FourCal()
a.setdata(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div()) #위와 같은 FourCal 클래스를 만들어보자.

#클래스 구조 만들기

class FourCal:
    pass

a = FourCal()
    type(a)
<class '__main__.FourCal'>

#객체에 숫자 지정 가능하도록 만들기

class FourCal:
     def setdata(self, first, second):
         self.first = first
         self.second = second

         >>> class FourCal:
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result

a = FourCal()
a.setdata(4, 2)
print(a.add())

def add(self):
    result = self.first + self.second
    return result

class FourCal:
     def setdata(self, first, second):
         self.first = first
         self.second = second
     def add(self):
         result = self.first + self.second
         return result
     def mul(self):
         result = self.first * self.second
         return result
     def sub(self):
         result = self.first - self.second
         return result
     def div(self):
         result = self.first / self.second
         return result

#클래스의 상속
class MoreFourCal(FourCal):
     pass

class MoreFourCal(FourCal):
     def pow(self):
         result = self.first ** self.second
         return result


#05-2 모듈

def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

#위 add, sub 함수만 있는 파일을 만들고 C:\doit 디렉터리에 저장하면 모듈이 된다.

import 모듈이름

from 모듈이름 import 모듈함수
add(3, 4) #바로 모듈의 함수를 사용하는 것이 가능

from mod1 import * #모든 함수 불러오기


#05-4 예외 처리

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e: #예외처리
    print(e)    