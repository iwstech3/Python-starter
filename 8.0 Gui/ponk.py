import tkinter as tk
import sqlite3

# Database setup
conn = sqlite3.connect("pong_game.db")
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
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
BALL_SIZE = 20

class PongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pong Game")
        
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        self.paddle1 = self.canvas.create_rectangle(10, HEIGHT//2 - PADDLE_HEIGHT//2, 20, HEIGHT//2 + PADDLE_HEIGHT//2, fill="white")
        self.paddle2 = self.canvas.create_rectangle(WIDTH - 20, HEIGHT//2 - PADDLE_HEIGHT//2, WIDTH - 10, HEIGHT//2 + PADDLE_HEIGHT//2, fill="white")
        self.ball = self.canvas.create_oval(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, WIDTH//2 + BALL_SIZE//2, HEIGHT//2 + BALL_SIZE//2, fill="white")
        
        self.score = 0
        self.high_score = get_high_score()
        self.score_label = tk.Label(master, text=f"Score: {self.score} | High Score: {self.high_score}", font=("Arial", 14), bg="black", fg="white")
        self.score_label.pack()
        
        self.paddle1_speed = 0
        self.paddle2_speed = 0
        self.ball_dx = 4
        self.ball_dy = 4
        
        self.master.bind("<w>", lambda _: self.move_paddle1(-10))
        self.master.bind("<s>", lambda _: self.move_paddle1(10))
        self.master.bind("<Up>", lambda _: self.move_paddle2(-10))
        self.master.bind("<Down>", lambda _: self.move_paddle2(10))
        
        self.run_game()
    
    def move_paddle1(self, dy):
        self.canvas.move(self.paddle1, 0, dy)
    
    def move_paddle2(self, dy):
        self.canvas.move(self.paddle2, 0, dy)
    
    def run_game(self):
        self.move_ball()
        self.master.after(50, self.run_game)
    
    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        paddle1_coords = self.canvas.coords(self.paddle1)
        paddle2_coords = self.canvas.coords(self.paddle2)
        
        if ball_coords[1] <= 0 or ball_coords[3] >= HEIGHT:
            self.ball_dy = -self.ball_dy
        
        if (ball_coords[0] <= paddle1_coords[2] and paddle1_coords[1] < ball_coords[1] < paddle1_coords[3]) or \
           (ball_coords[2] >= paddle2_coords[0] and paddle2_coords[1] < ball_coords[1] < paddle2_coords[3]):
            self.ball_dx = -self.ball_dx
            self.score += 10
            self.update_score()
        
        if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:
            save_score(self.score)
            self.high_score = get_high_score()
            self.update_score()
            self.reset_ball()
            self.score = 0
    
    def update_score(self):
        self.score_label.config(text=f"Score: {self.score} | High Score: {self.high_score}")
    
    def reset_ball(self):
        self.canvas.coords(self.ball, WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, WIDTH//2 + BALL_SIZE//2, HEIGHT//2 + BALL_SIZE//2)
        self.ball_dx = -self.ball_dx

root = tk.Tk()
game = PongGame(root)
root.mainloop()

conn.close()
