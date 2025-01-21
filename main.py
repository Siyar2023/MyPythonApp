# Import the tkinter library for creating the graphical user interface (GUI)
import tkinter as tk

# Function to handle button clicks (when a button is pressed, the corresponding value is added to the display)
def button_click(value):
    current = entry.get()  # Get the current value in the display entry
    entry.delete(0, tk.END)  # Clear the display entry
    entry.insert(0, current + value)  # Insert the new value (button clicked value) at the beginning

# Function to clear the display
def clear():
    entry.delete(0, tk.END)  # Delete everything in the display entry

# Function to calculate the result of the mathematical expression entered
def calculate():
    try:
        expression = entry.get()  # Get the expression from the display
        result = eval(expression)  # Use eval() to calculate the result of the expression
        entry.delete(0, tk.END)  # Clear the display
        entry.insert(0, str(result))  # Display the result as a string in the display entry
    except Exception as e:
        entry.delete(0, tk.END)  # If an error occurs (e.g., invalid input), clear the display
        entry.insert(0, "error")  # Display "error" in case of an invalid calculation

# Function to delete the last character from the current input (for backspace functionality)
def delete_last():
    current = entry.get()  # Get the current value in the display
    entry.delete(0, tk.END)  # Clear the display entry
    entry.insert(0, current[:-1])  # Insert the current value without the last character

# Create the main window (the root window)
root = tk.Tk()
root.title("Calculator")  # Set the window title

# Create an entry widget to display the input and output (results)
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)  # Place the entry in the window using grid layout

# List of buttons with their text, position in the grid, and span (if necessary)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),  # Row 1: Buttons 7, 8, 9, division
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),  # Row 2: Buttons 4, 5, 6, multiplication
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),  # Row 3: Buttons 1, 2, 3, subtraction
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),  # Row 4: Buttons 0, ".", clear (C), addition
    ('<', 5, 0), ('=', 5, 1, 3)  # Row 5: Buttons "<" (backspace) and "=" (calculate)
]

# Add buttons to the window using a loop
for (text, row, col, *span) in buttons:
    if text == '=':  # If the button is "=" (calculate button)
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=calculate)
        button.grid(row=row, column=col, columnspan=2, sticky="nsew")  # Merge columns for the "=" button
    elif text == 'C':  # If the button is "C" (clear button)
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=clear)
        button.grid(row=row, column=col, sticky="nsew")  # Place the clear button
    elif text == '<':  # If the button is "<" (backspace button)
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=delete_last)
        button.grid(row=row, column=col, sticky="nsew")  # Place the backspace button
    else:  # For number and operation buttons
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda value=text: button_click(value))
        button.grid(row=row, column=col, sticky="nsew")  # Place the number/operation buttons

# Make the buttons expand over the window space using row and column configurations
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

# Start the main event loop of the application to make the GUI interactive
root.mainloop()
