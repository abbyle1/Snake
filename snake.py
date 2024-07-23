import tkinter as tk
import random as rdm

# const :
CELL_SIZE=40
ROWS=10
COLUMNS=10
BACKGROUND_COLOR_1='#111111'
BACKGROUND_COLOR_2='#303030'

class Snake:
    def __init__(self):
        self.body_parts = 3
        self.coordinates = [(1,8), (2,8), (3,8)]
        self.color = '#00FF00'
        for (x, y) in self.coordinates:
            canva.create_rectangle(x*CELL_SIZE, y*CELL_SIZE, x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE, fill=self.color)
    
    def add_body_part(self, new_part:tuple[int,int]):
        self.coordinates.append(new_part)
        self.body_parts += 1
        
class Apple:
    def __init__(self):
        self.coordinates = self.__get_rdm_coord()
        x, y = self.coordinates
        self.color ='#FF0000'
        canva.create_oval(x*CELL_SIZE, y*CELL_SIZE, x*CELL_SIZE+CELL_SIZE, y*CELL_SIZE+CELL_SIZE, fill=self.color)

    @staticmethod
    def __get_rdm_coord():
        while True:
            x = rdm.randint(0, COLUMNS-1)
            y = rdm.randint(0, ROWS-1)
            if (x, y) not in snake.coordinates:
                return (x, y)

# var :
score = 0

# config interface :
window = tk.Tk()
window.title('SNAKE')
window.resizable(width=False, height=False)

    # score :
label = tk.Label(window, text=f'SCORE:{score}', font=('consolas', 20))
label.pack()

    # draughtboard :
canva = tk.Canvas(window, background=BACKGROUND_COLOR_1, height=ROWS*CELL_SIZE, width=COLUMNS*CELL_SIZE)
canva.pack()
for i in range(ROWS):
    for j in range(COLUMNS):
        x0 = j * CELL_SIZE
        y0 = i * CELL_SIZE
        x1 = x0 + CELL_SIZE
        y1 = y0 + CELL_SIZE
        if (i + j) % 2 == 0:
            color = BACKGROUND_COLOR_1
        else:
            color = BACKGROUND_COLOR_2
        canva.create_rectangle(x0, y0, x1, y1, fill=color)

snake = Snake()
apple = Apple()

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