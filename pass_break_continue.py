i=0
while i <= 10:
    i += 1
    if i==3:
        break
    print(f"{i} Hola Mundo")
print(f"{i} Este siempre se imprime")

i=0
while i <= 10:
    i += 1
    if i==3:
        pass
    print(f"{i} Hola Mundo")

print(f"{i} Este siempre se imprime")

i=0
while i <= 10:
    i += 1
    if i==3:
        continue
    print(f"{i} Hola Mundo")
print(f"{i} Esto siempre se imprime")
