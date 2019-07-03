from turtle import *

speed(-1)
color("red")
right(30)

for i in range(4):
    for j in range (4):   
        forward(100)
        left (60 + 60*(j%2))
    left(90)

mainloop()