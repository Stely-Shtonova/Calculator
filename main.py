from tkinter import *

window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
calc_width = 321
calc_height = 637
window.geometry(f"{calc_width}x{calc_height}+{(screen_width // 2)-(calc_width // 2)}"
                f"+{(screen_height // 2)-(calc_height // 2)-35}")
window.title("Calculator")
window.configure(bg='#242323')

result = ''
label = Label(window, text = result, bg='#242323', fg= 'white', font=("Comic Sans MS", 17), relief="flat", width=22, height=2)
label.grid(row=0, column=0, columnspan=4)

def check_nums_type(x, y):
    if '.' in x and '.' in y:
        return float(x), float(y)
    elif '.' in x and not '.' in y:
        return float(x), int(y)
    elif not '.' in x and '.' in y:
        return int(x), float(y)
    else:
        return int(x), int(y)

def operation(operator, x, y):
    num1, num2 = check_nums_type(x, y)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        final = num1 - num2
        if (type(num1) == float or type(num2) == float) and final == 0:
            return round(final)
        elif (type(num1) == float or type(num2) == float) and final != 0:
            return round(final, 10)
        else:
            return final
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return num1 % num2

def find_operator(text):
    for char in text:
        if char in ['+', '-', '*', '/', '%']:
            return char
    return None

def button_functionality(v):
    global result
    if v.isdigit() or v in ['-', '+', '/', '*', '%'] or v == '.':
        result += v
        label.config(text = result)
    elif v == '=':
        operator = find_operator(result)
        result = operation(operator, result[:result.index(operator)], result[result.index(operator)+1:])
        label.config(text = result)
    elif v == '<-':
        stack = list(result)
        stack.pop()
        res = ''.join(stack)
        label.config(text = res)
        result = res
    else:
        label.config(text = '')
        result = ''

buttons = [   ['C', '<-', '%', '/'],
              ['1', '2', '3', '*'],
              ['4', '5', '6', '-'],
              ['7', '8', '9', '+'],
              ['0', '.', '=']  ]

for row_idx, row in enumerate(buttons):
       for col, value in enumerate(row):
           if value == '0':
               Button(window, text=value, bg='#242323', fg= 'white', font=('Comic Sans MS', 11), relief="flat", width=17,
              height=5, command=lambda v=value: button_functionality(v)).grid(row=row_idx + 1, column=col, columnspan=2)
           else:
               if value == '.' or value == '=':
                   Button(window, text=value, bg='#242323', fg= '#248DF0', font=('Comic Sans MS', 11), relief = "flat", width = 8,
                   height = 5, command = lambda v=value: button_functionality(v)).grid(row=row_idx + 1, column=col+1)
               else:
                   if not value.isdigit():
                       Button(window, text=value, bg='#242323', fg='#248DF0', font=('Comic Sans MS', 11), relief="flat",
                              width=8,
                              height=5, command=lambda v=value: button_functionality(v)).grid(row=row_idx + 1,
                                                                                              column=col)
                   else:
                        Button(window, text=value, bg='#242323', fg= 'white', font=('Comic Sans MS', 11), relief="flat", width=8,
                        height=5, command=lambda v=value: button_functionality(v)).grid(row=row_idx + 1, column=col)

window.mainloop()
