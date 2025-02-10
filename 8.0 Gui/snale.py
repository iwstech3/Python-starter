import tkinter as tk
import random
import sqlite3

# Database setup

conn = sqlite3.connect("snake_game.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, score INTEGER)")
conn.commit()

def get_high_score():
    cursor.execute("SELECT MAX(score) FROM scores")
    result = cursor.fetchone()[0]
    return result if result is not None else 0

def save_score(score):
    cursor.execute("INSERT INTO scores (score) VALUES (?)", (score,))
    conn.commit()

# Game setup
WIDTH, HEIGHT = 500, 500
GRID_SIZE = 20

def start_game():
    global snake, food, score, direction, running, high_score
    canvas.delete("all")
    snake = [(100, 100), (90, 100), (80, 100)]
    direction = "Right"
    score = 0
    high_score = get_high_score()
    spawn_food()
    update_score()
    running = True
    move_snake()

def spawn_food():
    global food
    x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
    y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
    food = (x, y)
    canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="red", tag="food")

def move_snake():
    global running, score, high_score
    if not running:
        return
    
    head_x, head_y = snake[0]
    if direction == "Up":
        head_y -= GRID_SIZE
    elif direction == "Down":
        head_y += GRID_SIZE
    elif direction == "Left":
        head_x -= GRID_SIZE
    elif direction == "Right":
        head_x += GRID_SIZE
    
    new_head = (head_x, head_y)
    if new_head in snake or head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False
        save_score(score)
        high_score = get_high_score()
        update_score()
        return
    
    snake.insert(0, new_head)
    
    if new_head == food:
        score += 10
        spawn_food()
    else:
        snake.pop()
    
    update_score()
    draw_snake()
    window.after(100, move_snake)

def draw_snake():
    canvas.delete("snake")
    for x, y in snake:
        canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill="green", tag="snake")

def change_direction(new_direction):
    global direction
    opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
    if new_direction != opposite_directions.get(direction, ""):
        direction = new_direction

def update_score():
    score_label.config(text=f"Score: {score}  |  High Score: {high_score}")

# GUI setup
window = tk.Tk()
window.title("Snake Game")

score_label = tk.Label(window, text="Score: 0  |  High Score: 0", font=("Arial", 14))
score_label.pack()

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

window.bind("<Up>", lambda _: change_direction("Up"))
window.bind("<Down>", lambda _: change_direction("Down"))
window.bind("<Left>", lambda _: change_direction("Left"))
window.bind("<Right>", lambda _: change_direction("Right"))

start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()

start_game()
window.mainloop()

conn.close()
