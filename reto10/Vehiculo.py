class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"{self.marca} {self.modelo}, Año: {self.anio}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def descripcion(self):
        return f"{super().descripcion()}, Puertas: {self.num_puertas}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo

    def descripcion(self):
        return f"{super().descripcion()}, Tipo: {self.tipo}"


# Clase de Prueba
auto1 = Auto("Toyota", "Corolla", 2020, 4)
moto1 = Moto("Yamaha", "R3", 2021, "deportiva")

print(auto1.descripcion())
print(moto1.descripcion())

vehiculos = [auto1, moto1]
for v in vehiculos:
    print(v.descripcion())  # Polimorfismos