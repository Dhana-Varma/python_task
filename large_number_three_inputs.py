# largest number among the three input numbers

# l=[45, 67, 99]
# print (max(l))

num1 = float(input("enter the number:"))
num2 = float(input("enter the number:"))
num3 = float(input("enter the number:"))
if (num1>=num2):
    if (num1>=num3):
        largest = num1
    elif (num2>=num1) and (num2>=num3):
        largest = num2
    else:
        largest = num3
        print ("largest number is:", largest)