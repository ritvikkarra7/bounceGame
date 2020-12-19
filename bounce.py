from tkinter import *
import random as r
import time

class Ball:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 35, 35, fill=color)
        self.canvas.move(self.id, 245, 300)
        self.xdirection = -1
        self.ydirection = -1

    def draw(self):
        if self.canvas.coords(self.id)[1] < 0:
            self.ydirection = 1
        elif self.canvas.coords(self.id)[3] > 400:
            self.ydirection = -1
        if self.canvas.coords(self.id)[0] < 0:
            self.xdirection = 1
        elif self.canvas.coords(self.id)[2] > 500:
            self.xdirection = -1
        if contact(self,paddle):
            self.ydirection = -1

        self.canvas.move(self.id, self.xdirection, self.ydirection)

    def reset(self):
        self.canvas.move(self.id,0,-self.canvas.coords(self.id)[1])

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(200,380,300,400, fill=color)
        self.canvas.bind_all('<KeyPress-Left>', self.move)
        self.canvas.bind_all('<KeyPress-Right>', self.move)
        self.direction = 0

    def move(self, event):
        if event.keysym == 'Left':
            self.direction = -6
        elif event.keysym == 'Right':
            self.direction = 6

    def draw(self):
        #if canvas.coords(self.id)[2] != 500 or canvas.coords(self.id)[0] != 0:
        self.canvas.move(self.id,self.direction,0)
        self.direction = 0


def contact(Ball, Paddle) -> bool:
    if canvas.coords(Paddle.id)[1] == canvas.coords(Ball.id)[3] and \
            canvas.coords(Ball.id)[2] > canvas.coords(Paddle.id)[0] and \
            canvas.coords(Ball.id)[0] <= canvas.coords(Paddle.id)[2]:
        return True
    return False

class GameOver:

    def touching(self,Ball):
        if canvas.coords(Ball.id)[3] == 400:
            return True
        return False

    def __init__(self,canvas):
        self.canvas = canvas
        self.id = canvas.create_text(250, 200, text='')

    def show(self):
        self.canvas.itemconfig(self.id,text ="GAME OVER", fill='red',font=('Courier',40))

    def reset(self):
        self.canvas.itemconfig(self.id,text ="")


class Score:
    def __init__(self,canvas):
        self.canvas = canvas
        self.maxScore = 0
        self.currentScore = 0
        self.id1 = canvas.create_text(50,40, text='Max Score: ' + str(self.maxScore))
        self.id2 = canvas.create_text(50,50,text='Current Score: ' + str(self.currentScore))

    def update(self, Ball, Paddle):
        if contact(Ball, Paddle):
            self.currentScore += 1
            self.canvas.itemconfig(self.id2, text = 'Current Score: ' + str(self.currentScore))
        if gameOver.touching(Ball):
            if self.currentScore > self.maxScore:
                self.canvas.itemconfig(self.id1, text='Max Score: ' + str(self.currentScore))

    def reset(self):
        self.currentScore = 0
        self.canvas.itemconfig(self.id2, text='Current Score: ' + str(self.currentScore))

tk = Tk()
tk.title("Bounce")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
tk.update()
ball1 = Ball(canvas, 'red')
# ball2 = Ball(canvas,'green')
paddle = Paddle(canvas,'blue')
score = Score(canvas)
gameOver = GameOver(canvas)
def restart():
    score.reset()
    ball1.reset()
    gameOver.reset()

btn = Button(tk, text="Restart", command=restart)
btn.pack()
canvas.pack()

while 1:
    if gameOver.touching(ball1):
        if score.currentScore > score.maxScore:
            score.maxScore = score.currentScore
        gameOver.show()
    else:
        ball1.draw()
        paddle.draw()
        score.update(ball1,paddle)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.005)
