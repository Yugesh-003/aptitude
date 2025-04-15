import random
import tkinter as tk
import json
from tkinter import ttk,messagebox


root = tk.Tk()
root.title("Aptitude Test")
root.geometry("500x400")
root.config(bg = "#f0f0f0")

choices = None
cat = None

selected_answers = []
selected_questions = []
no_of_questions = 5


def questionSelection(choices):
    selected_cat = choices.get()
    with open("questions.json","r") as file:
        data = json.load(file)

    # fix this once the categories are given
    ##############################################
    if selected_cat == "easy":
        question_pool = list(data["easy"])
    elif selected_cat == "medium":
        question_pool = list(data["medium"])
    elif selected_cat == "hard":
        question_pool = list(data["hard"])
    else:
        return
    ##############################################
    
    randomQues = random.sample(question_pool, no_of_questions)

    for i in randomQues:
        selected_questions.append(i["question"])
        selected_answers.append(i["answer"])
        
    print(selected_questions)
    print(selected_answers)
    
    
def game(choice):
    #to remove all the widgets from the screen
    for widget in root.winfo_children():
        widget.destroy()
    if not selected_questions:
        messagebox.showwarning("Selection Missing", "Please select a cat level.")
        for widget in root.winfo_children():
            widget.destroy()
        setup_ui()
        return 
    
    choices.destroy()
    cat.destroy()
        
    
    title = tk.Label(root, text="Answer the following questions", font=("Times New Roman", 18, "bold"), bg="#f9f9f9", fg="#333")
    title.pack(pady=5)

def setup_ui():
    title = tk.Label(root, text="Aptitude Test", font=("Times New Roman", 18, "bold"), bg="#f9f9f9", fg="#333")
    title.pack(pady=20)
    
    cat = tk.Label(root,text="Choose cat")
    cat.pack()
    choices = ttk.Combobox(root,value = [])  # <---- enter the categories here
    choices.pack()
    

    timer_label = tk.Label(root, text="", font=("Times New Roman", 12), fg="red", bg="#f0f0f0")
    timer_label.pack()

    start = tk.Button(root,text="Start",font=("Times New Roman", 18, "bold"), bg="#f9f9f9", fg="#333",command=lambda : game(choices))
    start.pack(pady=20)
    print(choices.get())
    
setup_ui()
root.mainloop()

    