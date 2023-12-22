import turtle


# Pantalla
wn = turtle.Screen()
wn.title("Atari Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Cargar formas
wn.addshape("boton.gif")
wn.addshape("boton1.gif")
wn.addshape("pong.gif")
wn.addshape("jugador1.gif")
wn.addshape("jugador2.gif")

# Atari logo
logo = turtle.Turtle()
logo.shape("pong.gif")
logo.penup()
logo.goto(0, 150)

# Botón
start = turtle.Turtle()
start.shape("boton.gif")
start.penup()
start.goto(0, 0)


# jugador 1
jugador1 = turtle.Turtle()
jugador1.shape("jugador1.gif")
jugador1.penup()
jugador1.goto(0, 0)
jugador1.shapesize(stretch_wid=2, stretch_len=6)
jugador1.hideturtle()

# jugador 2
jugador2 = turtle.Turtle()
jugador2.shape("jugador2.gif")
jugador2.penup()
jugador2.goto(0, -75)
jugador2.hideturtle()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
paddle_a.hideturtle()

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b.hideturtle()

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2
ball.hideturtle()

# Score
score_a = 0
score_b = 0

# Pen
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.goto(0, 220)
score.hideturtle()

# Variables to track game state
game_started = False
game_started1 = False

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def close_window():
    try:
        wn.bye()
    except turtle.Terminator:
        pass
def start_menu():
  #boton wirting
  start_message = turtle.Turtle()
  start_message.goto(0,-150)
  start_message.color("white")
  start_message.hideturtle()
  start_message.write("Press Space to Start", align="center", font=("Courier", 24, "normal"))
  def on_button_press():
    start.shape("boton1.gif")

  def on_button_release():
    start.shape("boton.gif")
    start.hideturtle()
    start_message.reset()
    logo.hideturtle()
    jugador1.showturtle()
    jugador2.showturtle()
   

  def on_click(x, y):
    global game_started
    global game_started1
    if on_button_release:
      if -109 <= x <= 102 and -10 <= y <= 25:
         print("game for 1")
         jugador1.hideturtle()
         jugador2.hideturtle()
         paddle_a.showturtle()
         paddle_b.showturtle()
         ball.showturtle()
         game_started1=True
         game_for_1()
      elif -110<= x <=104 and -95 <= y <= -57:
         print("game for 2")
         jugador1.hideturtle()
         jugador2.hideturtle()
         paddle_a.showturtle()
         paddle_b.showturtle()
         ball.showturtle()
         game_started=True
         game_for_2()
  wn.listen()
  wn.onkeypress(on_button_press, "space")
  wn.onkeyrelease(on_button_release, "space")
  wn.onscreenclick(on_click)

start_menu()

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(close_window, "Escape")


# Functions for 2 players 
def game_for_2():
    global game_started, score_a, score_b
    while game_started:
        try:
            wn.update()
        except turtle.Terminator:
            break

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        # Top and bottom
        if ball.ycor() > 290:
            ball.color("blue")
            ball.sety(290)
            ball.dy *= -1

        elif ball.ycor() < -290:
            ball.color("red")
            ball.sety(-290)
            ball.dy *= -1

        # Left and right
        if ball.xcor() > 350:
            score_a += 1
            if score_a == 5:
                reset_game()
            else:
             score.clear()
             score.write(" {}     {}".format(score_a, score_b), align="center", font=("Courier", 50, "normal"))
             ball.goto(0, 0)
             ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            if score_b == 5:
                reset_game()
            else:
             score.clear()
             score.write(" {}     {}".format(score_a, score_b), align="center", font=("Courier", 50, "normal"))
             ball.goto(0, 0)
             ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1

        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1

# Functions for 1 players 
def game_for_1():
    global game_started1, score_a, score_b
    while game_started1:
        try:
            wn.update()
        except turtle.Terminator:
            break

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        # Top and bottom
        if ball.ycor() > 290:
            ball.color("blue")
            ball.sety(290)
            ball.dy *= -1

        elif ball.ycor() < -290:
            ball.color("red")
            ball.sety(-290)
            ball.dy *= -1

        # Left and right
        if ball.xcor() > 350:
            score_a += 1
            if score_a == 5:
                reset_game()
            else:
               score.clear()
               score.write(" {}     {}".format(score_a, score_b), align="center", font=("Courier", 50, "normal"))
               ball.goto(0, 0)
               ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            if score_b == 5:
                reset_game()
            else:
               score.clear()
               score.write(" {}     {}".format(score_a, score_b), align="center", font=("Courier", 50, "normal"))
               ball.goto(0, 0)
               ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1

        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
        # AI-controlled paddle 
        if paddle_b.ycor() < ball.ycor():
            paddle_b.sety(paddle_b.ycor() + 0.12)

        elif paddle_b.ycor() > ball.ycor():
            paddle_b.sety(paddle_b.ycor() -0.12)
def reset_game():
    global game_started, game_started1, score_a, score_b
    game_started = False
    game_started1 = False
    score_a = 0
    score_b = 0
    start_menu()
    paddle_a.hideturtle()
    paddle_b.hideturtle()
    ball.hideturtle()
    start.showturtle()
    logo.showturtle()
    score.clear()
    
    

# Main loop
while True:
    try:
        wn.update()
    except turtle.Terminator:
        break
