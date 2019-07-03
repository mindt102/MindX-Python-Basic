from turtle import *   # thu vien cho phep ve hinh
shape('turtle')
color('cyan')
speed(-1)              # di nhanh nhat

# for i in range(6):
#     for i in range(3):
#         forward(100)           
#         left(120)
#     right(7)

# for i in range(3,6):
#     for j in range (i):
#         forward(100)           
#         left(360/i)

# for i in range(4):
#     forward(100)           
#     left(90)

# for i in range(5):
#     forward(100)
#     left(72)

# Ve 30 hinh vuong khong chong len nhau
for i in range (30):
        for j in range(4):
                forward(100)
                left(90)
        left(7)

mainloop()             # giu cua so luon mo
