# Arithmetic Progression Generator
count = 1

print("-=" * 40)
firstTerm = int(input("Enter first term: "))
ratio = int(input("Enter ratio: "))

# Only the first 10 terms of the progression
while True:
    if count != 10:
        print(f"{firstTerm} → ", end="")
        firstTerm += ratio
        count += 1
    else: 
        print(f"{firstTerm} → ...")
        break
