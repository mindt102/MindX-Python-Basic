pairs = [1]

for i in range(5):
    pairs.append(pairs[i] + pairs[i-1])
    print("Month ",i,": ",pairs[i]," pair(s) of rabbit",sep = "")
    