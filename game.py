import turtle
import winsound

# Création de la fenêtre de jeu
win = turtle.Screen()
win.title('Pong')
win.bgcolor('green')
win.setup(width=1000,height=700)
win.tracer(0)  # Désactivation de la mise à jour automatique de l'écran

# Fonction pour dessiner le terrain de jeu
def drawField():
    draw = turtle.Turtle()
    draw.penup()
    draw.speed(0)
    draw.color('white')
    draw.hideturtle()
    draw.goto(-390,295)
    draw.pendown()
    for i in range(2):
        draw.forward(770)
        draw.right(90)
        draw.forward(580)
        draw.right(90)
    draw.goto(0,295)
    draw.right(90)
    draw.goto(0,-285)
    draw.penup()
    draw.goto(-50,0)
    draw.pendown()
    draw.circle(50)

drawField()

# Initialisation des scores
scoreA = 0
scoreB = 0

# Raquette A
padA = turtle.Turtle()
padA.speed(0)
padA.shape('square')
padA.shapesize(stretch_wid=8,stretch_len=1)
padA.color('blue')
padA.penup()
padA.goto(-350,0)

# Raquette B
padB = turtle.Turtle()
padB.speed(0)
padB.shape('square')
padB.shapesize(stretch_wid=8,stretch_len=1)
padB.color('red')
padB.penup()
padB.goto(350,0)

# Balle
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)

ball.dx = 0.5  # Déplacement horizontal initial
ball.dy = 0.5  # Déplacement vertical initial

# Stylo pour afficher les scores
pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,250)


# Fonction pour écrire les scores avec une animation
def write():
    pen.write(f"Player A : {scoreA}    Player B : {scoreB}", align='center', font=('Times New Roman', 25, 'normal'))

write()


# Gestion des entrées clavier pour les raquettes
def padA_up():
    y = padA.ycor()
    y += 55
    padA.sety(y)

def padA_down():
    y = padA.ycor()
    y -= 55
    padA.sety(y)

def padB_up():
    y = padB.ycor()
    y += 55
    padB.sety(y)

def padB_down():
    y = padB.ycor()
    y -= 55
    padB.sety(y)

# Association des touches du clavier aux fonctions de déplacement des raquettes
win.listen()
win.onkeypress(padA_up,'z')
win.onkeypress(padA_down,'s')
win.onkeypress(padB_up,'Up')
win.onkeypress(padB_down,'Down')



# Fonction pour jouer de la musique
def playMusic(music):

        winsound.PlaySound(music, winsound.SND_ASYNC)


# Boucle principale du jeu
while True:
    try:
        win.update()  # Mise à jour de l'écran

        # Déplacement de la balle
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Gestion des collisions avec les bords
        if ball.ycor() > 290:
            ball.dy *= -1
            playMusic('assets/oh-no.wav')

        if ball.ycor() < -290:
            ball.dy *= -1
            playMusic('assets/oh-no.wav')

        if ball.xcor() > 390:
            ball.setx(-100)
            ball.dx *= -1
            scoreA += 1
            playMusic('assets/CLAPPING.wav')
            pen.clear()
            write()

        if ball.xcor() < -390:
            ball.setx(-100)
            ball.dx *= -1
            scoreB += 1
            playMusic('assets/CLAPPING.wav')
            pen.clear()
            write()

        # Gestion des collisions avec les raquettes
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < padB.ycor() + 50 and ball.ycor() > padB.ycor() - 50):
            playMusic('assets/hit1.wav')
            ball.setx(340)
            ball.dx *= -1
        if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < padA.ycor() + 50 and ball.ycor() > padA.ycor() - 50):
            playMusic('assets/hit2.wav')
            ball.setx(-340)
            ball.dx *= -1

    except Exception as e:
        pass  # Ignorer les erreurs et continuer l'exécution du programme
