import unittest
from MergeSort import merge_sort
import time

class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        # Тестирование функции merge_sort с валидными входными данными
        first_case_test = [1, 3, 2]
        second_case_test = [1, 2, 3, 4, 5]
        third_case_test = [2, 1]

        sorted_first_case = merge_sort(first_case_test)
        sorted_second_case = merge_sort(second_case_test)
        sorted_third_case = merge_sort(third_case_test)

        self.assertEqual(sorted_first_case, [1, 2, 3])
        self.assertEqual(sorted_second_case, [1, 2, 3, 4, 5])
        self.assertEqual(sorted_third_case, [1, 2])

        # Вывод отсортированных массивов и времени выполнения
        print("Отсортированный массив:", sorted_first_case)
        print("Время выполнения программы на {} значениях составляет {} секунд".format(len(first_case_test), time.time()))

        print("Отсортированный массив:", sorted_second_case)
        print("Время выполнения программы на {} значениях составляет {} секунд".format(len(second_case_test), time.time()))

        print("Отсортированный массив:", sorted_third_case)
        print("Время выполнения программы на {} значениях составляет {} секунд".format(len(third_case_test), time.time()))

    def test_merge_sort_with_invalid_input(self):
        # Тестирование функции merge_sort с невалидными входными данными
        int_error = -33
        string_error = "33"
        array_error = [123]
        bool_error = False

        with self.assertRaises(TypeError):  # Изменено с ValueError на TypeError
            merge_sort(int_error)

        with self.assertRaises(TypeError):  # Изменено для соответствия ожидаемому TypeError
            merge_sort(string_error)
            merge_sort(array_error)
            merge_sort(bool_error)

    def test_merge_sort_with_non_list_input(self):
        # Тестирование функции merge_sort с неверным типом входных данных
        non_list_input = 123
        with self.assertRaises(TypeError):
            merge_sort(non_list_input)

if __name__ == '__main__':
    unittest.main()
