from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from Laptop_Business import Laptop_Business


def imprimir_informe(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave}: {valor}")
    print("\n")




laptop_pepito = Laptop("lenovo", "i7", 32)
laptop_maria = Laptop("lenovo", "i7", 32, 600)

Laptop_juanito = Laptop_Gaming("MSI", "I7", 4, "RTX 8GB")
print(Laptop_juanito.realizar_diagnostico_sistema())


#laptop_jose = Laptop_Business("Hp", "i5", 6, 150, 5)
#print(laptop_jose.realizar_diagnostico_sistema())
print("Pepito")
imprimir_informe(laptop_pepito)
print("Juanito")
imprimir_informe(Laptop_juanito)



#for numero in range(1,1001):
#   asus_lap = Laptop.asus_lap(numero)
#  print(asus_lap.__dict__)

#print(Laptop.comparar_costo(laptop_pepito, laptop_maria))