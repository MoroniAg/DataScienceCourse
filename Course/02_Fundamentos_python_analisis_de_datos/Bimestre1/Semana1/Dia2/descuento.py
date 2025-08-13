price = float(input("Ingrese el precio del producto: "))
offer = float(input("Ingrese el porcentaje de descuento: "))
discount = price * (offer / 100)
final_price = price - discount
print(f"El precio final es: {final_price:0.2f}")