# Input first number
first_number =int( input("Enter first number "))
int()
# Input opration type
opration = input("Enter opration type ")
# Input second number
second_number = int( input("Enter second number "))
# print the result 
if opration == "+" :
 print(first_number + second_number)
elif opration == "-" :
 print(first_number - second_number)
elif opration == "*" :
 print(first_number * second_number)
elif opration == "/" :
  print(first_number / second_number)
else:
 print("Error")