from tkinter import*
from random import *
from tkinter import ttk
root = Tk()
root.title('gcloudproject- Lady,Hunter,Tiger')
root.iconbitmap('bips.bmp')
root.geometry("500x600")
root.config(bg="white")
rock = "Lady"
paper = "Hunter"
scissors = "Tiger"
image_list = [rock,paper,scissors]
pick_number = randint(0,2)
image_label = Label(root,text=image_list[pick_number])
image_label.pack(pady=50)
def spin():
    pick_number = randint(0,2)
    image_label.config(text=image_list[pick_number])
    if user_choice.get() == "Lady":
        user_choice_value = 0
    elif user_choice.get()=="Hunter":
        user_choice_value = 1
    elif user_choice.get()=="Tiger":
        user_choice_value = 2
    if user_choice_value == 0:
        if pick_number == 0 :
            win_lose_label.config(text="It is a tie ")
        if pick_number == 1:
            win_lose_label.config(text="lady wins against the hunter ")
        if pick_number == 2:
            win_lose_label.config(text="Tiger eats the lady ")
    if user_choice_value == 1:
        if pick_number == 0 :
            win_lose_label.config(text="lady wins against the hunter")
        if pick_number == 1:
            win_lose_label.config(text="It is a tie ")
        if pick_number == 2:
            win_lose_label.config(text="Hunter shoots the tiger ")
    if user_choice_value == 2:
        if pick_number == 0 :
            win_lose_label.config(text="Tiger eats the lady")
        if pick_number == 1:
            win_lose_label.config(text="Hunter shoots the tiger ")
        if pick_number == 2:
            win_lose_label.config(text="It is a tie")    
user_choice = ttk.Combobox(root,value=("Lady","Hunter","Tiger")) 
user_choice.current(0)
user_choice.pack(pady=20)
win_lose_label= Label(root,text="",font=("helvetica",18))
win_lose_label.pack(pady=50)
spin_button = Button(root,text='Spin',command = spin)
spin_button.pack(pady=20)
root.mainloop()


        