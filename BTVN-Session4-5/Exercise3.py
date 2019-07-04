print("20 numbers, starting from 0")
print(*range(20))
input("\nPress Enter to continue\n")


n = int(input("Enter a number: "))
print(n,"positive numbers from 0 to",n-1)
print(*range(n))
input("\nPress Enter to continue\n")


print("1's and 0's, consecutively")
for i in range (20):
    print(1 - i%2,end = ' ')
input("\nPress Enter to continue\n")    


n = int(input("Enter a number: "))
print(n,"1's and 0's in total consecutively")
for i in range(n):
    print(1 - i%2,end = ' ')
input("\nPress Enter to continue\n")


print("9x9 numbers (multiplication table)")
for i in range(1,10):
    for j in range(1,10):
        print(j*i,end = ' '*(3-len(str(j*i))))
    print()
input("\nPress Enter to continue\n")


n = int(input("Enter a number: "))
print(n,'x',n,'numbers (multiplication table)')
for i in range (1,n+1):
    for j in range(1,n+1):
        print(i*j,'\t',end = "")
    print()
input("\nPress Enter to continue\n")


print("10x10 1's and 0's consecutively:")
for i in range (1,10 + 1):
    for j in range (1,10+1):
            print(1 - (i%2 - j%2)**2,end = "  ")      
    print()
input("\nPress Enter to continue\n")


n = int(input("Enter a number: "))
print(n,'x',n,"1's and 0's consecutively:",sep = "")
for i in range (1,n + 1):
    for j in range (1,n+1):
       print(1 - (i%2 - j%2)**2,end = "  ")    
    print()
input("\nPress Enter to quit\n")
