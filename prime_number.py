# Contador e entrada do número do usuário
count = 0
num = int(input("\nEnter a number: "))

# Verificação do número
print()
for n in range(1, num + 1):
    if num % n == 0:
        print(f"({n})", end=" ") 
        count += 1
    else: print(n, end=" ")

# Resultado
print()
print(f"\nThe number {num} was divisible {count} times")

if count > 2: print("And that's why he's NOT PRIME NUMBER")
else: print("And that's why he's PRIME NUMBER\n")
