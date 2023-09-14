shop_inventory = {
    "молоко": [2.5, 10],
    "яйца": [1.0, 20],
    "хлеб": [1.2, 15],
    "яблоки": [0.5, 30],
    "бананы": [0.8, 25]
}
while True:
    print("\nМеню:")
    print("1. Просмотр цены")
    print("2. Просмотр количества")
    print("3. Вся информация")
    print("4. Покупка")
    print("5. До свидания")
    choice = input("Выберите действие: ")

    if choice == '1':
        product_name = input("Введите название товара: ").lower()
        if product_name in shop_inventory:
            price = shop_inventory[product_name][0]
            print(f"{product_name} - Цена: {price} руб.")
    elif choice == '2':
        product_name = input("Введите название товара: ").lower()
        if product_name in shop_inventory:
              quantity = shop_inventory[product_name][1]
              print(f"{product_name} - Количество: {quantity} шт.")

    elif choice == '3':
          for product_name, info in shop_inventory.items():
                price = info[0]
                quantity = info[1]
                print(f"{product_name} - Цена: {price} руб., Количество: {quantity} шт.")
    elif choice == '4':
        total_cost = 0
        while True:
                product_name = input("Введите название товара (или 'n' для завершения покупки): ").lower()
                if product_name == 'n':
                      break
                if product_name not in shop_inventory:
                        print("Такого товара нет в магазине.")
                        continue
                try:
                        quantity_to_buy = int(input(f"Введите количество {product_name}: "))
                        if quantity_to_buy <= 0:
                            print("Количество должно быть больше нуля.")
                            continue
                        if quantity_to_buy > shop_inventory[product_name][1]:
                            print("Извините, товара в таком количестве нет в магазине.")
                            continue
                        price_per_unit = shop_inventory[product_name][0]
                        cost = price_per_unit * quantity_to_buy
                        total_cost += cost
                        shop_inventory[product_name][1] -= quantity_to_buy
                except ValueError:
                        print("Пожалуйста, введите корректное число.")
                        continue
                print(f"Общая стоимость покупки: {total_cost} руб.")
                print("Спасибо за покупку!")
    elif choice == '5':
        print("До свидания!")
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
