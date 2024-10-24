numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_none = 4

sum_ = sum(numbers[:index_none]) + sum(numbers[index_none+1:])
len_ = len(numbers)
average_of_numbers = sum_ / len_

numbers[index_none] = average_of_numbers
print("Измененный список:", numbers)
