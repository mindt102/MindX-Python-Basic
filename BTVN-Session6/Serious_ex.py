while True:
    size = input("Enter size of the matrix: ")
    if size.isdigit():
        size = int(size)
        break
space = "\t"
top_bot_line = "* "*size            + space + "* "*size                   + space + "* "*(size - 1) + "  "      + space + "* "*size 
mid_line     = "* " + "  "*(size-1) + space + "* " + "  "*(size-2) + "* " + space + "* " + "  "*(size-2) + "* " + space + "* "*size
other_line   = "* " + "  "*(size-1) + space + "* " + "  "*(size-2) + "* " + space + "* " + "  "*(size-2) + "* " + space + "* "

for i in range(size):
    if i == 0 or i == size - 1:
        print(top_bot_line)
    elif i == (size//2 - (1 -size%2)):
        print(mid_line)
    else:
        print(other_line)