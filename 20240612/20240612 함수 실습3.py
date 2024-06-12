#임의의 개수의 숫자를 입력받아 그 합을 출력하는 함수를 작성하세요.
def add2(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

nums=list(map(int,input("숫자 입력(예: 10,20,30)").split(",")))
print(add2(nums))