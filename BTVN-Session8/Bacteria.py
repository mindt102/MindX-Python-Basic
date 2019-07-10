init_bac = int(input("How much B bacterias are there? "))
time = int(input("How much time in minutes will we wait? "))

bac = init_bac*(2**(time//2))

print("After 4 minutes, we would have",bac,"bacterias.")