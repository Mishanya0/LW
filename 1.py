num = int(input("Введите случайное число: "))
a = 1
while a <= num:
    if num % a == 0:
        print(a)
        a = a + 1
    else:
        a = a + 1
