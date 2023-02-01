# Contador e entrada do número do usuário
cont = 0
num = int(input("\nDigite um número: "))

# Verificação do número
print()
for n in range(1, num + 1):
    if num % n == 0:
        print(f"({n})", end=" ") 
        cont += 1
    else: print(n, end=" ")

# Resultado
print()
print(f"\nO número {num} foi divisivel {cont} vezes")

if cont > 2: print("E por isso ele NÃO É PRIMO")
else: print("E por isso ele É PRIMO\n") 