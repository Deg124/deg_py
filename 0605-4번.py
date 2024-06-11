num1=int(input("1번 숫자: "))
num2=int(input("2번 숫자: "))
operator=input("연산자(+,-,*,/): ")

if operator=='+':
    print(num1,operator,num2,"=",num1+num2)
elif operator=='-':
    print(num1,operator,num2,"=",num1-num2)
elif operator=='*':
    print(num1,operator,num2,"=",num1*num2)
elif operator=='/':
    print(num1,operator,num2,"=",num1/num2)