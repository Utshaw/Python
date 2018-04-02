import turtle



my_turtle = turtle.Turtle()

my_turtle.shape('turtle')

# turtle color
my_turtle.color('white')

# turtle speed
my_turtle.speed(2)

# getting window reference
window = turtle.Screen()

# set window bgcolor
window.bgcolor('red')


my_turtle.forward(100)

my_turtle.left(90)

my_turtle.forward(100)


my_turtle.right(90)

my_turtle.forward(100)

my_turtle.left(90) # angle 90 degree

my_turtle.forward(100)

my_turtle.left(90)

my_turtle.forward(200)

my_turtle.left(90)

my_turtle.forward(200)


# Fill Color: https://www.youtube.com/watch?v=lev0HW6Bb6c



triangle_turtle = turtle.Turtle()

triangle_turtle.color('white', 'blue')  # first argument is pen color, second argument is fill color

triangle_turtle.begin_fill()

triangle_turtle.forward(100)

triangle_turtle.left(120)

triangle_turtle.forward(100)

triangle_turtle.left(120)

triangle_turtle.forward(100)


triangle_turtle.end_fill()


# set exit method for window
window.exitonclick()


