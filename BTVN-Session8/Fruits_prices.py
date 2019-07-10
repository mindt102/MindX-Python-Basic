prices = {
    "banana" : 4,
    "apple" : 2,
    "orange": 1.5,
    "pear" : 3,
}

stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15,
}

total = 0

for k,v in prices.items():
    total += v*stock[k]
    print("*",k)
    print("* price:",v)
    print("* stock:",stock[k])
    print()

print("Total: $",total,sep = "")