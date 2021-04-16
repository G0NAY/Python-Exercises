# Escribir un programa que tenga dos listas y que, a continuación, cree las siguientes listas (En las que no debe haber repeticiones):

# * Lista de palabras que aparecen en las dos listas.
# * Lista de palabras que aparecen en la primera lista, pero no en la segunda
# * Lista de palabras que aparecen en la segunda lista, pero no en la primera
# * Lista de palabras que aparecen en ambas listas.

verduras = ["Pepinos", "Cebollas", "Papas", "Zanahorias", "Jitomate", "Aguacate"]
frutas = ["Naranjas", "Mandarinas", "Platanos", "Piña", "Jitomate", "Pepinos", "Aguacate"]

lista_verduras = set(verduras)
lista_frutas = set(frutas)
print(f"Primer lista:\n {verduras}")
print(f"Segunda lista:\n {frutas}")
print(f"Elementos que aparecen en las dos listas:\n {list(lista_verduras & lista_frutas)}")
print(f"Elementos unicos de primera lista:\n {list(lista_verduras - lista_frutas)}")
print(f"Elementos unicos de la segunda lista:\n {list(lista_frutas - lista_verduras)}")
print(f"Elementos de las dos listas:\n {list(lista_frutas | lista_verduras)}")
