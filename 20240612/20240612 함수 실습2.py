#이름과 나이를 입력받아 자기소개 문장을 출력하는 함수를 작성하세요. 나이는 기본값으로 0을 사용하세요.
def age(name,year):
    return "이름은"+name+"이고 나이는 "+str(year)+"입니다."

name=input("이름: ")
year=int(input("나이: "))
print(age(name,year))