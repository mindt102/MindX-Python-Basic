import random
q1 = {
    "question" : "Who plays Thanos in the MCU?",
    "choices" : ["Josh Brolin", "Mark Ruffalo", "Jeremy Renner", "Paul Rudd"],
    "answer" : "Josh Brolin",
}

q2 = {
    "question" : "Who plays Gamora in the MCU?",
    "choices" : ["Pom Klementieff", "Karen Gillan", "Zoe Saldana", "Elizabeth Olsen"],
    "answer" : "Zoe Saldana"
}

q3 = {
    "question" : "Who plays Heimdall in the MCU?",
    "choices" : ["Don Cheadle","Anthony Mackie","Dave Bautista","Idris Elba"],
    "answer" : "Idris Elba"
}
questions = [q1,q2,q3]
correct_ans = 0
for q in questions:
    print(q["question"])
    random.shuffle(q["choices"])
    for i in range(4):
        print(i+1,". ",q["choices"][i],sep = "")
    user_guess = int(input("Your answer: ")) - 1
    if q["choices"][user_guess] == q["answer"]:
        print("Hura!!!")
        correct_ans += 1
    else: 
        print("Not a correct answer :'(")
    input("Press Enter to continue.\n")

print("Your accuracy rate: ",round(correct_ans/len(questions),4)*100,"%",sep = "")