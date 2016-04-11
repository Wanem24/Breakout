from tkinter import*
import random
import time

#Screen Display------------------------------------------------------------------
LEVEL2 = Tk()
LEVEL2.title("BREAKOUT")
LEVEL2.resizable(0, 0)
canvas = Canvas(LEVEL2, bg="Black", width="1000", height="700")
canvas.pack()
LEVEL2.update()
#LEVEL--------------------------------------------------------------------------
Level = Label(LEVEL2, text="Current level: 2", bg="Black", fg="White", font=("Space Bd BT",15))
#LIFE POINTS
LP = Label(LEVEL2, text="Life points:", bg="Black", fg="White", font=("Space Bd BT",15))
#TIME----------------------------------------------------------------------------
Time = Label(LEVEL2, text="Time left:", bg="Black", fg="White", font=("Space Bd BT",15))
#LOGO#--------------------------------------------------------------------------------
Logo = Label(LEVEL2, text="BREAKOUT", bg="Black", fg="White", font=("Space Bd BT",40))
#PACKS#-------------------------------------------------------------------------------
Level.place(x=10,y=10)
LP.place(x=10,y=50)
Time.place(x=800,y=25)
Logo.place(x=360,y=10)
canvas.pack()

#MENU------------------------------------------------------------------------------
def GameINSTRUCTION():
    import Breakout_Instruction
def GameControl():
    import Breakout_Control

menubar = Menu(LEVEL2)
#Cascade (pulldown menu)--------------------------------------------------------------
Help = Menu(LEVEL2)
Help.add_cascade(label="Instruction", command=GameINSTRUCTION)
Help.add_cascade(label="Controls", command=GameControl)
menubar.add_cascade(label="Help", menu=Help)
#Quit---------------------------------------------------------------------------------
def quit():
    LEVEL2.destroy()
menubar.add_command(label="Exit", command=quit)

LEVEL2.config(menu=menubar)
#-------------------------------------------------------------------------------
canvas.create_line(0, 100, 1000, 100, fill="White")
canvas.pack()
#===============================================================================
lost = False
Gameover = False
life = 3 #Number of life in the beginning
Brick_Left = 40 #Number of bricks in the beginning
Time = 170 #Time

#BALL
class Ball:
    def __init__(self, canvas, paddle,
                 #Row 1 bricks
                 brick1,
                 brick2,
                 brick3,
                 brick4,
                 brick5,
                 brick6,
                 brick7,
                 brick8,
                 brick9,
                 brick10,
                 #Row 2, bricks
                 brick11,
                 brick12,
                 brick13,
                 brick14,
                 brick15,
                 brick16,
                 brick17,
                 brick18,
                 brick19,
                 brick20,
                 #Row 3 bricks
                 brick21,
                 brick22,
                 brick23,
                 brick24,
                 brick25,
                 brick26,
                 brick27,
                 brick28,
                 brick29,
                 brick30,
                 #Row 4 bricks
                 brick31,
                 brick32,
                 brick33,
                 brick34,
                 brick35,
                 brick36,
                 brick37,
                 brick38,
                 brick39,
                 brick40):
        self.canvas = canvas
        self.paddle = paddle
        self.brick1 = brick1
        self.brick2 = brick2
        self.brick3 = brick3
        self.brick4 = brick4
        self.brick5 = brick5
        self.brick6 = brick6
        self.brick7 = brick7
        self.brick8 = brick8
        self.brick9 = brick9
        self.brick10 = brick10
        self.brick11 = brick11
        self.brick12 = brick12
        self.brick13 = brick13
        self.brick14 = brick14
        self.brick15 = brick15
        self.brick16 = brick16
        self.brick17 = brick17
        self.brick18 = brick18
        self.brick19 = brick19
        self.brick20 = brick20
        self.brick21 = brick21
        self.brick22 = brick22
        self.brick23 = brick23
        self.brick24 = brick24
        self.brick25 = brick25
        self.brick26 = brick26
        self.brick27 = brick27
        self.brick28 = brick28
        self.brick29 = brick29
        self.brick30 = brick30
        self.brick31 = brick31
        self.brick32 = brick32
        self.brick33 = brick33
        self.brick34 = brick34
        self.brick35 = brick35
        self.brick36 = brick36
        self.brick37 = brick37
        self.brick38 = brick38
        self.brick39 = brick39
        self.brick40  = brick40
        #Creation of the ball
        self.id = canvas.create_oval(10, 10, 25, 25, fill="grey")
        #This is where the ball is placed at the beginning of the game
        self.canvas.move(self.id, 500, 600)
        starts = [-3, -2, -1, 1, 2, 3]
        #Random determines which direction the ball will go off
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.y = -4
                global Time
                Time -= 1
                Countdown()
                if Time == 0:
                    #Shows a text saying gameover
                    game_over()
                    #This delays the time to close the game
                    LEVEL2.after(3000, lambda: LEVEL2.destroy())
                    
    
    def hit_brick1(self, pos):
        brick1_pos = self.canvas.coords(self.brick1.id)
        if len(brick1_pos) != 0:
            if pos[2] >= brick1_pos[0] and pos[0] <= brick1_pos[2]:
                if pos[3] >= brick1_pos[1] and pos[1] <= brick1_pos[3]:
                    self.y = 4
                    canvas.delete(brick1.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick2(self, pos):
        brick2_pos = self.canvas.coords(self.brick2.id)
        if len(brick2_pos) != 0:
            if pos[2] >= brick2_pos[0] and pos[0] <= brick2_pos[2]:
                if pos[3] >= brick2_pos[1] and pos[1] <= brick2_pos[3]:
                    self.y = 4
                    canvas.delete(brick2.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick3(self, pos):
        brick3_pos = self.canvas.coords(self.brick3.id)
        if len(brick3_pos) != 0:
            if pos[2] >= brick3_pos[0] and pos[0] <= brick3_pos[2]:
                if pos[3] >= brick3_pos[1] and pos[1] <= brick3_pos[3]:
                    self.y = 4
                    canvas.delete(brick3.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick4(self, pos):
        brick4_pos = self.canvas.coords(self.brick4.id)
        if len(brick4_pos) != 0:
            if pos[2] >= brick4_pos[0] and pos[0] <= brick4_pos[2]:
                if pos[3] >= brick4_pos[1] and pos[1] <= brick4_pos[3]:
                    self.y = 4
                    canvas.delete(brick4.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick5(self, pos):
        brick5_pos = self.canvas.coords(self.brick5.id)
        if len(brick5_pos) != 0:
            if pos[2] >= brick5_pos[0] and pos[0] <= brick5_pos[2]:
                if pos[3] >= brick5_pos[1] and pos[1] <= brick5_pos[3]:
                    self.y = 4
                    canvas.delete(brick5.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick6(self, pos):
        brick6_pos = self.canvas.coords(self.brick6.id)
        if len(brick6_pos) != 0:
            if pos[2] >= brick6_pos[0] and pos[0] <= brick6_pos[2]:
                if pos[3] >= brick6_pos[1] and pos[1] <= brick6_pos[3]:
                    self.y = 4
                    canvas.delete(brick6.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick7(self, pos):
        brick7_pos = self.canvas.coords(self.brick7.id)
        if len(brick7_pos) != 0:
            if pos[2] >= brick7_pos[0] and pos[0] <= brick7_pos[2]:
                if pos[3] >= brick7_pos[1] and pos[1] <= brick7_pos[3]:
                    self.y = 4
                    canvas.delete(brick7.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick8(self, pos):
        brick8_pos = self.canvas.coords(self.brick8.id)
        if len(brick8_pos) != 0:
            if pos[2] >= brick8_pos[0] and pos[0] <= brick8_pos[2]:
                if pos[3] >= brick8_pos[1] and pos[1] <= brick8_pos[3]:
                    self.y = 4
                    canvas.delete(brick8.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick9(self, pos):
        brick9_pos = self.canvas.coords(self.brick9.id)
        if len(brick9_pos) != 0:
            if pos[2] >= brick9_pos[0] and pos[0] <= brick9_pos[2]:
                if pos[3] >= brick9_pos[1] and pos[1] <= brick9_pos[3]:
                    self.y = 4
                    canvas.delete(brick9.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick10(self, pos):
        brick10_pos = self.canvas.coords(self.brick10.id)
        if len(brick10_pos) != 0:
            if pos[2] >= brick10_pos[0] and pos[0] <= brick10_pos[2]:
                if pos[3] >= brick10_pos[1] and pos[1] <= brick10_pos[3]:
                    self.y = 4
                    canvas.delete(brick10.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick11(self, pos):
        brick11_pos = self.canvas.coords(self.brick11.id)
        if len(brick11_pos) != 0:
            if pos[2] >= brick11_pos[0] and pos[0] <= brick11_pos[2]:
                if pos[3] >= brick11_pos[1] and pos[1] <= brick11_pos[3]:
                    self.y = 4
                    canvas.delete(brick11.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick12(self, pos):
        brick12_pos = self.canvas.coords(self.brick12.id)
        if len(brick12_pos) != 0:
            if pos[2] >= brick12_pos[0] and pos[0] <= brick12_pos[2]:
                if pos[3] >= brick12_pos[1] and pos[1] <= brick12_pos[3]:
                    self.y = 4
                    canvas.delete(brick12.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick13(self, pos):
        brick13_pos = self.canvas.coords(self.brick13.id)
        if len(brick13_pos) != 0:
            if pos[2] >= brick13_pos[0] and pos[0] <= brick13_pos[2]:
                if pos[3] >= brick13_pos[1] and pos[1] <= brick13_pos[3]:
                    self.y = 4
                    canvas.delete(brick13.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick14(self, pos):
        brick14_pos = self.canvas.coords(self.brick14.id)
        if len(brick14_pos) != 0:
            if pos[2] >= brick14_pos[0] and pos[0] <= brick14_pos[2]:
                if pos[3] >= brick14_pos[1] and pos[1] <= brick14_pos[3]:
                    self.y = 4
                    canvas.delete(brick14.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick15(self, pos):
        brick15_pos = self.canvas.coords(self.brick15.id)
        if len(brick15_pos) != 0:
            if pos[2] >= brick15_pos[0] and pos[0] <= brick15_pos[2]:
                if pos[3] >= brick15_pos[1] and pos[1] <= brick15_pos[3]:
                    self.y = 4
                    canvas.delete(brick15.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick16(self, pos):
        brick16_pos = self.canvas.coords(self.brick16.id)
        if len(brick16_pos) != 0:
            if pos[2] >= brick16_pos[0] and pos[0] <= brick16_pos[2]:
                if pos[3] >= brick16_pos[1] and pos[1] <= brick16_pos[3]:
                    self.y = 4
                    canvas.delete(brick16.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick17(self, pos):
        brick17_pos = self.canvas.coords(self.brick17.id)
        if len(brick17_pos) != 0:
            if pos[2] >= brick17_pos[0] and pos[0] <= brick17_pos[2]:
                if pos[3] >= brick17_pos[1] and pos[1] <= brick17_pos[3]:
                    self.y = 4
                    canvas.delete(brick17.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick18(self, pos):
        brick18_pos = self.canvas.coords(self.brick18.id)
        if len(brick18_pos) != 0:
            if pos[2] >= brick18_pos[0] and pos[0] <= brick18_pos[2]:
                if pos[3] >= brick18_pos[1] and pos[1] <= brick18_pos[3]:
                    self.y = 4
                    canvas.delete(brick18.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick19(self, pos):
        brick19_pos = self.canvas.coords(self.brick19.id)
        if len(brick19_pos) != 0:
            if pos[2] >= brick19_pos[0] and pos[0] <= brick19_pos[2]:
                if pos[3] >= brick19_pos[1] and pos[1] <= brick19_pos[3]:
                    self.y = 4
                    canvas.delete(brick19.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick20(self, pos):
        brick20_pos = self.canvas.coords(self.brick20.id)
        if len(brick20_pos) != 0:
            if pos[2] >= brick20_pos[0] and pos[0] <= brick20_pos[2]:
                if pos[3] >= brick20_pos[1] and pos[1] <= brick20_pos[3]:
                    self.y = 4
                    canvas.delete(brick20.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick21(self, pos):
        brick21_pos = self.canvas.coords(self.brick21.id)
        if len(brick21_pos) != 0:
            if pos[2] >= brick21_pos[0] and pos[0] <= brick21_pos[2]:
                if pos[3] >= brick21_pos[1] and pos[1] <= brick21_pos[3]:
                    self.y = 4
                    canvas.delete(brick21.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick22(self, pos):
        brick22_pos = self.canvas.coords(self.brick22.id)
        if len(brick22_pos) != 0:
            if pos[2] >= brick22_pos[0] and pos[0] <= brick22_pos[2]:
                if pos[3] >= brick22_pos[1] and pos[1] <= brick22_pos[3]:
                    self.y = 4
                    canvas.delete(brick22.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick23(self, pos):
        brick23_pos = self.canvas.coords(self.brick23.id)
        if len(brick23_pos) != 0:
            if pos[2] >= brick23_pos[0] and pos[0] <= brick23_pos[2]:
                if pos[3] >= brick23_pos[1] and pos[1] <= brick23_pos[3]:
                    self.y = 4
                    canvas.delete(brick23.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick24(self, pos):
        brick24_pos = self.canvas.coords(self.brick24.id)
        if len(brick24_pos) != 0:
            if pos[2] >= brick24_pos[0] and pos[0] <= brick24_pos[2]:
                if pos[3] >= brick24_pos[1] and pos[1] <= brick24_pos[3]:
                    self.y = 4
                    canvas.delete(brick24.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick25(self, pos):
        brick25_pos = self.canvas.coords(self.brick25.id)
        if len(brick25_pos) != 0:
            if pos[2] >= brick25_pos[0] and pos[0] <= brick25_pos[2]:
                if pos[3] >= brick25_pos[1] and pos[1] <= brick25_pos[3]:
                    self.y = 4
                    canvas.delete(brick25.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick26(self, pos):
        brick26_pos = self.canvas.coords(self.brick26.id)
        if len(brick26_pos) != 0:
            if pos[2] >= brick26_pos[0] and pos[0] <= brick26_pos[2]:
                if pos[3] >= brick26_pos[1] and pos[1] <= brick26_pos[3]:
                    self.y = 4
                    canvas.delete(brick26.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick27(self, pos):
        brick27_pos = self.canvas.coords(self.brick27.id)
        if len(brick27_pos) != 0:
            if pos[2] >= brick27_pos[0] and pos[0] <= brick27_pos[2]:
                if pos[3] >= brick27_pos[1] and pos[1] <= brick27_pos[3]:
                    self.y = 4
                    canvas.delete(brick27.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass


    def hit_brick28(self, pos):
        brick28_pos = self.canvas.coords(self.brick28.id)
        if len(brick28_pos) != 0:
            if pos[2] >= brick28_pos[0] and pos[0] <= brick28_pos[2]:
                if pos[3] >= brick28_pos[1] and pos[1] <= brick28_pos[3]:
                    self.y = 4
                    canvas.delete(brick28.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick29(self, pos):
        brick29_pos = self.canvas.coords(self.brick29.id)
        if len(brick29_pos) != 0:
            if pos[2] >= brick29_pos[0] and pos[0] <= brick29_pos[2]:
                if pos[3] >= brick29_pos[1] and pos[1] <= brick29_pos[3]:
                    self.y = 4
                    canvas.delete(brick29.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick30(self, pos):
        brick30_pos = self.canvas.coords(self.brick30.id)
        if len(brick30_pos) != 0:
            if pos[2] >= brick30_pos[0] and pos[0] <= brick30_pos[2]:
                if pos[3] >= brick30_pos[1] and pos[1] <= brick30_pos[3]:
                    self.y = 4
                    canvas.delete(brick30.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick31(self, pos):
        brick31_pos = self.canvas.coords(self.brick31.id)
        if len(brick31_pos) != 0:
            if pos[2] >= brick31_pos[0] and pos[0] <= brick31_pos[2]:
                if pos[3] >= brick31_pos[1] and pos[1] <= brick31_pos[3]:
                    self.y = 4
                    canvas.delete(brick31.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick32(self, pos):
        brick32_pos = self.canvas.coords(self.brick32.id)
        if len(brick32_pos) != 0:
            if pos[2] >= brick32_pos[0] and pos[0] <= brick32_pos[2]:
                if pos[3] >= brick32_pos[1] and pos[1] <= brick32_pos[3]:
                    self.y = 4
                    canvas.delete(brick32.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick33(self, pos):
        brick33_pos = self.canvas.coords(self.brick33.id)
        if len(brick33_pos) != 0:
            if pos[2] >= brick33_pos[0] and pos[0] <= brick33_pos[2]:
                if pos[3] >= brick33_pos[1] and pos[1] <= brick33_pos[3]:
                    self.y = 4
                    canvas.delete(brick33.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick34(self, pos):
        brick34_pos = self.canvas.coords(self.brick34.id)
        if len(brick34_pos) != 0:
            if pos[2] >= brick34_pos[0] and pos[0] <= brick34_pos[2]:
                if pos[3] >= brick34_pos[1] and pos[1] <= brick34_pos[3]:
                    self.y = 4
                    canvas.delete(brick34.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick35(self, pos):
        brick35_pos = self.canvas.coords(self.brick35.id)
        if len(brick35_pos) != 0:
            if pos[2] >= brick35_pos[0] and pos[0] <= brick35_pos[2]:
                if pos[3] >= brick35_pos[1] and pos[1] <= brick35_pos[3]:
                    self.y = 4
                    canvas.delete(brick35.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick36(self, pos):
        brick36_pos = self.canvas.coords(self.brick36.id)
        if len(brick36_pos) != 0:
            if pos[2] >= brick36_pos[0] and pos[0] <= brick36_pos[2]:
                if pos[3] >= brick36_pos[1] and pos[1] <= brick36_pos[3]:
                    self.y = 4
                    canvas.delete(brick36.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick37(self, pos):
        brick37_pos = self.canvas.coords(self.brick37.id)
        if len(brick37_pos) != 0:
            if pos[2] >= brick37_pos[0] and pos[0] <= brick37_pos[2]:
                if pos[3] >= brick37_pos[1] and pos[1] <= brick37_pos[3]:
                    self.y = 4
                    canvas.delete(brick37.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick38(self, pos):
        brick38_pos = self.canvas.coords(self.brick38.id)
        if len(brick38_pos) != 0:
            if pos[2] >= brick38_pos[0] and pos[0] <= brick38_pos[2]:
                if pos[3] >= brick38_pos[1] and pos[1] <= brick38_pos[3]:
                    self.y = 4
                    canvas.delete(brick38.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass

    def hit_brick39(self, pos):
        brick39_pos = self.canvas.coords(self.brick39.id)
        if len(brick39_pos) != 0:
            if pos[2] >= brick39_pos[0] and pos[0] <= brick39_pos[2]:
                if pos[3] >= brick39_pos[1] and pos[1] <= brick39_pos[3]:
                    self.y = 4
                    canvas.delete(brick39.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass


    def hit_brick40(self, pos):
        brick40_pos = self.canvas.coords(self.brick40.id)
        if len(brick40_pos) != 0:
            if pos[2] >= brick40_pos[0] and pos[0] <= brick40_pos[2]:
                if pos[3] >= brick40_pos[1] and pos[1] <= brick40_pos[3]:
                    self.y = 4
                    canvas.delete(brick40.id)
                    global Brick_Left
                    Brick_Left -= 1
                    bricks()
                    if Brick_Left == 0:
                        #Shows a text saying "You win"
                        you_win()
                        #Delays closing time of the game
                        LEVEL2.after(3000, lambda: LEVEL2.destroy())
                        #Imports next level
                        import LEVEL3
        else:
            pass  
        
    
    def draw(self):
        #co-ordinates of where the ball will bounce off
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #maximum height the ball will bounce up to
        if pos[1] <= 100:
        #how fast the ball will bounce back (height)
            self.y = 4
            global Time
            Time -= 1
            Countdown()
            if Time == 0:
                game_over()
                LEVEL2.after(3000, lambda: LEVEL2.destroy())
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        #if the ball hits the paddle it will bonce back
        if self.hit_paddle(pos) == True:
            self.y = -4
        #if the ball hits the brick1 it will bounce back
        if self.hit_brick1(pos) == True:
            self.y = 4
            canvas.delete(brick1.id)
        #if the ball hits the brick2 it will bounce back
        if self.hit_brick2(pos) == True:
            self.y = 4
            canvas.delete(brick2.id)
        #if the ball hits the brick3 it will bounce back
        if self.hit_brick3(pos) == True:
            self.y = 4
            canvas.delete(brick3.id)
        #if the ball hits the brick4 it will bounce back
        if self.hit_brick4(pos) == True:
            self.y = 4
            canvas.delete(brick4.id)
        #if the ball hits the brick5 it will bounce back
        if self.hit_brick5(pos) == True:
            self.y = 4
            canvas.delete(brick5.id)
        #if the ball hits the brick6 it will bounce back
        if self.hit_brick6(pos) == True:
            self.y = 4
            canvas.delete(brick6.id)
        #if the ball hits the brick7 it will bounce back
        if self.hit_brick7(pos) == True:
            self.y = 4
            canvas.delete(brick7.id)
        #if the ball hits the brick8 it will bounce back
        if self.hit_brick8(pos) == True:
            self.y = 4
            canvas.delete(brick8.id)
        #if the ball hits the brick9 it will bounce back
        if self.hit_brick9(pos) == True:
            self.y = 4
            canvas.delete(brick9.id)
        #if the ball hits the brick10 it will bounce back
        if self.hit_brick10(pos) == True:
            self.y = 4
            canvas.delete(brick10.id)
        #if the ball hits the brick11 it will bounce back
        if self.hit_brick11(pos) == True:
            self.y = 4
            canvas.delete(brick11.id)
        #if the ball hits the brick12 it will bounce back
        if self.hit_brick12(pos) == True:
            self.y = 4
            canvas.delete(brick12.id)
        #if the ball hits the brick13 it will bounce back
        if self.hit_brick13(pos) == True:
            self.y = 4
            canvas.delete(brick13.id)
        #if the ball hits the brick14 it will bounce back
        if self.hit_brick14(pos) == True:
            self.y = 4
            canvas.delete(brick14.id)
        #if the ball hits the brick15 it will bounce back
        if self.hit_brick15(pos) == True:
            self.y = 4
            canvas.delete(brick15.id)
        #if the ball hits the brick16 it will bounce back
        if self.hit_brick16(pos) == True:
            self.y = 4
            canvas.delete(brick16.id)
        #if the ball hits the brick17 it will bounce back
        if self.hit_brick17(pos) == True:
            self.y = 4
            canvas.delete(brick17.id)
        #if the ball hits the brick18 it will bounce back
        if self.hit_brick18(pos) == True:
            self.y = 4
            canvas.delete(brick18.id)
        #if the ball hits the brick19 it will bounce back
        if self.hit_brick19(pos) == True:
            self.y = 4
            canvas.delete(brick19.id)
        #if the ball hits the brick20 it will bounce back
        if self.hit_brick20(pos) == True:
            self.y = 4
            canvas.delete(brick20.id)
        #if the ball hits the brick20 it will bounce back
        if self.hit_brick20(pos) == True:
            self.y = 4
            canvas.delete(brick21.id)
        #if the ball hits the brick20 it will bounce back
        if self.hit_brick21(pos) == True:
            self.y = 4
            canvas.delete(brick21.id)
        #if the ball hits the brick22 it will bounce back
        if self.hit_brick22(pos) == True:
            self.y = 4
            canvas.delete(brick22.id)
        #if the ball hits the brick23 it will bounce back
        if self.hit_brick23(pos) == True:
            self.y = 4
            canvas.delete(brick23.id)
        #if the ball hits the brick24 it will bounce back
        if self.hit_brick24(pos) == True:
            self.y = 4
            canvas.delete(brick24.id)
        #if the ball hits the brick25 it will bounce back
        if self.hit_brick25(pos) == True:
            self.y = 4
            canvas.delete(brick25.id)
        #if the ball hits the brick26 it will bounce back
        if self.hit_brick26(pos) == True:
            self.y = 4
            canvas.delete(brick26.id)
        #if the ball hits the brick27 it will bounce back
        if self.hit_brick27(pos) == True:
            self.y = 4
            canvas.delete(brick27.id)
        #if the ball hits the brick28 it will bounce back
        if self.hit_brick28(pos) == True:
            self.y = 4
            canvas.delete(brick28.id)
        #if the ball hits the brick29 it will bounce back
        if self.hit_brick29(pos) == True:
            self.y = 4
            canvas.delete(brick29.id)
        #if the ball hits the brick30 it will bounce back
        if self.hit_brick30(pos) == True:
            self.y = 4
            canvas.delete(brick30.id)
        #if the ball hits the brick31 it will bounce back
        if self.hit_brick31(pos) == True:
            self.y = 4
            canvas.delete(brick31.id)
        #if the ball hits the brick32 it will bounce back
        if self.hit_brick32(pos) == True:
            self.y = 4
            canvas.delete(brick32.id)
        #if the ball hits the brick33 it will bounce back
        if self.hit_brick33(pos) == True:
            self.y = 4
            canvas.delete(brick33.id)
        #if the ball hits the brick34 it will bounce back
        if self.hit_brick34(pos) == True:
            self.y = 4
            canvas.delete(brick34.id)
        #if the ball hits the brick35 it will bounce back
        if self.hit_brick35(pos) == True:
            self.y = 4
            canvas.delete(brick35.id)
        #if the ball hits the brick36 it will bounce back
        if self.hit_brick36(pos) == True:
            self.y = 4
            canvas.delete(brick36.id)
        #if the ball hits the brick37 it will bounce back
        if self.hit_brick37(pos) == True:
            self.y = 4
            canvas.delete(brick37.id)
        #if the ball hits the brick38 it will bounce back
        if self.hit_brick38(pos) == True:
            self.y = 4
            canvas.delete(brick38.id)
        #if the ball hits the brick39 it will bounce back
        if self.hit_brick39(pos) == True:
            self.y = 4
            canvas.delete(brick39.id)
        #if the ball hits the brick40 it will bounce back
        if self.hit_brick40(pos) == True:
            self.y = 4
            canvas.delete(brick40.id)
        #maximum width the ball will bounce up to
        if pos[0] <= 0:
        #how fast the ball will bounce back (width)
            self.x = 4
            Time -= 1
            Countdown()
            if Time == 0:
                game_over()
                #This delays the time to close the game
                LEVEL2.after(3000, lambda: LEVEL2.destroy())
        if pos[2] >= self.canvas_width:
            self.x = -4
            Time -= 1
            Countdown()
            if Time == 0:
                game_over()
                #This delays the time to close the game
                LEVEL2.after(3000, lambda: LEVEL2.destroy())

        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            global lost
            lost = True
            global life
            life -= 1
            lives()
        if life == 0:
            #Shows gameover sign
            game_over()
            #This delays the time to close the game
            LEVEL2.after(3000, lambda: LEVEL2.destroy())
        

#PADDLE
class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
            #creation of the paddle
        self.id = canvas.create_rectangle(200, 700, 430, 386, fill="red")
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        canvas.bind_all("<space>", start_game)
        
   
    #PADDLE MOVEMENT
    def turn_left(self, evt):
        self.x = -3
            
    def turn_right(self, evt):
        self.x = 3

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
        global gameover
        if Gameover == False:
            self.canvas.after(10,self.draw)

class Brick1:
    def __init__(self):
        self.id = canvas.create_rectangle(0, 120, 100, 150, fill="Blue")
    def draw(self):
        pass

class Brick2:
    def __init__(self):
        self.id = canvas.create_rectangle(100, 120, 200, 150, fill="Blue")
    def draw(self):
        pass

class Brick3:
    def __init__(self):
        self.id = canvas.create_rectangle(200, 120, 300, 150, fill="Blue")
    def draw(self):
        pass

class Brick4:
    def __init__(self):
        self.id = canvas.create_rectangle(300, 120, 400, 150, fill="Blue")
    def draw(self):
        pass

class Brick5:
    def __init__(self):
        self.id = canvas.create_rectangle(400, 120, 500, 150, fill="Blue")
    def draw(self):
        pass

class Brick6:
    def __init__(self):
        self.id = canvas.create_rectangle(500, 120, 600, 150, fill="Blue")
    def draw(self):
        pass

class Brick7:
    def __init__(self):
        self.id = canvas.create_rectangle(600, 120, 700, 150, fill="Blue")
    def draw(self):
        pass

class Brick8:
    def __init__(self):
        self.id = canvas.create_rectangle(700, 120, 800, 150, fill="Blue")
    def draw(self):
        pass

class Brick9:
    def __init__(self):
        self.id = canvas.create_rectangle(800, 120, 900, 150, fill="Blue")
    def draw(self):
        pass

class Brick10:
    def __init__(self):
        self.id = canvas.create_rectangle(900, 120, 1000, 150, fill="Blue")
    def draw(self):
        pass

class Brick11:
    def __init__(self):
        self.id = canvas.create_rectangle(0, 150, 100, 180, fill="Blue") 
    def draw(self):
        pass

class Brick12:
    def __init__(self):
        self.id = canvas.create_rectangle(100, 150, 200, 180, fill="White") 
    def draw(self):
        pass

class Brick13:
    def __init__(self):
        self.id = canvas.create_rectangle(200, 150, 300, 180, fill="WHITE") 
    def draw(self):
        pass

class Brick14:
    def __init__(self):
        self.id = canvas.create_rectangle(300, 150, 400, 180, fill="White") 
    def draw(self):
        pass

class Brick15:
    def __init__(self):
        self.id = canvas.create_rectangle(400, 150, 500, 180, fill="White") 
    def draw(self):
        pass

class Brick16:
    def __init__(self):
        self.id = canvas.create_rectangle(500, 150, 600, 180, fill="White") 
    def draw(self):
        pass

class Brick17:
    def __init__(self):
        self.id = canvas.create_rectangle(600, 150, 700, 180, fill="White") 
    def draw(self):
        pass

class Brick18:
    def __init__(self):
        self.id = canvas.create_rectangle(700, 150, 800, 180, fill="White") 
    def draw(self):
        pass

class Brick19:
    def __init__(self):
        self.id = canvas.create_rectangle(800, 150, 900, 180, fill="White") 
    def draw(self):
        pass

class Brick20:
    def __init__(self):
        self.id = canvas.create_rectangle(900, 150, 1000, 180, fill="Blue") 
    def draw(self):
        pass

class Brick21:
    def __init__(self):
        self.id = canvas.create_rectangle(0, 180, 100, 210, fill="Blue") 
    def draw(self):
        pass

class Brick22:
    def __init__(self):
        self.id = canvas.create_rectangle(100, 180, 200, 210, fill="Red") 
    def draw(self):
        pass

class Brick23:
    def __init__(self):
        self.id = canvas.create_rectangle(200, 180, 300, 210, fill="Red") 
    def draw(self):
        pass

class Brick24:
    def __init__(self):
        self.id = canvas.create_rectangle(300, 180, 400, 210, fill="Red") 
    def draw(self):
        pass

class Brick25:
    def __init__(self):
        self.id = canvas.create_rectangle(400, 180, 500, 210, fill="Red") 
    def draw(self):
        pass

class Brick26:
    def __init__(self):
        self.id = canvas.create_rectangle(500, 180, 600, 210, fill="Red") 
    def draw(self):
        pass

class Brick27:
    def __init__(self):
        self.id = canvas.create_rectangle(600, 180, 700, 210, fill="Red") 
    def draw(self):
        pass

class Brick28:
    def __init__(self):
        self.id = canvas.create_rectangle(700, 180, 800, 210, fill="Red") 
    def draw(self):
        pass

class Brick29:
    def __init__(self):
        self.id = canvas.create_rectangle(800, 180, 900, 210, fill="Red") 
    def draw(self):
        pass

class Brick30:
    def __init__(self):
        self.id = canvas.create_rectangle(900, 180, 1000, 210, fill="Blue") 
    def draw(self):
        pass
class Brick31:
    def __init__(self):
        self.id = canvas.create_rectangle(0, 210, 100, 240, fill="Blue")
    def draw(self):
        pass

class Brick32:
    def __init__(self):
        self.id = canvas.create_rectangle(100, 210, 200, 240, fill="Blue")
    def draw(self):
        pass

class Brick33:
    def __init__(self):
        self.id = canvas.create_rectangle(200, 210, 300, 240, fill="Blue")
    def draw(self):
        pass

class Brick34:
    def __init__(self):
        self.id = canvas.create_rectangle(300, 210, 400, 240, fill="Blue")
    def draw(self):
        pass

class Brick35:
    def __init__(self):
        self.id = canvas.create_rectangle(400, 210, 500, 240, fill="Blue")
    def draw(self):
        pass

class Brick36:
    def __init__(self):
        self.id = canvas.create_rectangle(500, 210, 600, 240, fill="Blue")
    def draw(self):
        pass

class Brick37:
    def __init__(self):
        self.id = canvas.create_rectangle(600, 210, 700, 240, fill="Blue")
    def draw(self):
        pass

class Brick38:
    def __init__(self):
        self.id = canvas.create_rectangle(700, 210, 800, 240, fill="Blue")
    def draw(self):
        pass

class Brick39:
    def __init__(self):
        self.id = canvas.create_rectangle(800, 210, 900, 240, fill="Blue")
    def draw(self):
        pass

class Brick40:
    def __init__(self):
        self.id = canvas.create_rectangle(900, 210, 1000, 240, fill="Blue")
    def draw(self):
        pass
    
def start_game(event):
    global lost, ball
    if lost == True:
        ball = Ball(canvas, paddle,
                    brick1,
                    brick2,
                    brick3,
                    brick4,
                    brick5,
                    brick6,
                    brick7,
                    brick8,
                    brick9,
                    brick10,
                    brick11,
                    brick12,
                    brick13,
                    brick14,
                    brick15,
                    brick16,
                    brick17,
                    brick18,
                    brick19,
                    brick20,
                    brick21,
                    brick22,
                    brick23,
                    brick24,
                    brick25,
                    brick26,
                    brick27,
                    brick28,
                    brick29,
                    brick30,
                    brick31,
                    brick32,
                    brick33,
                    brick34,
                    brick35,
                    brick36,
                    brick37,
                    brick38,
                    brick39,
                    brick40)
   
    ball.draw()
    paddle.draw()
    #Row 1 bricks
    brick1.draw()
    brick2.draw()
    brick3.draw()
    brick4.draw()
    brick5.draw()
    brick6.draw()
    brick7.draw()
    brick8.draw()
    brick9.draw()
    brick10.draw()
    brick11.draw()
    brick12.draw()
    brick13.draw()
    brick14.draw()
    brick15.draw()
    brick16.draw()
    brick17.draw()
    brick18.draw()
    brick19.draw()
    brick20.draw()
    brick21.draw()
    brick22.draw()
    brick23.draw()
    brick24.draw()
    brick25.draw()
    brick26.draw()
    brick27.draw()
    brick28.draw()
    brick29.draw()
    brick30.draw()
    brick31.draw()
    brick32.draw()
    brick33.draw()
    brick34.draw()
    brick35.draw()
    brick36.draw()
    brick37.draw()
    brick38.draw()
    brick39.draw()
    brick40.draw()
    lives()
    bricks()

def lives():
    canvas.itemconfig(life_now, text=" " + str(life))

def bricks():
    canvas.itemconfig(Number_of_bricks_now, text=" " + str(Brick_Left))
    
def game_over():
    canvas.itemconfig(game, text="Game over!")

def you_win():
    canvas.itemconfig(finishgame, text="You win!")

def Countdown():
    canvas.itemconfig(time_now, text=" " + str(Time))
  
paddle = Paddle(canvas)
#Row1 bricks
brick1 = Brick1()
brick2 = Brick2()
brick3 = Brick3()
brick4 = Brick4()
brick5 = Brick5()
brick6 = Brick6()
brick7 = Brick7()
brick8 = Brick8()
brick9 = Brick9()
brick10 = Brick10()
#Row2 Bricks
brick11 = Brick11()
brick12 = Brick12()
brick13 = Brick13()
brick14 = Brick14()
brick15 = Brick15()
brick16 = Brick16()
brick17 = Brick17()
brick18 = Brick18()
brick19 = Brick19()
brick20 = Brick20()
#Row3 bricks
brick21 = Brick21()
brick22 = Brick22()
brick23 = Brick23()
brick24 = Brick24()
brick25 = Brick25()
brick26 = Brick26()
brick27 = Brick27()
brick28 = Brick28()
brick29 = Brick29()
brick30 = Brick30()
#Row4 bricks
brick31 = Brick31()
brick32 = Brick32()
brick33 = Brick33()
brick34 = Brick34()
brick35 = Brick35()
brick36 = Brick36()
brick37 = Brick37()
brick38 = Brick38()
brick39 = Brick39()
brick40 = Brick40()

ball = Ball(canvas, paddle,
            brick1,
            brick2,
            brick3,
            brick4,
            brick5,
            brick6,
            brick7,
            brick8,
            brick9,
            brick10,
            brick11,
            brick12,
            brick13,
            brick14,
            brick15,
            brick16,
            brick17,
            brick18,
            brick19,
            brick20,
            brick21,
            brick22,
            brick23,
            brick24,
            brick25,
            brick26,
            brick27,
            brick28,
            brick29,
            brick30,
            brick31,
            brick32,
            brick33,
            brick34,
            brick35,
            brick36,
            brick37,
            brick38,
            brick39,
            brick40)

game = canvas.create_text(500, 300, text=" ", fill="White", font=("Space Bd BT", 100))
finishgame = canvas.create_text(500, 300, text=" ", fill="White", font=("Space Bd BT", 100))
life_now = canvas.create_text(120, 65, text=" " + str(life), fill = "White", font=("Space Bd BT", 16))
Number_of_bricks_now = canvas.create_text(800, 65, text=" " + str(Brick_Left))
time_now = canvas.create_text(910, 40, text=" " + str(Time), fill = "White", font=("Space Bd BT", 16))


LEVEL2.mainloop()

#=========================================================================================
