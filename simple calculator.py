import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result_label.config(text="Error: Division by zero")
                return
            result = num1 / num2
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Please enter valid numbers!!")


# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Inputs
tk.Label(root, text="Enter first number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation options
tk.Label(root, text="Choose Operation").pack()
operation = tk.StringVar(value="+")
tk.OptionMenu(root, operation, "+", "-", "*", "/").pack()

# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=20)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run app
root.mainloop()

