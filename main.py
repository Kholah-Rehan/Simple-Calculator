from tkinter import *
import math
var = None
operation_complete = False


# Event handler for button click
def click(event):
    global var, operation_complete
    text = event.widget.cget("text")

    # Check if an operation has been completed
    if operation_complete:
        var.set("")
        operation_complete = False

    if text == "=":
        try:
            # Evaluate expression and set result in Entry widget
            expression = var.get().replace("%", "*0.01")
            result = eval(expression)
            var.set(str(result))
            operation_complete = True  # Operation completed
        except Exception as e:
            var.set("Error")
            operation_complete = True
            print(e)
    elif text == "C":
        # Clear Entry widget
        var.set("")
    elif text == "√":
        try:
            value = float(var.get())
            if value < 0:
                raise ValueError("Cannot calculate square root of a negative number")
            result = math.sqrt(value)
            var.set(str(result))
            operation_complete = True  # Operation completed
        except ValueError as e:
            var.set("Error: " + str(e))
    elif text == "x²":
        try:
            value = float(var.get())
            result = value ** 2
            var.set(str(result))
            operation_complete = True  # Operation completed
        except ValueError:
            var.set("Error")
            operation_complete = True
    elif text == "⌫":
        # Delete the last character from Entry widget
        current_text = var.get()
        var.set(current_text[:-1])
    else:
        # Append clicked button text to Entry widget
        var.set(var.get() + text)


# Create the main application window
root = Tk()
root.geometry("644x580")
root.title("Calculator")

# Create a StringVar to store the text in the Entry widget
var = StringVar()
var.set('')

# Create Entry widget
entry_widget = Entry(root, textvariable=var, font="lucida 40 bold")
entry_widget.pack(fill=X, padx=10, pady=10, ipadx=30)

# Define button layout
button_layout = [
    ("9", "8", "7", "-","⌫"),
    ("6", "5", "4", "+","√"),
    ("3", "2", "1", "*","x²"),
    ( ".", "0", "=", "C","/" )
]

# Create buttons using a loop
for row in button_layout:
    f = Frame(root, bg="grey")
    for text in row:
        b = Button(f, text=text, padx=12, pady=5, font="lucida 35 bold")
        b.pack(side=LEFT, padx=20, pady=10)
        b.bind("<Button-1>", click)
    f.pack()

root.mainloop()








