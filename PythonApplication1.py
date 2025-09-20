precio = float(input("Ingrese el precio del producto: "))
codigo = int(input("Ingrese el código de descuento (1 = estudiante, 2 = empleado, 3 = cliente frecuente): "))

descuento = 0

if codigo == 1:
    descuento = 0.10
elif codigo == 2:
    descuento = 0.15
elif codigo == 3:
    descuento = 0.20

precio_final = precio - (precio * descuento)

# Descuento adicional si el precio original es mayor a 500
if precio > 500:
    precio_final -= precio * 0.05

print(f"Precio final: {precio_final:.2f}")
