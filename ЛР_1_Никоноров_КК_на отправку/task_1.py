numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_1 = numbers[:4]
numbers_2 = numbers[5:]
len_1 = len(numbers_1)
len_2 = len(numbers_2)

sum_1 = sum(numbers_1) + sum(numbers_2)
count_1 = len(numbers)
None_ = sum_1 / count_1
numbers[4] = None_

print("Измененный список:", numbers)
