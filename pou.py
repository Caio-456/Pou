import turtle

turtle.title("Pou!!!")
screen = turtle.Screen()
screen.setup(0.6, 0.6)
paulin = turtle.Turtle()
paulin.shape('turtle')
paulin.speed(3)
paulin.color('#101010')
paulin.pensize(3)
paulin.pu()
paulin.begin_fill()
# Abreviações: penup(pu), pendown(pd).

# Canto direito:
paulin.setheading(-90.1)
paulin.goto((150.56, -42.65))
paulin.pd()
paulin.circle(-100, 80)
paulin.pu()
cdireito = paulin.pos()

# Base:
paulin.goto(cdireito)
paulin.setheading(-168)
paulin.pd()
paulin.circle(-430, 25)
paulin.pu()
base = paulin.pos()

# Canto esquerdo:
paulin.setheading(160)
paulin.pu()
paulin.goto(base)
paulin.pd()
paulin.circle(-100, 80)
paulin.pu()
cesquerdo = paulin.pos()

# Lado esquerdo:
paulin.goto(cesquerdo)
paulin.setheading(67.3)
paulin.pd()
paulin.circle(-430, 25)
paulin.pu()
lesquerdo = paulin.pos()

# Topo:
paulin.setheading(36.6)
paulin.goto(lesquerdo)
paulin.pd()
paulin.circle(-100, 80)
paulin.pu()
topo = paulin.pos()

# Lado direito:
paulin.setheading(-46)
paulin.goto(topo)
paulin.pd()
paulin.circle(-433, 25)
paulin.pu()

paulin.color('#D6A259')
paulin.end_fill()
paulin.penup()
paulin.setheading(0)

#Olho esquerdo:
paulin.pu()
paulin.color('#101010')
paulin.goto(-25, 43)
paulin.pd()
paulin.setheading(45)
paulin.begin_fill()
paulin.circle(40, 90)
paulin.circle(27, 90)
paulin.circle(40, 90)
paulin.circle(27, 90)
paulin.color('#FEFEFE')
paulin.end_fill()
paulin.pu()
paulin.goto(-41, 69)
paulin.dot(20, '#101010')

# Olho direito:
paulin.pu()
paulin.color('#101010')
paulin.goto(35, 43)
paulin.pd()
paulin.setheading(45)
paulin.begin_fill()
paulin.circle(40, 90)
paulin.circle(27, 90)
paulin.circle(40, 90)
paulin.circle(27, 90)
paulin.color('#FEFEFE')
paulin.end_fill()
paulin.pu()
paulin.goto(18, 69)
paulin.dot(20, '#101010')

# Boca:
paulin.pensize(4)
paulin.color('#101010')
paulin.pu()
paulin.goto(-90, 15)
paulin.pd()
paulin.setheading(240)
paulin.circle(35, 45)
paulin.setheading(-80)
paulin.circle(15, 70)
paulin.setheading(-15)
paulin.circle(20, 45)

# Final:
paulin.pu()
paulin.goto((120, 100))
paulin.color('#01bb01')
rodadinha = 0
for j in range(3):
  for i in range(5):
    rodadinha += 2
    paulin.left(rodadinha)
    screen.bgcolor('#fe8081')
  for i in range(5):
    rodadinha += 2
    paulin.left(rodadinha)
    screen.bgcolor('#01ffff')
  for i in range(5):
    rodadinha += 2
    paulin.left(rodadinha)
    screen.bgcolor('#fff951')
  for i in range(5):
    rodadinha += 2
    paulin.left(rodadinha)
    screen.bgcolor('#ffa64c')
  for i in range(5):
    rodadinha += 2
    paulin.left(rodadinha)
    screen.bgcolor('#ff67a8')
# Essas são as cores dos papeis de parede do Pou, mas excluí o verde para não misturar com a tartaruga.
screen.bgcolor('#fff')
screen.mainloop()
