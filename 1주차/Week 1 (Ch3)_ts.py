#===========================================================================================
#03-1 if문
#===========================================================================================

money = True
if money:
    print("택시를 타고 가라") #if와 else 다음 행은 indentation 주기
else:
    print("걸어 가라") 

money = True
if money:
    print("택시를")
    print("타고")
    print("가라")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#x in s, x not in s 활용하기
pocket = ['paper', 'cellphone', 'Money']
if 'Money' in 'pocket':
    print("택시를 타고 가라")
else:
    print("걸어가삼")

#조건문에서 아무일도 일어나지 않게 설정하기
pocket = ['paper', 'Money', 'cellphone']
if 'Money' in pocket:
    pass
else:
    print("카드를 꺼내라") #pass를 설정하면 if문에 해당해도 아무 값도 안 나옴

#다양한 조건을 판단하는 elif
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
         print("걸어가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card: #추가 조건 지정, elif는 개수 한계 없이 사용 가능
    print("택시를 타고가라")
else:
    print("걸어가라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass #수행할 문장이 한줄이면 간단하게 콜론 뒤에 작성 가능
else: print("카드를 꺼내라")

#조건부 표현식
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

message = "success" if score >= 60 else "failure" #더 쉽게 표현 가능
#조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우

#===========================================================================================
#03-2 while문
#===========================================================================================

#while문은 반복해서 문장을 수행해야 할 경우에 사용
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

#while문 만들기
prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
    Enter number: """

number = 4
while number != 4:
    print(prompt)
    number = int(input()) #사용자의 숫자 입력을 받아들임

#while문 강제로 빠져나가기
coffee = 10
money = 300 #money는 0이 아니므로 항상 참
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: ")) #값을 입력받아 money변수에 대입
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

#while문 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1  
    if a % 2 == 0: continue #continue문은 while문의 맨 처음으로 돌아가게 하는 명령어
    print(a)

#무한루프
while True: #항상 참
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

#===========================================================================================
#03-3 for문
#===========================================================================================

test_list = ['one', 'two', 'three'] 
for i in test_list: 
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0 
for mark in marks: 
    number = number +1 
    if mark >= 60: 
        print("%d번 학생은 합격입니다." % number)
    else: 
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 80]

number = 0 
for mark in marks: 
    number = number +1 
    if mark < 60:
        continue #점수가 60이하인 경우에는 continue문이 수행되어 for문 처음으로 돌아가게 됨
    print("%d번 학생 축하합니다. 합격입니다. " % number) 

#range 함수
a = range(10) #range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체 생성
print(a)
range(0, 10) #끝 숫자는 미포함

add = 0 
for i in range(1, 11): 
    add = add + i 
print(add)

for i in range(2,10): #2부터 9까지의 숫자가 차례로 i에 대입
    for j in range(1, 10): #i가 처음 2일 때 1부터 9까지의 숫자가 차례로 j에 대입
        print(i*j, end=" ")  #매개변수 end: 결과값을 출력할 때 다음줄로 넘기지 않기 위해서
    print('')  #두번째 for문이 끝나면 결과값을 다음줄부터 출력하게 해주는 문장

#리스트 내포
a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)
    print(result)

a = [1,2,3,4]
result = [num * 3 for num in a] #리스트 내포 활용
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

result = [x*y for x in range(2,10)
               for y in range(1,10)]
print(result)

#===========================================================================================
#03 연습문제
#===========================================================================================

#Q01
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#출력되는 값은 shirt

#Q02
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

#Q03
i = 0
while True:
    i += 1
    if i > 5: break`
    print ('*' * i)

#Q04
for i in range(1, 101):
    print(i)

#Q05
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average) 

#Q06
numbers=[1,2,3,4,5]
result = [n*2 for n in numbers if n%2==1]
print(result)
[2, 6, 10]