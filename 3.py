try:
    a = int(input("Введите количество элементов списка: "))
    if a <= 0:
        raise ValueError("Количество элементов должно быть положительным.")
    rlist = []
    for i in range(a):
        while True:
            try:
                element = int(input(f"Введите элемент {i + 1}: "))
                rlist.append(element)
                break
            except ValueError:
                print("Пожалуйста, введите целое число.")
    i = 0
    maximum = min(rlist)
    while i < a:
        if rlist[i] % 2 == 0:
            if rlist[i] > maximum:
                maximum = rlist[i]
        i += 1
    if maximum % 2 == 1:
        print(rlist[0])
    else:
        print(maximum)
    print("Упорядоченный список:", sorted(rlist, reverse=True))
except ValueError as e:
    print(f"Ошибка: {e}")
