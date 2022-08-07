size=int(input("Enter the size : "))
lst=[]
for i in range(size):
    num=int(input("Enter the number : "))
    lst.append(num)
data=map(lambda num:num+num+num ,lst)
print("Triple of given list of numbers : ",list(data))

