from tkinter import *

#LEADS TO GAME#    
def ToTheGame():
    import Level1
    window.destroy()

#WINDOW===============================================================================
window = Tk()
window.title("BREAKOUT")
w = Canvas(window, width="1000", height="600", bg="Black")
#TEXT=================================================================================
Level = Label(window, text="Current level:", bg="Black", fg="White", font=("Space Bd BT",15))
LP = Label(window, text="Life points:", bg="Black", fg="White", font=("Space Bd BT",15))
Time = Label(window, text="Time left:", bg="Black", fg="White", font=("Space Bd BT",15))
Logo = Label(window, text="BREAKOUT", bg="Black", fg="White", font=("Space Bd BT",40))
LineControl = Label(window, text="Control", bg="Black", fg="White",font=("Space Bd BT",30))
LineControl2 = Label(window, text='''Press Spacebar Button to release the ball
Press ← Button to move the paddle to the left"
Press → Button to move the paddle to the right''',bg="Black", fg="Yellow", font=("Space Bd BT", 15))
LineInstruction = Label(window, text="Instruction", bg="Black", fg="White", font=("Space Bd BT",30))
LineInstruction1 = Label(window, text="The concept of the game is to break all the bricks with a ball", bg="Black", fg="Green", font=("Space Bd BT",10))
LineInstruction2 = Label(window, text="using the paddle to deflect the ball within the time limit.", bg="Black", fg="Green", font=("Space Bd BT",10))
LineInstruction3 = Label(window, text="You will have 3 live points at the start.", bg="Black", fg="Green", font=("Space Bd BT",10))
LineInstruction4 = Label(window, text="If you run out of life points, it will be game over.", bg="Black", fg="Green", font=("Space Bd BT",10))
LineInstruction5 = Label(window, text="If you fail to destroy all the bricks in time limit it will be game over.", bg="Black", fg="Green", font=("Space Bd BT",10))
LineInstruction6 = Label(window, text="You can begin the game by pressing the spacebar button.", bg="Black", fg="Green", font=("Space Bd BT",10))
w.create_line(0, 100, 1000, 100, fill="White")
#BUTTON================================================================================
B = Button(window, text="Start", bg="White", activebackground="white", font="BOLD", command=ToTheGame)


#MENU==================================================================================
def GameINSTRUCTION():
    import Breakout_Instruction
def GameControl():
    import Breakout_Control

menubar = Menu(window)
#Cascade (pulldown menu)
Help = Menu(window)
Help.add_cascade(label="Instruction", command=GameINSTRUCTION)
Help.add_cascade(label="Controls", command=GameControl)
menubar.add_cascade(label="Help", menu=Help)
#Quit
def quit():
    window.destroy()
menubar.add_command(label="Exit", command=quit)

#DISPLAY===============================================================================
window.config(menu=menubar)
w.pack()
B.pack(fill=BOTH, expand=2)
Level.place(x=10,y=10)
LP.place(x=10,y=50)
Time.place(x=800,y=25)
Logo.place(x=360,y=10)
LineControl.place(x=150,y=150)
LineControl2.place(x=30,y=210)
LineInstruction.place(x=600,y=150) 
LineInstruction1.place(x=550,y=200) 
LineInstruction2.place(x=550,y=220)
LineInstruction3.place(x=550,y=240) 
LineInstruction4.place(x=550,y=260)
LineInstruction5.place(x=550,y=280)
LineInstruction6.place(x=550,y=300)




