# Factorial display
num = int(input("Enter your number: "))
f = 1

for n in range(num, 1, -1): 
  f *= n

print(f"{num}! = {f}")
