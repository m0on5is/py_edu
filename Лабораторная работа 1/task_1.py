numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_ = 0
for i in range(0, 20):
    if numbers[i] != None:
        sum_ += numbers[i]

len_ = len(numbers)
average = sum_ / len_

for i in range(0, 20):
    if numbers[i] == None:
        numbers[i] = average

print("Измененный список:", numbers)
