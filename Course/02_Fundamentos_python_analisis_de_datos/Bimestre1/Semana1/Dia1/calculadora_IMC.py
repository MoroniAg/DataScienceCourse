nombre = "Juan"
apellido = "Perez"
edad = 30
peso = 80.0
altura = 1.75
membresia = True

# Cálculo de IMC
imc = peso / (altura ** 2)

print(f"Cliente: {nombre} {apellido}")
print(f"Edad: {edad}")
print(f"IMC: {imc:.2f}")
print(f"Membresía activa: {membresia}")