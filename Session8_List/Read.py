items = ["com","pho","chao"]
items.append("bun")

print(*items)
print(*items,sep = ", ")
print(*items,sep = "|")

print("Phan tu dau tien:",items[0].upper())
print("Phan tu cuoi cung:",items[-1].upper())
print("Phan tu gan cuoi:",items[-2].upper())
