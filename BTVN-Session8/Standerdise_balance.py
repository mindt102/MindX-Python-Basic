while True:
    balance = input("Enter your balance: ")
    if balance.isdigit():
        break
balance = list(balance)
while balance[0] == "0":
    balance.pop(0)

print("Your updated balance: $",end = "")

length = len(balance)
for i,numb in enumerate(balance):
    print(numb,end = "")
    if ((i+1) % 3) == (length % 3) and (i+1) != length:
        print(",", end = "")