import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create an Entry widget for the display
display = tk.Entry(root, width=20, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, ipadx=46, ipady=20, padx=5, pady=5)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons and place them in a grid
row, col = 1, 0
buttons = []

for label in button_labels:
    button = tk.Button(root, text=label, width=5, height=2, font=("Arial", 16))
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(button)
    col += 1
    if col > 3:
        col = 0
        row += 1


# Define the button_click function
def button_click(event):
    # Get the current text in the display
    current = display.get()

    # Get the label of the button that was clicked
    button = event.widget
    text = button['text']

    if text == '=':
        try:
            # Evaluate the expression and display the result
            result = eval(current)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            # Handle errors (e.g., invalid syntax or division by zero)
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        # Append the button's text to the current display text
        display.insert(tk.END, text)


# Define the clear function
def clear():
    # Clear the display
    display.delete(0, tk.END)


# Bind the button_click function to the calculator buttons
for button in buttons:
    button.bind("<Button-1>", button_click)

# Create a clear button and bind the clear function
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 16), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Run the main loop
root.mainloop()
