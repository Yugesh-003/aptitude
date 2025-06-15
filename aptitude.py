#aptitude game

import random
import tkinter as tk
import json
from tkinter import ttk,messagebox

from pandas import options


submit_btn = None
timer_id = None
choices = None
topic = None
selected_answers = []
selected_options = []
selected_questions = []
no_of_questions = 5

def questionSelection(choices):
    selected_cat = choices.get()
    with open("questions.json","r") as file:
        data = json.load(file)


     #fixed
    if selected_cat == "Ratio and Proportion":
        question_pool = list(data["ratio_and_proportion"])
    elif selected_cat == "Average":
        question_pool = list(data["average"])
    elif selected_cat == "Profit and Loss":
        question_pool = list(data["profit_and_loss"])
    elif selected_cat == "Time and Work":
        question_pool = list(data["time_and_work"])
    elif selected_cat == "Reasoning Skills":
        question_pool = list(data["reasoning_skills"])
    else:
        return
    ##############################################

    randomQues = random.sample(question_pool, no_of_questions)

    for i in randomQues:
        selected_questions.append(i["question"])
        selected_answers.append(i["answer"])
        selected_options.append(i["options"])
        
    print(selected_questions)
    print(selected_options)
    print(selected_answers)


answers = []    
correct_ans = []
score = 0

def submit(user_ans:list):    
    # for entry in user_ans:
    #     entry.config(state="disabled")

    global timer_id

    # Cancel the timer
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
    score = 0 
    ans = []
    
    for entry in user_ans:  #to convert the list (user_ans) of objects into list of strings
        ans.append(entry.get())
        print(entry.get())
    
    for i in range(no_of_questions):
        if selected_answers[i].lower().replace(" ", "") == ans[i]:#correct
            score += 1
            correct_ans[i].config(text="Correct answer!!!")

        else:#wrong
            correct_ans[i].config(text=f"Actual answer : {selected_answers[i]}")
            
    tk.Label(root,text=f"Game over!!! Your total score is {score}/{no_of_questions}",
             font=("Times New Roman", 12), fg="red", bg="#f0f0f0").pack()
    submit_btn.config(text="Restart",command=restart)


def restart():
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None
    for widget in root.winfo_children():
        widget.destroy()

    # Reset everything
    answers.clear()
    correct_ans.clear()
    selected_answers.clear()
    selected_options.clear()
    selected_questions.clear()

    # Restart the game
    setup_ui()

    

def start_timer(t):
    countdown(t)

def countdown(seconds):
    global timer_id
    if seconds > 0:
        minutes = seconds // 60
        secs = seconds % 60
        timer_label.config(text=f"Time Left: {minutes:02d}:{secs:02d}")
        timer_id = root.after(1000, countdown, seconds - 1)
    else:
        timer_label.config(text="Time's up!")
        submit(answers)
        

def game(choices):
    global topic    
    start.pack_forget()
    topic.pack_forget()
    selected_questions.clear()
    selected_answers.clear()

    global submit_btn 
    questionSelection(choices)

    if not selected_questions:
        messagebox.showwarning("Selection Missing", "Please select a difficulty level.")
        for widget in root.winfo_children():
            widget.destroy()

        setup_ui()
        return 
    choices.destroy()
    title.config(text="Answer the following questions..")
    for inx, ques in enumerate(selected_questions):

        tk.Label(root, text=f"{inx + 1}. {ques} ",font=("Times New Roman",14),wraplength=650 ).pack(pady=5)
######################################################################################################        
            
        # Create a StringVar for this question
        var = tk.StringVar()
        var.set(None)  # No option selected initially
        answers.append(var)

            
        # Frame for first row (first two options)
        frame1 = tk.Frame(root)
        frame1.pack()
        tk.Radiobutton(frame1, text=selected_options[inx][0], variable=var, value=selected_options[inx][0]).pack(side="left", padx=10)
        tk.Radiobutton(frame1, text=selected_options[inx][1], variable=var, value=selected_options[inx][1]).pack(side="left", padx=10)

        # Frame for second row (next two options)
        frame2 = tk.Frame(root)
        frame2.pack()
        tk.Radiobutton(frame2, text=selected_options[inx][2], variable=var, value=selected_options[inx][2]).pack(side="left", padx=10)
        tk.Radiobutton(frame2, text=selected_options[inx][3], variable=var, value=selected_options[inx][3]).pack(side="left", padx=10)
                
######################################################################################################
        crt_ans = tk.Label(root,text='')
        crt_ans.pack()
        correct_ans.append(crt_ans)
        
    submit_btn = tk.Button(root, text="Submit", font=("Times New Roman",13),command=lambda : submit(answers))
    submit_btn.pack(pady=5)
    start_timer(300)
   
root = tk.Tk()
root.title("Trivia game")

def setup_ui():
    global title, timer_label,start, topic, choices
    root.geometry("650x780")
    root.configure(bg="#f0f0f0")

    title = tk.Label(root, text="Welcome to the Aptitude Test!", font=("Times New Roman", 18, "bold"))
    title.pack(pady=20)
    
    topic = tk.Label(root, text="Select the topic..", font=("Times New Roman", 12, "bold"))
    topic.pack(pady=20)
    
    choices = ttk.Combobox(root,value = ["Ratio and Proportion","Average","Profit and Loss","Time and Work","Reasoning Skills"])
    choices.pack()
    

    timer_label = tk.Label(root, text="", font=("Times New Roman", 12), fg="red", bg="#f0f0f0")
    timer_label.pack()

    start = tk.Button(root,text="Start",font=("Times New Roman", 18, "bold"), bg="#f9f9f9", fg="#333",command=lambda : game(choices))
    start.pack(pady=20)
    print(choices.get())
    
        
setup_ui()
root.mainloop()
