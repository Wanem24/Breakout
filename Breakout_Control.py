from tkinter import*

window = Tk()
window.title("Breakout Controls")
w = Canvas(window, bg = "BLACK", width="1000", height="600")
Title = Label(window, text="Breakout: Controls", bg="Black", fg="White", font=("Space Bd BT",40))
LineControl2 = Label(window, text="Press Spacebar Button to release the ball", bg="Black", fg="Yellow", font=("Space Bd BT",20))
LineControl3 = Label(window, text="Press ← Button to move the paddle to the left", bg="Black", fg="Yellow", font=("Space Bd BT",20))
LineControl4 = Label(window, text="Press → Button to move the paddle to the right", bg="Black", fg="Yellow", font=("Space Bd BT",20))

w.pack()
Title.place(x=250,y=10) 
LineControl2.place(x=150,y=100) 
LineControl3.place(x=150,y=140)
LineControl4.place(x=150,y=180) 
