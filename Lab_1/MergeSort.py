def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]  # Разделение списка на левую часть
        right = nums[mid:]  # и правую часть
        merge_sort(left)  # Рекурсивная сортировка левой части
        merge_sort(right)  # Рекурсивная сортировка правой части
        i = j = k = 0  # Инициализация индексов для объединения

        # Объединение левой и правой части в один отсортированный список
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]  # Если элемент из левой части меньше, помещаем его в nums
                i += 1
            else:
                nums[k] = right[j]  # Иначе помещаем элемент из правой части
                j += 1
            k += 1

        # Проверяем, остались ли элементы в левой и правой части и добавляем их
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1