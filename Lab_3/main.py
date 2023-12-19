import tkinter as tk
from tkinter import ttk
import math

# Функция для вычисления значения функции f(x) = x^3 - m * sin(x)
def func(x, m):
    return x**3 - m * math.sin(x)

# Функция для выполнения вычислений и обновления Treeview
def Run():
    # Получение значений от пользователя из виджетов ввода
    start = float(start_entry.get())
    end = float(end_entry.get())
    step = float(step_entry.get())
    m = float(m_entry.get())

    # Очистка предыдущих записей в Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Вычисление значений функции и вставка их в Treeview
    current_x = start
    while current_x <= end:
        y = func(current_x, m)
        tree.insert("", "end", values=(current_x, y))
        current_x += step

    # Обновление метки для отображения текущей функции
    function_label.config(text=f'Функция: f(x) = x^3 - {m} * sin(x)')

# Создание основного окна Tkinter
window = tk.Tk()
window.title("Лабораторная работа 3")

# Настройка стилей для меток и кнопок
style = ttk.Style()
style.configure("TLabel", padding=5, font=('Helvetica', 10))
style.configure("TButton", padding=10, font=('Helvetica', 10, 'bold'))

# Создание фрейма внутри окна
frame = ttk.Frame(window)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=20, pady=20)

# Метка для отображения текущей функции
function_label = ttk.Label(frame, text="Функция: f(x) = x^3 - m * sin(x)", style="TLabel", font=('Arial', 14, 'bold'))
function_label.grid(column=0, row=0, columnspan=2, pady=(0, 10), sticky="w")

# Метки и виджеты ввода для пользовательского ввода
start = ttk.Label(frame, text="Начало диапазона:", style="TLabel")
start_entry = ttk.Entry(frame)
end = ttk.Label(frame, text="Конец диапазона:", style="TLabel")
end_entry = ttk.Entry(frame)
step = ttk.Label(frame, text="Шаг:", style="TLabel")
step_entry = ttk.Entry(frame)
m = ttk.Label(frame, text="Параметр m:", style="TLabel")
m_entry = ttk.Entry(frame)

# Кнопка для запуска вычислений
button = ttk.Button(frame, text="Рассчитать", style="TButton", command=Run)

# Treeview для отображения результатов
tree = ttk.Treeview(frame, columns=("x", "f(x)"), show="headings")
tree.heading("x", text="x")
tree.heading("f(x)", text="f(x)")

# Размещение меток, виджетов ввода, кнопки и Treeview внутри фрейма
start.grid(column=0, row=1, sticky="w", pady=(0, 5))
start_entry.grid(column=1, row=1, pady=(0, 5), sticky="w")
end.grid(column=0, row=2, sticky="w", pady=(0, 5))
end_entry.grid(column=1, row=2, pady=(0, 5), sticky="w")
step.grid(column=0, row=3, sticky="w", pady=(0, 5))
step_entry.grid(column=1, row=3, pady=(0, 5), sticky="w")
m.grid(column=0, row=4, sticky="w", pady=(0, 5))
m_entry.grid(column=1, row=4, pady=(0, 5), sticky="w")
button.grid(column=0, row=5, columnspan=2, pady=10, sticky="w")
tree.grid(column=0, row=6, columnspan=2, pady=(10, 0), sticky="w")

# Запуск цикла событий Tkinter
window.mainloop()
