print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División real")
print("5. División entera")
print("6. Módulo")

opcion = input("Seleccione una opción: ")

num1 = float(input("Ingrese primer número: "))
num2 = float(input("Ingrese segundo número: "))

if opcion == "1":
    print(num1 + num2)
elif opcion == "2":
    print(num1 - num2)
elif opcion == "3":
    print(num1 * num2)
elif opcion == "4":
    print(num1 / num2)
elif opcion == "5":
    print(num1 // num2)
elif opcion == "6":
    print(num1 % num2)
else:
    print("Opción no válida")