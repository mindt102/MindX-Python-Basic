items = []
while True:
    option = input("C: Creat\nR: Read\nU: Update\nD: Delete\nQ: Quit\nChon mot thao tac: ")
    if option == "C":
        items.append(input("Nhap thu ban yeu thich: "))
    elif option == "R":
        if len(items) == 0:
            print("Danh sach rong.")
        else:
            print("Danh sach cua ban:")
            for i in items:
                print(i) 
    elif option == "U":
        location = int(input("Nhap vi tri ban muon thay doi: "))
        items[location] = input("Nhap noi dung: ")
    elif option == "D":
        location = int(input("Nhap vi tri ban muon xoa: "))
        items.pop(location)
    else:
        break
    print()
