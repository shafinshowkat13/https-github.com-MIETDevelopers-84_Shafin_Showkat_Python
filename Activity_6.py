
d = {}
x = int(input("Enter number keys : "))
for i in range(x):
    k = input(f"Enter the {i+1} key : ")
    v = input(f"Enter the value for the key {i+1} : ")
    d[k] = v
print(d)
for i in d:
    print(i, '->', d[i])
a = input("Do you want to search the record (Yes/No) : ")
if (a == "yes") or (a == "Yes") or (a == "y") or (a == "Y"):
    name = input("Enter the name of the student : ")
    if name in d.keys():
        print(d[name])
    else:
        print("Student Not Found")
else:
    print()