size=int(input("Enter the size : "))
lst=[]
for i in range(size):
    num=int(input("Enter the number : "))
    lst.append(num) 
data =list(map(lambda num : num*num,lst))
print("Square of given numbers in the list : ",data)




