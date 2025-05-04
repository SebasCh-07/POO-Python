from laptop import Laptop
import random

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuestos=10):
        super().__init__(marca, procesador, memoria, costo, impuestos)
        self.almacenamiento = almacenamiento 
        self.duracion_bateria = duracion_bateria

    def __str__(self):
        return f" Marca: {self.marca} \n Procesador: {self.procesador}\n Memoria: {self.memoria}\n Almacenamiento: {self.almacenamiento}\n Duracion de Bateria {self.duracion_bateria}\n Costo: {self.costo}\n Impuestos: {self.impuestos}\n" 

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema() 
        diagnostico_empresarial = {
            "ALMACENAMIENTO": "OK" if self.almacenamiento >= 256 else "Espacio insuficiente",
            "DURACION DE BATERIA": "OK" if self.duracion_bateria >= 6 else "Duración insuficiente para trabajo empresarial"
        }
        conectividad = self.verificar_conectividad_red()
        resultado_diagnostico.update(diagnostico_empresarial)
        resultado_diagnostico.update(conectividad)
        return resultado_diagnostico

    def verificar_conectividad_red(self):
        conectividad = {
            "Wi-Fi disponible": random.choice([True, False]),
            "Acceso a servidores empresariales": random.choice([True, False]),
            "Latencia de red aceptable": random.choice([True, False])
        }
        return conectividad


    pass