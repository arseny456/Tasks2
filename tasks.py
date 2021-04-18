def func(N):
        for i in range(N):
            if N % (i+1) == 0:
                print(i+1,end=' ')
while 1:

    try:
        i = int(input("Введите число"))
        if i==0:
            print("Завершение работы")
            break
        func(i)
    except:
        print("Error")
