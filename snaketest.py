import turtle 
import random 
import time 

delay = 0.1
#score
score = 0 
high_score = 0

#Set up the screen 
wn = turtle.Screen()
wn.title("Snake by Luke Henderson")
wn.bgcolor("Blue")
wn.setup(width=700, height=700)
wn.tracer(0)

#Snake head 
head = turtle.Turtle()
head.speed(1)
head.shape("square")
head.color("Black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Snake food
food = turtle.Turtle()
food.speed(0)
food.color("White")
food.shape("circle")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score : 0 High Score : 0", align = "center", font = ("Courier", 24, "normal"))

# Fuctions

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move(): 
    if head.direction == "up": 
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left": 
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Setting up keyboard 

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main loop 

while True:
    wn.update()

    # Check for border collision 
    if head.xcor()>340 or head.xcor()< -340 or head.ycor()>340 or head.ycor()< -340:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
    
    # Hide the segments 
    for segment in segments: 
        segment.goto(1000,1000)
    
    # Clear the segments list
    segments.clear()

    #Reset the score 
    score = 0 

    #Reset the Delay 
    delay = 0.1

    #reset pen
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #Check for collison with food 
    if head.distance(food) < 20:
        # Move food to random location 
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        food.goto(x,y)

        #Add segments 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay 
        delay -=0.001

        #Increase score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move segments to end in reverse order 
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # Move segment 0 to where the head is 
    if len(segments) > 0: 
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #Check for head collsion with body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #Hide the segments 
            for segment in segments:
                segment.goto(1000,1000)

            #Clear the segments 
            segments.clear()

            #Reset the score 
            score = 0

            #Reset delay 
            delay = 0.1 

            #Update score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
