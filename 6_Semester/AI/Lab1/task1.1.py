import tkinter as tk 
from tkinter import ttk

def calculate_result():
    selected_operation = operation_var.get() 
    x2_entry.configure(state='normal')
    if selected_operation == "AND":
        calculate_logic_function(and_neuron)
    elif selected_operation == "OR":
        calculate_logic_function(or_neuron)
    elif selected_operation == "NOT":
        x2_entry.configure(state='disabled')
        calculate_logic_function(not_neuron)
    elif selected_operation == "XOR":
        calculate_logic_function(xor_neuron)

def calculate_logic_function(logic_function): 
    x1 = float(x1_var.get())
    x1 = round_value(x1)
    if operation_var.get() != "NOT": 
        x2 = float(x2_var.get())
        x2 = round_value(x2)
        result = logic_function(x1, x2)
    else:
        result = logic_function(x1, '') 
    result_var.set(result)

def round_value(value):
    return 1 if value != 0 else 0

def and_neuron(x1, x2): 
    w1, w2 = 1, 1 
    threshold = 1.5
    S = x1 * w1 + x2 * w2
    return 1 if S >= threshold else 0

def or_neuron(x1, x2):
    w1, w2 = 1, 1
    threshold = 0.5
    S = x1 * w1 + x2 * w2
    return 1 if S >= threshold else 0

def not_neuron(x, _):
    w = -1.5
    threshold = -1
    S = x * w
    return 1 if S >= threshold else 0

def xor_neuron(x1, x2):
    w1, w2 = 1, -1
    threshold_1 = 0.5
    S1 = x1 * w1 + x2 * w2
    output_1 = 1 if S1 >= threshold_1 else 0
    
    w3, w4 = -1, 1
    threshold_2 = 0.5
    S2 = x1 * w3 + x2 * w4
    output_2 = 1 if S2 >= threshold_2 else 0

    w5, w6 = 1, 1
    threshold_3 = 0.5
    S3 = output_1 * w5 + output_2 * w6
    return 1 if S3 >= threshold_3 else 0

root = tk.Tk()
root.title("Логічні функції")
x1_var = tk.StringVar()
x2_var = tk.StringVar()
x1_label = ttk.Label(root, text="x1:")
x1_entry = ttk.Entry(root, textvariable=x1_var)
x2_label = ttk.Label(root, text="x2:")
x2_entry = ttk.Entry(root, textvariable=x2_var)
operation_var = tk.StringVar()
operations = ["choice operation", "AND", "OR", "NOT", "XOR"]
operation_label = ttk.Label(root, text="Operation:")
operation_menu = ttk.OptionMenu(root, operation_var, *operations)
operation_var.set(operations[0])
calculate_button = ttk.Button(root, text="Calculate", command=calculate_result)
result_var = tk.StringVar()
result_label = ttk.Label(root, text="Result:")
result_entry = ttk.Entry(root, textvariable=result_var, state="readonly")
x1_label.grid(row=0, column=0, padx=5, pady=5)
x2_label.grid(row=0, column=1, padx=5, pady=5)
x1_entry.grid(row=1, column=0, padx=5, pady=5)
x2_entry.grid(row=1, column=1, padx=5, pady=5)
operation_label.grid(row=2, column=0, padx=5, pady=5)
operation_menu.grid(row=2, column=1, padx=5, pady=5)
calculate_button.grid(row=3, column=1, columnspan=2, pady=10)
result_label.grid(row=4, column=0, padx=5, pady=5)
result_entry.grid(row=4, column=1, padx=5, pady=5)
root.mainloop()
