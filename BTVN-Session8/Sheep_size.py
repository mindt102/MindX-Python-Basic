sheep_sizes = [5,7,300,90,24,50,75]

print("Hello, my name is Minh and here is my flock")
print(sheep_sizes)
print()

for i in range(4):
    if i > 0:
        print("Month ",i,":",sep = "")
        for j in range(len(sheep_sizes)):
            sheep_sizes[j] += 50
        print("One month has passed, now here is my flock")
        print(sheep_sizes)

    if i < 3:
        print("Now my biggest sheep has size",max(sheep_sizes),"let's shear it")
        sheep_sizes[sheep_sizes.index(max(sheep_sizes))] = 8
        
        print("After shearing, here is my flock")
        print(sheep_sizes)
        print()

total_size = sum(sheep_sizes)
print("\nMy flock has size in total:",total_size)
print("I would get ",total_size," * 2$ = ",total_size*2,"$",sep = "")
