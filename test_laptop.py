from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from Laptop_Business import Laptop_Business


laptop_pepito = Laptop("lenovo", "i7", 32)
laptop_maria = Laptop("lenovo", "i7", 32, 600)

#laptop_juanito = Laptop_Gaming("MSI", "I7", 4, "RTX 8GB")
#print(laptop_juanito.realizar_diagnostico_sistema())


laptop_jose = Laptop_Business("Hp", "i5", 6, 150, 5)
print(laptop_jose.realizar_diagnostico_sistema())



#for numero in range(1,1001):
 #   asus_lap = Laptop.asus_lap(numero)
  #  print(asus_lap.__dict__)

#print(Laptop.comparar_costo(laptop_pepito, laptop_maria))