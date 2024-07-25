import tkinter as tk
import random as rdm

# TODO : the game is won when all the table is green
# TODO : rewrite code repetitions

# const :
CELL_SIZE=50
ROWS=5
COLUMNS=5
SPEED=400 # reaction time of the loop game in millisec (bigger = slower)
BACKGROUND_COLOR_0='#111111'
BACKGROUND_COLOR_1='#111111' # '#000033'
BACKGROUND_COLOR_2='#303030' # '#000066'

class Snake:
    def __init__(self):
        self.body_part = 0
        self.coordinates = []
        self.squares = []
        self.color = '#00FF00'
        initial_coords = [(1,1), (2,1), (3,1)]
        for (x, y) in initial_coords:
            self.add_body_part((x, y))
    
    def add_body_part(self, new_part:tuple[int,int]):
        self.coordinates.insert(0, new_part)
        x, y = new_part
        square = canva.create_rectangle(x*CELL_SIZE,
                                        y*CELL_SIZE,
                                        x*CELL_SIZE+CELL_SIZE,
                                        y*CELL_SIZE+CELL_SIZE,
                                        fill=self.color,
                                        tag='snake')
        self.squares.insert(0, square)
        
class Apple:
    def __init__(self):
        self.coordinates = self.__get_rdm_coord()
        x, y = self.coordinates
        self.color ='#FF0000'
        canva.create_oval(x*CELL_SIZE, 
                          y*CELL_SIZE, 
                          x*CELL_SIZE+CELL_SIZE, 
                          y*CELL_SIZE+CELL_SIZE, 
                          fill=self.color,
                          tag='apple')

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
snake = None
apple = None
current_direction = 'RIGHT'
start_button = None
retry_button = None

# config game :
def start():
    global start_button
    canva.create_text(CELL_SIZE*ROWS / 2, 
                      CELL_SIZE*COLUMNS /2,
                      text="SNAKE",
                      font=('consolas', CELL_SIZE),
                      fill='#00FF00',
                      tag='start')
    start_button = tk.Button(window, text='START', command=init_game)
    canva.create_window(CELL_SIZE*ROWS / 2,
                        CELL_SIZE*COLUMNS /2 + CELL_SIZE,
                        window=start_button)

def init_game():
    global snake, apple, current_direction, retry_button, start_button, score
    canva.delete('game_over', 'start', 'you_won', 'snake', 'apple')
    snake = Snake()
    apple = Apple()
    score = 0
    label.config(text=f'SCORE:{score}')
    current_direction = 'RIGHT'
    if (start_button):
        start_button.destroy()
        start_button = None
    if (retry_button):
        retry_button.destroy()
        retry_button = None
    window.after(SPEED, actions_auto)

def actions_auto():
    x, y = snake.coordinates[0]
    if (current_direction == 'RIGHT'):
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
        snake_deplacement_auto(x, y)
        if check_eating(x, y):
            new_apple()
        if (snake.body_part == ROWS*COLUMNS):
            you_won()
        else:
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

def snake_deplacement_auto(x, y):
    snake.coordinates.pop()
    canva.delete(snake.squares[-1])
    snake.squares.pop()
    snake.add_body_part((x, y))

def check_eating(x:int, y:int):
    x_apple, y_apple = apple.coordinates
    if (x == x_apple and y == y_apple):
        return True
    return False

def new_apple():
    global apple, score, snake
    canva.delete('apple')
    snake.add_body_part(apple.coordinates)
    apple = Apple()
    score += 1
    snake.body_part += 1
    label.config(text=f'SCORE:{score}')

def game_over():
    global retry_button
    canva.delete('snake', 'apple')
    canva.create_text(CELL_SIZE*ROWS / 2, 
                      CELL_SIZE*COLUMNS /2,
                      text="GAME OVER",
                      font=('consolas', CELL_SIZE),
                      fill='#FF0000',
                      tag='game_over')
    retry_button = tk.Button(window, text='RETRY', command=init_game)
    canva.create_window(CELL_SIZE*ROWS / 2, 
                        CELL_SIZE*COLUMNS /2 + CELL_SIZE,
                        window=retry_button)
    
def you_won():
    global retry_button
    canva.create_text(CELL_SIZE*ROWS / 2, 
                      CELL_SIZE*COLUMNS /2,
                      text="YOU WON",
                      font=('consolas', CELL_SIZE),
                      fill='#0000FF',
                      tag='you_won')
    retry_button = tk.Button(window, text='PLAY AGAIN', command=init_game)
    canva.create_window(CELL_SIZE*ROWS / 2,
                        CELL_SIZE*COLUMNS /2 + CELL_SIZE,
                        window=retry_button)

start()

# launch :
window.mainloop()