import tkinter as tk
import random as rdm

# const :
CELL_SIZE=10
HEIGHT=40
WIDTH=40
SNAKE_COLOR='#00FF00'
APPLE_COLOR='#FF0000'
BACKGROUND_COLOR_1='#111111'
BACKGROUND_COLOR_2='#303030'

class Snake:
    def __init__(self):
        self.body_parts = 3
        self.position = [(1,1), (1,2), (1,3)]
        
class Apple:
    def __init__(self):
        self.position = (0,0) # TODO randomise

# var :
score = 0
snake = Snake()

# config interface :
window = tk.Tk()
window.title('SNAKE')
window.resizable(width=False, height=False)

    # score :
label = tk.Label(window, text=f'SCORE:{score}', font=('consolas', 20))
label.pack()

    # draughtboard :
canva = tk.Canvas(window, background=BACKGROUND_COLOR_1, height=HEIGHT*CELL_SIZE, width=WIDTH*CELL_SIZE)
canva.pack()
for i in range(0, HEIGHT*CELL_SIZE, WIDTH):
    for j in range(0, WIDTH*CELL_SIZE, HEIGHT):
        if (i/10%8 == j/10%8):
            canva.create_rectangle(i+0, j+0, i+WIDTH, j+HEIGHT, fill=BACKGROUND_COLOR_2)
            canva.pack()

# config game :
def init_game():
    pass

def on_key_press():
    # changer de direction
        # LEFT :    appliquer (x-=1,y)
        # RIGHT :   appliquer (x+=1,y)
        # UP :      appliquer (x,y+=1)
        # DOWN :    appliquer (x,y-=1)
    pass

def check_collisions():
    # si le snake tente de se positionner derrière un mur
    # si le serpend se mange lui-même
    pass

def game_over():
    # afficher le message de game over
    pass

# launch :
window.mainloop()