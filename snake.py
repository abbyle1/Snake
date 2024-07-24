import tkinter as tk
import random as rdm

# const :
CELL_SIZE=40
ROWS=10
COLUMNS=10
SPEED=500 # reaction time of the loop game in millisec (bigger = slower)
BACKGROUND_COLOR_0='#111111'
BACKGROUND_COLOR_1='#111111' # '#000033'
BACKGROUND_COLOR_2='#303030' # '#000066'

class Snake:
    def __init__(self):
        self.body_parts = 3
        self.coordinates = [(3,8), (2,8), (1,8)]
        self.squares = []
        self.color = '#00FF00'
        for (x, y) in self.coordinates:
            square = canva.create_rectangle(x*CELL_SIZE, 
                                            y*CELL_SIZE, 
                                            x*CELL_SIZE+CELL_SIZE, 
                                            y*CELL_SIZE+CELL_SIZE, 
                                            fill=self.color)
            self.squares.append(square)
    
    def add_body_part(self, new_part:tuple[int,int]):
        self.coordinates.append(new_part)
        self.body_parts += 1
        
class Apple:
    def __init__(self):
        self.coordinates = self.__get_rdm_coord()
        x, y = self.coordinates
        self.color ='#FF0000'
        canva.create_oval(x*CELL_SIZE, 
                          y*CELL_SIZE, 
                          x*CELL_SIZE+CELL_SIZE, 
                          y*CELL_SIZE+CELL_SIZE, 
                          fill=self.color)

    @staticmethod
    def __get_rdm_coord():
        while True:
            x = rdm.randint(0, COLUMNS-1)
            y = rdm.randint(0, ROWS-1)
            if (x, y) not in snake.coordinates:
                return (x, y)

# config interface :
window = tk.Tk()
window.title('SNAKE')
window.resizable(width=False, height=False)

    # score :
score = 0
label = tk.Label(window, text=f'SCORE:{score}', font=('consolas', 20))
label.pack()

    # draughtboard :
canva = tk.Canvas(window, 
                  background=BACKGROUND_COLOR_0,
                  height=ROWS*CELL_SIZE-1, 
                  width=COLUMNS*CELL_SIZE-1)
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
    
    # commands :
window.bind('<Left>', lambda event : on_key_press('LEFT'))
window.bind('<Right>', lambda event : on_key_press('RIGHT'))
window.bind('<Up>', lambda event : on_key_press('UP'))
window.bind('<Down>', lambda event : on_key_press('DOWN'))

# var :
snake = Snake()
apple = Apple()
current_direction = 'RIGHT'

# config game :
def init_game():
    # TODO message de start
    # canva.create_text(text='START?', font=('consolas', 20))
    window.after(SPEED, actions_auto)

def actions_auto():
    x, y = snake.coordinates[0]
    if (current_direction == 'RIGHT'): # XXX add a local var to optimize
        x += 1
    elif (current_direction == 'LEFT'):
        x -= 1
    elif (current_direction == 'UP'):
        y -= 1
    elif (current_direction == 'DOWN'):
        y += 1
    if check_collisions(x, y):
        game_over()
    else:
        snake.coordinates.pop()
        canva.delete(snake.squares[-1])
        snake.squares.pop()
        snake.coordinates.insert(0, (x, y))
        snake.squares.insert(0, canva.create_rectangle(x*CELL_SIZE, 
                                                       y*CELL_SIZE, 
                                                       x*CELL_SIZE+CELL_SIZE, 
                                                       y*CELL_SIZE+CELL_SIZE, 
                                                       fill=snake.color))
        if check_eating(x, y):
            new_apple()
        window.after(SPEED, actions_auto)

def on_key_press(new_direction:str):
    # FIXME possibilité de revenir de faire un move interdit si on presse rapidement 2 touches
    global current_direction # to avoid this error: UnboundLocalError: local variable 'current_direction' referenced before assignment
    if (current_direction == 'RIGHT' and new_direction == 'LEFT') or \
       (current_direction == 'LEFT' and new_direction == 'RIGHT') or \
       (current_direction == 'UP' and new_direction == 'DOWN') or \
       (current_direction == 'DOWN' and new_direction == 'UP'):
        pass
    else:
        current_direction = new_direction

def check_collisions(x:int, y:int):
    if (x < 0 or x > COLUMNS-1 or y < 0 or y > ROWS-1): # wall
        return True
    if (x, y) in snake.coordinates: # eat himself
        return True
    return False

def check_eating(x:int, y:int):
    x_apple, y_apple = apple.coordinates
    if (x == x_apple and y == y_apple):
        return True
    return False

def new_apple():
    # TODO
    print('mangé')
    # suppression de l'apple
    # génération d'une nouvelle apple
    # + 1 membre au snake
    # + 1 au score
    pass

def game_over():
    canva.delete(tk.ALL)
    # TODO game over message
    # TODO retry button

init_game()

# launch :
window.mainloop()