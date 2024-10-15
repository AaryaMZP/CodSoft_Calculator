import tkinter as tk
from tkinter import messagebox, font

def add():
    perform_operation('add')

def subtract():
    perform_operation('subtract')

def multiply():
    perform_operation('multiply')

def divide():
    perform_operation('divide')

def perform_operation(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == 'add':
            result = num1 + num2
            operator = '+'
        elif operation == 'subtract':
            result = num1 - num2
            operator = '-'
        elif operation == 'multiply':
            result = num1 * num2
            operator = '*'
        elif operation == 'divide':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is undefined.")
                return
            result = num1 / num2
            operator = '/'
        else:
            return

        result_label.config(text=f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")
root.config(bg="#282c34")  # Background color

# Set a custom font
custom_font = font.Font(family="Helvetica", size=12)

# Create input fields
entry1 = tk.Entry(root, width=15, font=custom_font, bg="#ffffff")
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root, width=15, font=custom_font, bg="#ffffff")
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create labels
label1 = tk.Label(root, text="First Number:", font=custom_font, bg="#282c34", fg="#ffffff")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Second Number:", font=custom_font, bg="#282c34", fg="#ffffff")
label2.grid(row=1, column=0)

# Create buttons
button_style = {"padx": 20, "pady": 10, "font": custom_font, "bg": "#61afef", "fg": "#ffffff", "borderwidth": 0}

add_button = tk.Button(root, text="+", command=add, **button_style)
add_button.grid(row=2, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="-", command=subtract, **button_style)
subtract_button.grid(row=2, column=1, padx=5, pady=5)

multiply_button = tk.Button(root, text="*", command=multiply, **button_style)
multiply_button.grid(row=2, column=2, padx=5, pady=5)

divide_button = tk.Button(root, text="/", command=divide, **button_style)
divide_button.grid(row=2, column=3, padx=5, pady=5)

# Create result label
result_label = tk.Label(root, text="Result: ", font=custom_font, bg="#282c34", fg="#ffffff")
result_label.grid(row=3, column=0, columnspan=4, pady=10)

# Run the application
root.mainloop()

