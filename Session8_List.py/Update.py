items = ["com","pho","chao"]
items.append("bun")

items[0] = "Spider Man"
items[-1] = "Dragon ball"
print(items)

i = int(input("Nhap vi tri muon sua: "))
items[i] = input("Nhap noi dung: ")

print(items)