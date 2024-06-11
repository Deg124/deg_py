total=0

while True:
    num=int(input('더할 값: '))
    total+=num
    print('total의 값: ',total)
    if total>100:
        break