#Program to perform Binary Search on a user defined List

def binarySearch(l,num):
    low = 0
    upper = len(l)-1
    mid = 0
    while (low<=upper):
        mid = (upper + low) // 2
        if l[mid] < num:
            low = mid + 1

        elif l[mid] > num:
            upper = mid - 1

        else:
            return mid
            
    return -1

l = []
x = int(input("\nEnter the no of elements in List: "))
for i in range(x):
    ele = int(input(f"Enter {i+1} element of  list: "))
    l.append(ele)
print("Given List = ",l)
l.sort()
print("Sorted list = ",l)

num = int(input("\nEnter element to be searched: "))
result = binarySearch(l,num)
if (result != -1):
    print(f"{num} is present in list at index {result}")
else:
    print(f"{num} is not in the list")
    
    
#Program to perform Linear Search on a user defined List

def linearSearch(l,n,num):
    for i in range(0,n):
        if (l[i] == num):
            print(f"{num} is present in the List at index {i}")
            break
    else:
        print(f"{num} is not in the List.")

l = []
x = int(input("Enter the elements of List: "))
print("\n")
for i in range(x):
    ele = int(input(f"Enter {i+1} element of  list: "))
    l.append(ele)
print(l)
n = len(l)
num = int(input("\nEnter a number to be searched: "))
linearSearch(l,n,num)