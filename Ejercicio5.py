# En una tienda se ofrece un descuento del 15% sobre el total de la compra
# y un cliente desea saber cuánto deberá pagar finalmente por su compra

compra = float(input("Ingrese Cantidad a Cobrar: "))
descuento = compra * 0.15

print(f"Total a pagar es ${compra - descuento: .1f}")