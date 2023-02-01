# turtle drawing at the start of the game
def start_drawing():

    import turtle
    tut = turtle.Pen()

    ## drawing function
    def draw_square(color="black", fill_color="black"):
        ### pen color
        tut.color(color)
        tut.fillcolor(fill_color)

        ### making the turtle go in a square
        for x in range(5):
            tut.forward(100)
            tut.left(90)

    ## black drawing 
    draw_square()

    ## red and blue drawing
    draw_square("red", "blue")

    ## purple and pink drawing
    
    #draw_square("purple", "pink")

    ## close the screen after
    turtle.Screen().bye()