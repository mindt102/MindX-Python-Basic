highscores = [45,67,56,78]

highscores.sort(reverse = True)
print("High scores:")
for i,score in enumerate(highscores):
    if i > 4:
        break
    print(i+1,". ",score,sep = "")
        
for i in range(3):
    highscores.append(int(input("Enter your new scores: ")))
    highscores.sort(reverse = True)
    print("High scores:")
    for i,score in enumerate(highscores):
        if i > 4:
            break
        print(i+1,". ",score,sep = "")

