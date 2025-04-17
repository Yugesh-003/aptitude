import tkinter as tk

def submit():
    selected = var.get()
    result_label.config(text=f"You selected: {selected}")
# Main window
root = tk.Tk()
root.title("Single Choice Question")

# Question label
question_label = tk.Label(root, text="Which one is a programming language?")
question_label.pack()

# Variable for Radiobuttons
var = tk.StringVar()
var.set(None)  # No option selected initially

# Radiobuttons
rb1 = tk.Radiobutton(root, text="Option A: Banana", variable=var, value="Banana")
rb2 = tk.Radiobutton(root, text="Option B: Python", variable=var, value="Python")
rb3 = tk.Radiobutton(root, text="Option C: Chair", variable=var, value="Chair")

rb1.pack()
rb2.pack()
rb3.pack()

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack()

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
