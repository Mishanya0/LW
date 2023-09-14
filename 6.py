elements = []
while True:
    while True:
        try:
            user_input = input("Введите элемент кортежа (или 'q' для завершения ввода): ")
            if user_input.lower() == 'q':
                num = None
                break
            num = int(user_input)
            elements.append(num)
        except ValueError:
            print("Пожалуйста, введите целое число (или 'q' для выхода).")
    if num is None:
        break
my_tuple = tuple(elements)
sum_positive = 0
for num in my_tuple:
    if num > 0:
        sum_positive += num
print("Сумма положительных элементов:", sum_positive)

