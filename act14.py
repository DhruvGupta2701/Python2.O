with open("Z:\MyFile.txt","w") as file:
    for i in range(3):
        l = input(f"Enter line {i+1}:")
        file.write(l + "\n")
print("Three lines have been written to MyFile.txt")
