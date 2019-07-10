items = ["com","pho","chao","bun"]
print(items,"\n")

items.pop(1)
print("Xoa phan tu thu 2:\n",items,"\n",sep = "")

if "LOL" in items:
    items.remove("LOL")
else:
    print("LOL khong ton tai")
print(items,"\n")

i = int(input("Nhap vi tri phan tu muon xoa: "))
items.pop(i)
print(items,"\n")

item_to_del = input("Nhap phan tu muon xoa: ")
if item_to_del in items:
    items.remove(item_to_del)
else:
    print(item_to_del,"khong ton tai")
print(items)