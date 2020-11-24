#Ben_Chadwick_Triangle_Illusion
#Program prints an optical illusion of a triangle
#Ben Chadwick
#10/26/20

#import all the modules that are going to be used
import turtle
import time

#set up window
win = turtle.Screen()
win.setup(500, 500)
win.title("Triangle Illusion")
win.tracer(2)


while True: #added while true to create a loop for the whole program
        colors = ["black", "white"] #created a list of triangle fill colors for the for loop to chose from
        for i in colors: #created a for loop for all the background colors and fill colors to randomize through
            if i == "black": #created an if statement to get the opposite color of i for the pen color and assigned variables to each colors
                colorpen = "white"
            else:
                colorpen = "black"
            pencolor = (i) #created a variable for the pen color 
            
            #creatle turtle "ben"
            ben = turtle.Turtle()
            
            ben.speed(0)
            ben.pensize(10)
            ben.pencolor(pencolor) #called for the pencolor variable for the pen's color
            ben.hideturtle() #hide turtle so program looks better when going through the loop
            
            #begin drawing outer part of triangle
            ben.penup()
            ben.goto(-25, 220)
            ben.pendown()
            ben.fillcolor(colorpen)
            ben.begin_fill()
            ben.forward(60)
            ben.left(-60)
            ben.forward(400)
            ben.left(-60)
            ben.forward(60)
            ben.right(60)
            ben.forward(400)
            ben.right(60)
            ben.forward(60)
            ben.right(60)
            ben.forward(400)
            ben.end_fill()
            #end fill
            #finished outer triangle

            #begin drawing inner triangle
            ben.penup()
            ben.goto(0, 100)
            ben.pendown()
            ben.fillcolor('limegreen')
            ben.begin_fill()
            ben.right(120)
            ben.forward(200)
            ben.right(120)
            ben.forward(200)
            ben.right(120)
            ben.forward(200)
            ben.end_fill()
            #finished inner triangle

            #right inner line
            ben.forward(50)
            ben.goto(205, -178.37)
            ben.penup()
            #finished right line

            #lower inner line
            ben.goto(-225, -126.41)
            ben.pendown()
            ben.seth(0) #set direction east
            ben.forward(355)
            ben.goto(100.00,-73.21)
            #finished lower inner line

            #begin last left inner line
            ben.seth(180) #set direction west
            ben.forward(235)
            ben.goto(35,220)
            ben.right(120)
            ben.penup()
            #finished left inner line

            ben.goto(0,100) #set turtle to top of inner triangle
            ben.pendown()
            ben.speed(0) #speed up turtle

            
            #created a list of colors in order for future use on background and inner fill triangle
            colors = ["red", "orangered", "darkorange", "orange", "gold", "yellow", "greenyellow", "limegreen", "limegreen", "forestgreen", "green", "mediumaquamarine", "lightseagreen", "turquoise", "steelblue", "dodgerblue", "royalblue", "mediumblue", "darkslateblue", "mediumslateblue", "blueviolet", "darkorchid", "darkviolet", "purple", "indigo", "darkmagenta", "magenta", "crimson", "red", "orangered", "darkorange",  "orange", "gold", "yellow", "greenyellow", "limegreen"]


            for i in colors: #created loop to cycle through colors once before going back to While true
                
                colorchoice = i #used colorchoice to assign a variable for i
                    
                ben.fillcolor(colorchoice) #using the new variable colorchoice, the program now changes its fill color everytime the loop repeats
                ben.begin_fill() #turtle outlines inner triangle again
                ben.right(120)
                ben.forward(200)
                ben.right(120)
                ben.forward(200)
                ben.right(120)
                ben.forward(200)
                    

                ben.end_fill() #end filling in new inner triangle
                win.bgcolor(colorchoice) # change the background of window to match filled in section after triangle is made to make sure the colors are in sync
                time.sleep(.00) #add a delay to make the program run smoother and it doesnt take as much processing power from the computer
                    #program loops again
               
