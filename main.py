import turtle as t

print('''1 - dragon fractal
2 - tree
3 - Koch curve
4 - Sierpinski triangle''')
choose = input('input number: ')

pensize = 1
t.hideturtle()
t.pensize(pensize)
t.tracer(1)


def create_program(axiom, rule, itr):
    for j in range(itr):
        tmp = ''
        for key in axiom:
            tmp += rule.get(key, key)
        axiom = tmp
    return axiom


def draw_fractal(axiom, angle, distance):
    stack = []
    for i in axiom:
        if i == 'F' or i == 'G':
            t.forward(distance)
        elif i == '+':
            t.right(angle)
        elif i == '-':
            t.left(angle)
        elif i == '[':
            stack.append(t.xcor())
            stack.append(t.ycor())
            stack.append(t.heading())
            t.left(angle)
        elif i == ']':
            t.penup()
            t.setheading(stack.pop())
            t.sety(stack.pop())
            t.setx(stack.pop())
            t.right(angle)
            t.pendown()


if choose == '1':  # dragon fractal
    Itr = 10
    Angle = 90
    Distance = 5
    Axiom = 'FX'
    Rule = {"X": "X+YF+", "Y": "-FX-Y"}     # (X → X+YF+), (Y → −FX−Y)

    Axiom = create_program(Axiom, Rule, Itr)
    t.tracer(2)
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    draw_fractal(Axiom, Angle, Distance)
    t.update()
    t.done()
elif choose == '2':  # tree
    Itr = 6
    Angle = 45
    Distance = 10
    Axiom = 'F'
    Rule = {"F": "G[F]F", "G": "GG"}  # (G → GG), (F → G[F]F)

    Axiom = create_program(Axiom, Rule, Itr)

    t.penup()
    t.setposition(0, t.window_height() / -2 + 10)
    t.left(90)
    t.pendown()
    draw_fractal(Axiom, Angle, Distance)
    t.update()
    t.done()
elif choose == '3':  # Koch curve
    Itr = 5
    Angle = 60
    Distance = 6
    Axiom = 'F'
    Rule = {"F": "F-F++F-F"}  # (F → F-F++F-F)

    Axiom = create_program(Axiom, Rule, Itr)

    t.penup()
    t.setposition(-720, -400)
    t.pendown()
    t.tracer(2)
    draw_fractal(Axiom, Angle, Distance)
    t.update()
    t.done()
elif choose == '4':  # Sierpinski triangle
    Itr = 4
    Angle = 120
    Distance = 20
    Axiom = 'F-G-G'
    Rule = {"F": "F-G+F+G-F", "G": "GG"}  # (F → F−G+F+G−F), (G → GG)

    Axiom = create_program(Axiom, Rule, Itr)

    t.penup()
    t.setposition(-125, -125)
    t.pendown()
    draw_fractal(Axiom, Angle, Distance)
    t.update()
    t.done()
else:
    print('Input argument error')
