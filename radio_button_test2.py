import tkinter as tk

root = tk.Tk()
root.title("2 Radio Buttons Per Row")

# Create a variable to store the selected option
selected_option = tk.StringVar(value="")

# Sample options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Loop to create radio buttons in 2 columns
for index, option in enumerate(options):
    row = index // 2
    col = index % 2
    tk.Radiobutton(root, text=option, variable=selected_option, value=option).grid(row=row, column=col, padx=10, pady=5)

root.mainloop()
