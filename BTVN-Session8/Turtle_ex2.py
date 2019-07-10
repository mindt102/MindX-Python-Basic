from turtle import *
colors = ["red", "blue", "brown", "yellow", "grey"]

for c in colors:
    color(c)
    fillcolor(c)
    begin_fill()
    for i in range(5):
        if i%2:
            forward(100)
        else:
            forward(50)
        if i != 4:
            right(90)
    end_fill()
mainloop()