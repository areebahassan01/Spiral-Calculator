#requirements gathering
purpose= "A simple calculator performing different functions"
requirements=["numbers","operators","Data Types","statments"]

#Modelling
#design of the calculator
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Create display
        self.display = tk.Entry(self.master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        b = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "=", "C", "+"
        ]

        # Create button grid
        row = 1
        col = 0
        for button in b:
            cmd = lambda x=button: self.button_click(x)
            tk.Button(self.master, text=button, width=7, command=cmd).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    # Button click event
    def click(self, key):
        if key == "C":
            self.display.delete(0, tk.END)
        elif key == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, key)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

#code and testing of the calculator
def calculator():
    while True:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        op = input("Enter an op (+, -, *, /): ")
        if op == "+":
            output = n1 + n2
            print(f"{n1} + {n2} = {output}")
        elif op == "-":
            output = n1 - n2
            print(f"{n1} - {n2} = {output}")
        elif op == "*":
            output = n1 * n2
            print(f"{n1} * {n2} = {output}")
        elif op == "/":
            if n2 == 0:
                print("Error: division by zero")
            else:
                output = n1 / n2
                print(f"{n1} / {n2} = {output}")
        else:
            print("Error: invalid op")
        choice = input("Do you want to perform another calculation? (yes/no) ")
        if choice.lower() != "yes":
            break

calculator()

#Planning
# Risk analysis for calculator in Python

# Step 1: Identify risks
RISKS = [
    {
        "id": 1,
        "description": "Input validation risk (high): The code assumes that the user will always input valid numbers and ops, and does not perform any input validation. This can lead to errors or unexpected outputs if the user inputs non-numeric values or invalid ops."
    },
    {
        "id": 2,
        "description": "Error handling risk (medium): The code uses basic error handling to catch division by zero errors, but does not handle all possible errors that can occur when performing arithmetic operations. This can lead to unexpected outputs or crashes if the user inputs large or small numbers, or if the program encounters floating-point precision issues."
    },
    {
        "id": 3,
        "description": "Usability risk (low): The code is simple and easy to use, but may be less user-friendly for users who are not familiar with Python or programming concepts."
    },
    {
        "id": 4,
        "description": "Maintainability risk (medium): The code is easy to read and understand, but may be difficult to maintain or extend if additional features or functionality are added in the future."
    }
]

# Step 2: Assess risks
for risk in RISKS:
    print(f"Risk {risk['id']}: {risk['description']}")
    severity = input("What is the severity of this risk? (1 = low, 2 = medium, 3 = high): ")
    likelihood = input("What is the likelihood of this risk occurring? (1 = low, 2 = medium, 3 = high): ")
    impact = int(severity) * int(likelihood)
    print(f"Risk impact: {impact}\n")

# Step 3: Mitigate risks
print("Risk mitigation plan:")
for risk in RISKS:
    if risk['id'] == 1:
        print("To mitigate input validation risk, add input validation code to ensure that user input is in the correct format and range.")
    elif risk['id'] == 2:
        print("To mitigate error handling risk, use more advanced techniques or libraries to handle arithmetic operations with greater precision and reliability.")
    elif risk['id'] == 3:
        print("To mitigate usability risk, consider adding more user-friendly features, such as error messages or help text.")
    elif risk['id'] == 4:
        print("To mitigate maintainability risk, follow best practices for code organization and documentation, and consider refactoring the code as needed to improve readability and extensibility.")

