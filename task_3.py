# 3) Для чисел в пределах от 20 до 240
# найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.

# Подсказка: использовать функцию range() и генератор.

if __name__ == '__main__':
    # all items to ram
    # generator_collection = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]

    generator = (i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0)
    result_list = list(generator)
    print(f"Result {result_list}")
