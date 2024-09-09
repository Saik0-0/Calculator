import re
from functools import partial
from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.title("Calculator")
root.geometry("230x300")
root.resizable(False, False)
root['bg'] = 'PaleVioletRed'

nums = ['', '']   # хранение введённых чисел
current_num = ''


#   функция для ввода цифр с кнопок
def print_num(num):
    if button_other_entry['text'] == 'Enter\nfirst':
        first_num_entry.insert(END, num)
    else:
        second_num_entry.insert(END, num)


#   функция для получения введенных чисел
def take_num(event):
    global nums
    if first_num_entry.get() != '':
        nums[0] = float(first_num_entry.get())
    if second_num_entry.get() != '':
        nums[1] = float(second_num_entry.get())
    else:
        button_other_entry['text'] = 'Enter\nsecond'
        second_num_entry.focus()
    if nums[0] != '' and nums[1] != '':
        button_other_entry['text'] = 'Choose\naction'
        button_div.config(command=partial(button_div_func, nums[0], nums[1]))
        button_mod.config(command=partial(button_mod_func, nums[0], nums[1]))
        button_sum.config(command=partial(button_sum_func, nums[0], nums[1]))
        button_sub.config(command=partial(button_sub_func, nums[0], nums[1]))


#   функция delete
def delete_func(num_of_entry):
    if num_of_entry == 'first':
        first_num_entry.delete(END)
    elif num_of_entry == 'second':
        second_num_entry.delete(END)


#   функции операций
def button_div_func(num_1, num_2):
    if re.fullmatch('(-)?0+(.)(0+)', second_num_entry.get()):
        showinfo('Ошибка', 'Нельзя делить на ноль')
    else:
        showinfo('Результат целочисленного деления', str(num_1 // num_2))
    global nums
    nums = ['', '']
    button_other_entry['text'] = 'Enter\nfirst'
    first_num_entry.delete(0, last=END)
    second_num_entry.delete(0, last=END)
    first_num_entry.focus()


def button_mod_func(num_1, num_2):
    if re.fullmatch('(-)?0+(.)(0+)', second_num_entry.get()):
        showinfo('Ошибка', 'Нельзя делить на ноль')
    else:
        showinfo('Результат взятия остатка', str(num_1 % num_2))
    global nums
    nums = ['', '']
    button_other_entry['text'] = 'Enter\nfirst'
    first_num_entry.delete(0, last=END)
    second_num_entry.delete(0, last=END)
    first_num_entry.focus()


def button_sum_func(num_1, num_2):
    showinfo('Результат сложения', str(num_1 + num_2))
    global nums
    nums = ['', '']
    button_other_entry['text'] = 'Enter\nfirst'
    first_num_entry.delete(0, last=END)
    second_num_entry.delete(0, last=END)
    first_num_entry.focus()


def button_sub_func(num_1, num_2):
    showinfo('Результат вычитания', str(num_1 - num_2))
    global nums
    nums = ['', '']
    button_other_entry['text'] = 'Enter\nfirst'
    first_num_entry.delete(0, last=END)
    second_num_entry.delete(0, last=END)
    first_num_entry.focus()


#   кнопки циферок
button_labels = ['1', '2', '3', '+',
                 '4', '5', '6', '-',
                 '7', '8', '9', 'delete',
                 '+/-', '0', '.']
count_x = 20
count_y = 130
for i, label in enumerate(button_labels):
    if label.isdigit() or label == '.':
        button = Button(text=label, command=partial(print_num, label))
    elif label == 'delete':
        button = Button(text=label, command=lambda: root.focus_get().delete(len(root.focus_get().get()) - 1))
    elif label == '+/-':
        button = Button(text=label, command=partial(print_num, '-'))
    elif label == '+':
        button_sum = Button(text=label)
        button = button_sum
    elif label == '-':
        button_sub = Button(text=label)
        button = button_sub
    else:
        button = Button(text=label)
    button.place(height=25, width=40, x=count_x, y=count_y)

    if i % 4 == 3:
        count_y += 40
        count_x = 20
    else:
        count_x += 50


#  кнопки див мод след begin
button_div = Button(text='Div')
button_div.place(height=30, width=60, x=20, y=90)
button_mod = Button(text='Mod')
button_mod.place(height=30, width=60, x=150, y=90)
button_other_entry = Button(text='Enter\nfirst')
button_other_entry.place(height=30, width=50, x=90, y=90)

# поля ввода:
first_num_entry = Entry(justify=RIGHT)
first_num_entry.place(height=40, width=90, x=20, y=30)
first_num_entry.focus()
second_num_entry = Entry(justify=RIGHT)
second_num_entry.place(height=40, width=90, x=120, y=30)

# привязка функций к кнопкам
button_other_entry.bind('<Button-1>', take_num)


root.mainloop()

print(nums)