import tkinter as tk
from tkinter import ttk
from BD import getDataSet, unic
from SortMethods import *


def get_selected_characteristics():
    selected_characteristics = []
    if company_var.get():
        selected_characteristics.append('Company')
    if type_name_var.get():
        selected_characteristics.append('TypeName')
    if inches_var.get():
        selected_characteristics.append('Inches')
    if screen_resolution_var.get():
        selected_characteristics.append('ScreenResolution')
    if ram_var.get():
        selected_characteristics.append('Ram')
    if memory_var.get():
        selected_characteristics.append('Memory')
    if op_sys_var.get():
        selected_characteristics.append('OpSys')
    if weight_var.get():
        selected_characteristics.append('Weight')
    if price_var.get():
        selected_characteristics.append('Price_euros')
    return selected_characteristics


def filter_data():
    selected_characteristics = get_selected_characteristics()
    data = getDataSet()  # Получите ваш массив данных
    if 'Company' in selected_characteristics:
        companies = company_selector.get()
        data = sortByCompany(data, companies)
    if 'TypeName' in selected_characteristics:
        type_names = type_name_selector.get()
        data = sortByTypeName(data, type_names)
    if 'Inches' in selected_characteristics:
        inches = inches_selector.get()
        data = sortByInches(data, inches)
    if 'ScreenResolution' in selected_characteristics:
        screen_resolutions = screen_resolution_selector.get()
        data = sortByScreenResolution(data, screen_resolutions)
    if 'Ram' in selected_characteristics:
        rams = ram_selector.get()
        data = sortByRam(data, rams)
    if 'Memory' in selected_characteristics:
        memories = memory_selector.get()
        data = sortByMemory(data, memories)
    if 'OpSys' in selected_characteristics:
        op_sys = op_sys_selector.get()
        data = sortByOpSys(data, op_sys)
    if 'Weight' in selected_characteristics:
        weight_choice = weight_selector.get()
        data = sortByWeight(data, weight_choice)
    if 'Price_euros' in selected_characteristics:
        price_choice = price_selector.get()
        data = sortByPrice(data, price_choice)

    display_results(data)


def display_results(data):
    result_window = tk.Toplevel(root)
    result_window.title("Результаты")

    for i, laptop in enumerate(data):
        tk.Label(result_window, text=f"Ноутбук {i + 1}").grid(row=i, column=0, sticky='w')
        tk.Label(result_window, text=f"Компания - {laptop[1]}").grid(row=i, column=1, sticky='w')
        tk.Label(result_window, text=f"Продукт - {laptop[2]}").grid(row=i, column=2, sticky='w')
        tk.Label(result_window, text=f"Тип ноутбука - {laptop[3]}").grid(row=i, column=3, sticky='w')
        tk.Label(result_window, text=f"Размер экрана - {laptop[4]}").grid(row=i, column=4, sticky='w')
        tk.Label(result_window, text=f"Разрешение экрана - {laptop[5]}").grid(row=i, column=5, sticky='w')
        tk.Label(result_window, text=f"Процессор - {laptop[6]}").grid(row=i, column=6, sticky='w')
        tk.Label(result_window, text=f"ОП - {laptop[7]}").grid(row=i, column=7, sticky='w')
        tk.Label(result_window, text=f"Память - {laptop[8]}").grid(row=i, column=8, sticky='w')
        tk.Label(result_window, text=f"Видеокарта - {laptop[9]}").grid(row=i, column=9, sticky='w')
        tk.Label(result_window, text=f"ОС - {laptop[10]}").grid(row=i, column=10, sticky='w')
        tk.Label(result_window, text=f"Вес - {laptop[11]}").grid(row=i, column=11, sticky='w')
        price_euros = float(laptop[12])
        price_rubles = int(price_euros) * 100
        tk.Label(result_window, text=f"Цена - {price_rubles} рублей").grid(row=i, column=12, sticky='w')


# Создание главного окна приложения
root = tk.Tk()
root.title("Выбор характеристик")

# Создание фрейма для характеристик
characteristics_frame = ttk.LabelFrame(root, text="Выберите характеристики:")
characteristics_frame.grid(row=0, column=0, padx=10, pady=10)

# Создание чекбоксов для выбора характеристик
company_var = tk.BooleanVar()
company_checkbox = ttk.Checkbutton(characteristics_frame, text="Company", variable=company_var)
company_checkbox.grid(row=0, column=0, sticky='w')

type_name_var = tk.BooleanVar()
type_name_checkbox = ttk.Checkbutton(characteristics_frame, text="TypeName", variable=type_name_var)
type_name_checkbox.grid(row=1, column=0, sticky='w')

inches_var = tk.BooleanVar()
inches_checkbox = ttk.Checkbutton(characteristics_frame, text="Inches", variable=inches_var)
inches_checkbox.grid(row=2, column=0, sticky='w')

screen_resolution_var = tk.BooleanVar()
screen_resolution_checkbox = ttk.Checkbutton(characteristics_frame, text="ScreenResolution",
                                             variable=screen_resolution_var)
screen_resolution_checkbox.grid(row=3, column=0, sticky='w')

ram_var = tk.BooleanVar()
ram_checkbox = ttk.Checkbutton(characteristics_frame, text="Ram", variable=ram_var)
ram_checkbox.grid(row=4, column=0, sticky='w')

memory_var = tk.BooleanVar()
memory_checkbox = ttk.Checkbutton(characteristics_frame, text="Memory", variable=memory_var)
memory_checkbox.grid(row=5, column=0, sticky='w')

op_sys_var = tk.BooleanVar()
op_sys_checkbox = ttk.Checkbutton(characteristics_frame, text="OpSys", variable=op_sys_var)
op_sys_checkbox.grid(row=6, column=0, sticky='w')

weight_var = tk.BooleanVar()
weight_checkbox = ttk.Checkbutton(characteristics_frame, text="Weight", variable=weight_var)
weight_checkbox.grid(row=7, column=0, sticky='w')

price_var = tk.BooleanVar()
price_checkbox = ttk.Checkbutton(characteristics_frame, text="Price_euros", variable=price_var)
price_checkbox.grid(row=8, column=0, sticky='w')

# Создание селекторов для характеристик
company_selector = ttk.Combobox(characteristics_frame,
                                values=['Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI', 'Microsoft',
                                        'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer', 'Mediacom', 'Samsung', 'Google',
                                        'Fujitsu', 'LG'], state="disabled")
company_selector.grid(row=0, column=1)

type_name_selector = ttk.Combobox(characteristics_frame,
                                  values=['Ultrabook', 'Notebook', 'Netbook', 'Gaming', '2 in 1 Convertible',
                                          'Workstation'], state="disabled")
type_name_selector.grid(row=1, column=1)

inches_selector = ttk.Combobox(characteristics_frame,
                               values=['13.3', '15.6', '15.4', '14', '12', '11.6', '17.3', '10.1', '13.5', '12.5', '13',
                                       '18.4', '13.9', '12.3', '17', '15', '14.1', '11.3'], state="disabled")
inches_selector.grid(row=2, column=1)

screen_resolution_selector = ttk.Combobox(characteristics_frame,
                                          values=['IPS Panel Retina Display 2560x1600', '1440x900', 'Full HD 1920x1080',
                                                  'IPS Panel Retina Display 2880x1800', '1366x768',
                                                  'IPS Panel Full HD 1920x1080', 'IPS Panel Retina Display 2304x1440',
                                                  'IPS Panel Full HD / Touchscreen 1920x1080',
                                                  'Full HD / Touchscreen 1920x1080', 'Touchscreen / Quad HD+ 3200x1800',
                                                  'IPS Panel Touchscreen 1920x1200', 'Touchscreen 2256x1504',
                                                  'Quad HD+ / Touchscreen 3200x1800', 'IPS Panel 1366x768',
                                                  'IPS Panel 4K Ultra HD / Touchscreen 3840x2160',
                                                  'IPS Panel Full HD 2160x1440', '4K Ultra HD / Touchscreen 3840x2160',
                                                  'Touchscreen 2560x1440', '1600x900',
                                                  'IPS Panel 4K Ultra HD 3840x2160', '4K Ultra HD 3840x2160',
                                                  'Touchscreen 1366x768', 'IPS Panel Full HD 1366x768',
                                                  'IPS Panel 2560x1440', 'IPS Panel Full HD 2560x1440',
                                                  'IPS Panel Retina Display 2736x1824', 'Touchscreen 2400x1600',
                                                  '2560x1440', 'IPS Panel Quad HD+ 2560x1440',
                                                  'IPS Panel Quad HD+ 3200x1800',
                                                  'IPS Panel Quad HD+ / Touchscreen 3200x1800',
                                                  'IPS Panel Touchscreen 1366x768', '1920x1080',
                                                  'IPS Panel Full HD 1920x1200',
                                                  'IPS Panel Touchscreen / 4K Ultra HD 3840x2160',
                                                  'IPS Panel Touchscreen 2560x1440', 'Touchscreen / Full HD 1920x1080',
                                                  'Quad HD+ 3200x1800', 'Touchscreen / 4K Ultra HD 3840x2160',
                                                  'IPS Panel Touchscreen 2400x1600'], state="disabled")
screen_resolution_selector.grid(row=3, column=1)

ram_selector = ttk.Combobox(characteristics_frame,
                            values=['8GB', '16GB', '4GB', '2GB', '12GB', '6GB', '32GB', '24GB', '64GB'],
                            state="disabled")
ram_selector.grid(row=4, column=1)

memory_selector = ttk.Combobox(characteristics_frame,
                               values=['128GB SSD', '128GB Flash Storage', '256GB SSD', '512GB SSD', '500GB HDD',
                                       '256GB Flash Storage', '1TB HDD', '32GB Flash Storage', '128GB SSD +  1TB HDD',
                                       '256GB SSD +  256GB SSD', '64GB Flash Storage', '256GB SSD +  1TB HDD',
                                       '256GB SSD +  2TB HDD', '32GB SSD', '2TB HDD', '64GB SSD', '1.0TB Hybrid',
                                       '512GB SSD +  1TB HDD', '1TB SSD', '256GB SSD +  500GB HDD',
                                       '128GB SSD +  2TB HDD', '512GB SSD +  512GB SSD', '16GB SSD',
                                       '16GB Flash Storage', '512GB SSD +  256GB SSD', '512GB SSD +  2TB HDD',
                                       '64GB Flash Storage +  1TB HDD', '180GB SSD', '1TB HDD +  1TB HDD', '32GB HDD',
                                       '1TB SSD +  1TB HDD', '512GB Flash Storage', '128GB HDD', '240GB SSD', '8GB SSD',
                                       '508GB Hybrid', '1.0TB HDD', '512GB SSD +  1.0TB Hybrid',
                                       '256GB SSD +  1.0TB Hybrid'], state="disabled")
memory_selector.grid(row=5, column=1)

op_sys_selector = ttk.Combobox(characteristics_frame,
                               values=['macOS', 'No OS', 'Windows 10', 'Mac OS X', 'Linux', 'Android', 'Windows 10 S',
                                       'Chrome OS', 'Windows 7'], state="disabled")
op_sys_selector.grid(row=6, column=1)

weight_selector = ttk.Combobox(characteristics_frame,
                               values=['Меньше 1 килограмма', 'Меньше 1,5 килограмм', 'Меньше 2 килограмм',
                                       'Меньше 2,5 килограмма', 'Меньше 3 килограмм'], state="disabled")
weight_selector.grid(row=7, column=1)

price_selector = ttk.Combobox(characteristics_frame,
                              values=['Меньше 50000 руб', 'Меньше 100000 руб', 'Меньше 150000 руб', 'Меньше 200000 руб',
                                      'Меньше 250000 руб', 'Больше 250000 руб'], state="disabled")
price_selector.grid(row=8, column=1)

def toggle_selectors():
    company_selector['state'] = 'readonly' if company_var.get() else 'disabled'
    type_name_selector['state'] = 'readonly' if type_name_var.get() else 'disabled'
    inches_selector['state'] = 'readonly' if inches_var.get() else 'disabled'
    screen_resolution_selector['state'] = 'readonly' if screen_resolution_var.get() else 'disabled'
    ram_selector['state'] = 'readonly' if ram_var.get() else 'disabled'
    memory_selector['state'] = 'readonly' if memory_var.get() else 'disabled'
    op_sys_selector['state'] = 'readonly' if op_sys_var.get() else 'disabled'
    weight_selector['state'] = 'readonly' if weight_var.get() else 'disabled'
    price_selector['state'] = 'readonly' if price_var.get() else 'disabled'

# Включение/отключение селекторов при выборе характеристик
company_var.trace_add('write', lambda *args: toggle_selectors())
type_name_var.trace_add('write', lambda *args: toggle_selectors())
inches_var.trace_add('write', lambda *args: toggle_selectors())
screen_resolution_var.trace_add('write', lambda *args: toggle_selectors())
ram_var.trace_add('write', lambda *args: toggle_selectors())
memory_var.trace_add('write', lambda *args: toggle_selectors())
op_sys_var.trace_add('write', lambda *args: toggle_selectors())
weight_var.trace_add('write', lambda *args: toggle_selectors())
price_var.trace_add('write', lambda *args: toggle_selectors())

# Кнопка для фильтрации данных
filter_button = ttk.Button(root, text="Получить результат", command=filter_data)
filter_button.grid(row=1, column=0, padx=10, pady=10)
