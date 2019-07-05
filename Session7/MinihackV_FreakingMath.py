import random
point = 0

while True:
    numb1 = random.randint(1,30)
    numb2 = random.randint(1,30)   

    if random.randint(0,1):
        mark = "+"
    else:
        mark = "-"
        
    right_equa = "T"
    
    if random.randint(0,1):
        ans = random.randint(-30,30)
        if mark == "+":
            if int(numb1) + int(numb2) != int(ans):
                right_equa = "F"
        else:
            if int(numb1) - int(numb2) != int(ans):
                right_equa = "F"
    else:
        if mark == "+":
            ans = int(numb1) + int(numb2)
        else:
            ans = int(numb1) - int(numb2)

    print(numb1,mark,numb2,"=",ans)
    user_ans = input("Enter T/F:")
    if user_ans == "quit":
        break

    if user_ans == right_equa:
        point += 1
        print("Your points:",point)
        continue
    else:
        break
        
    