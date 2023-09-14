while True:
    try:
        print("Введите кол-во элементов словаря -- ", end="")
        count = int(input())
        if count < 0:
            raise ValueError("Количество элементов не может быть отрицательным.")
        dict1 = {}
        for i in range(count):
            while True:
                try:
                    value = int(input(f"Введите значение для ключа {i+1}: "))
                    dict1[i+1] = value
                    break
                except ValueError:
                    print("Пожалуйста, введите целое число.")
        sorted_dict = {}
        sorted_dicto = {}
        sorted_keys = sorted(dict1, key=dict1.get)
        for i in sorted_keys:
            sorted_dict[i] = dict1[i]
        print("Прямой порядок: ", sorted_dict)
        sorted_dicto = dict(reversed(sorted_dict.items()))
        print("Обратный порядок: ", sorted_dicto)
        break
    except ValueError as e:
        print(f"Ошибка: {e}")
