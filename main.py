def main_function():
  print("Welcome!")

main_function()
print("This function calculates rectangle area.")
L = input("What is the length? ")
L = int(L)
W = input("What is the width? ")
W = int(W)
print("The length of the rectangle is", (L))
print("The width of the rectangle is", (W))
a = L*W
print("The area of the rectangle is",(a))


print("This function calculates rectangle perimeter.")
L = int (input("What is the length? "))
W = int (input("What is the width? "))
print("The length of the rectangle is", (L))
print("The width of the rectangle is", (W))
p = L+W+L+W
print("The perimeter of the rectangle is", (p))
print("Thank you for your time! Bye bye! ")