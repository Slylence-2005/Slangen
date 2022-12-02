num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))

my_tuple = (num5, num4, num3, num2, num1)

my_list = list(my_tuple)

my_list.sort()

print(my_list[::-1])