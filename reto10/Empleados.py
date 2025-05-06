from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        return self.salario_base * 1.20


class EmpleadoMedioTiempo(Empleado):
    def calcular_salario(self):
        return self.salario_base * 1.10


# Clase de Prueba
emp1 = EmpleadoTiempoCompleto("Ana", 1000)
emp2 = EmpleadoMedioTiempo("Luis", 800)

print(f"{emp1.nombre} - Salario Final: {emp1.calcular_salario()}")
print(f"{emp2.nombre} - Salario Final: {emp2.calcular_salario()}")

empleados = [emp1, emp2]
for e in empleados:
    print(f"{e.nombre} - Salario Final: {e.calcular_salario()}")
