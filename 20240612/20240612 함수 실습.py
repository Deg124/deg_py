#두 개의 숫자를 더하고 결과를 반환하는 함수를 작성하세요.
def add(a,b):
    return a+b
#이름과 나이를 입력받아 자기소개 문장을 출력하는 함수를 작성하세요. 나이는 기본값으로 0을 사용하세요.
def age(name,year):
    return "이름은"+name+"이고 나이는 "+str(year)+"입니다."
#임의의 개수의 숫자를 입력받아 그 합을 출력하는 함수를 작성하세요.
def add2(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

x=int(input("x에 수를 입력하세요: "))
y=int(input("y에 수를 입력하세요: "))
print(str(x)+"과 "+str(y)+"의 합은 "+str(add(x,y)))


name=input("이름: ")
year=int(input("나이: "))
print(age(name,year))

nums=list(map(int,input("숫자 입력(예: 10,20,30)").split(",")))
print(add2(nums))

