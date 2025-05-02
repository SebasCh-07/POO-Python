from laptop import Laptop

laptop_pepito = Laptop("lenovo", "i7", 32)
laptop_maria = Laptop("lenovo", "i7", 32, 600)

for numero in range(1,1001):
    asus_lap = Laptop.asus_lap(numero)
    print(asus_lap.__dict__)

#print(Laptop.comparar_costo(laptop_pepito, laptop_maria))