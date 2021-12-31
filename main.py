# All plot imports
from tkinter import messagebox
from tkinter import *
import tkinter.font as font
from matplotlib import pyplot as plot
from sympy import symbols, parse_expr


# Function to remove every x in function and substitute by the value
def subs_function(value_to_subs, function_of_x):
    x_symbol = symbols('x')
    cast_pol_exp = parse_expr(function_of_x)
    cur_expression = cast_pol_exp.subs(x_symbol, value_to_subs)
    return cur_expression


# Function to check about valid case -> max should be greater than min (e.g.)
# also subs by max and min value then plot the function
def plot_function():
    min_value = int(min_value_entry.get())
    max_value = int(max_value_entry.get())
    function_to_plot = function_entry.get()
    if min_value < max_value:
        subs_function(min_value, function_to_plot)
        subs_function(max_value, function_to_plot)
        plot_it()
        window.mainloop()
    else:
        messagebox.showerror('Limited Error', 'Max value should be greater than min value')


# Function to create scale for (x, y) axis and show the final graph
def plot_it():
    min_value = int(min_value_entry.get())
    max_value = int(min_value_entry.get())
    x_axis = []
    y_axis = []
    for values in range(min_value, max_value + 100):
        x_axis.append(values)

    for values in x_axis:
        y_axis.append(subs_function(values, function_entry.get()))

    x_axis_values = x_axis
    y_axis_values = y_axis
    plot.plot(x_axis_values, y_axis_values)
    plot.xlabel('x-axis')
    plot.ylabel('y-axis')
    plot.show()


window = Tk()

window.title("Function Plotter")
window.geometry("600x400")
frame_tool = Frame(window, bg='white')
frame_tool.pack(fill='x')
myFont = font.Font(family="Calibre", size=15)

window.minsize(300, 300)

# Welcome Message
welcome_msg = Label(window, text='Function Plotter', font=('Helvetica', 16), height=5)
welcome_msg.pack(side=TOP)

min_value_label = Label(text="Min value", font=myFont)
min_value_label.pack()
min_value_label.place(x=100, y=100, height=90, width=100)

# Textbox for min value
min_value_entry = Entry()
min_value_entry.pack()
min_value_entry.place(x=100, y=170, height=35, width=100)

max_value_label = Label(text="Max value", font=myFont)
max_value_label.pack()
max_value_label.place(x=400, y=100, height=90, width=100)

# Textbox for max value
max_value_entry = Entry()
max_value_entry.pack()
max_value_entry.place(x=400, y=170, height=35, width=100)

# Textbox for function to plot
function_entry = Entry()
function_entry.pack()
function_entry.place(x=200, y=230, height=45, width=200)

# Button for add plot action
btn_plot = Button(text="Plot", command=plot_function, font=myFont)
btn_plot.place(x=180, y=300, height=40, width=85)

# Button to exit the program
btn_exit = Button(window, text="Exit!", font=myFont, fg='red', command=window.destroy)
btn_exit.place(x=330, y=300, height=40, width=85)

# show GUI
window.mainloop()
