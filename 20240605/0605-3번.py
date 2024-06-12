# 사용자로부터 3개의 정수를 입력받아 그 중 가장 큰 수를 출력하는 프로그램을 작성해보세요.

arr = list(map(int,input("3개의 숫자를 입력하시오(예시.10 5 12)").split(" ")))
print("가장 큰 값:",max(arr))
print("가장 작은 값:",min(arr))