from MergeSort import merge_sort

import time
file = open('Input.txt', 'r')
nums = [int(i) for i in file.readline().split(',')]  # Считываем числа из файла и разбиваем их по запятым
file.close()

start = time.time()  # Засекаем время перед выполнением сортировки
merge_sort(nums)  # Вызываем функцию сортировки слиянием
time_job = (time.time() - start)  # Засекаем время после выполнения сортировки

file = open('Result.txt', 'w')
file.write(str(nums))  # Записываем отсортированный список в файл
file.close()
print(f"{len(nums)} numbers per {time_job} seconds")  # Выводим количество чисел и время сортировки
