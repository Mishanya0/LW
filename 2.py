try:
    user_input = input("Введите строку: ")
    if not user_input:
        raise ValueError("Строка не может быть пустой.")
    words = user_input.split()
    count = 0
    max_length = 0
    longer = ""
    for word in words:
        if len(word) % 2 == 0:
            count += 1
        if len(word) > max_length:
            max_length = len(word)
            longer = word
    print("Количество слов, которые имеют четную длину: ", count)
    print("Самое длинное слово: ", longer)
except ValueError as e:
    print(f"Ошибка: {e}")
