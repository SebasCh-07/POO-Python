import random
class Laptop:
    def __init__(self, marca, procesador, memoria, costo = 500, impuestos = 10 ):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuestos = impuestos
    
    def valor_final(self):
        return self.costo + self.impuestos

    def valor_descuento(self, descuento):
        return (self.costo * descuento)/100
    
    def realizar_diagnostico_sistema(self):
        resultado = {
            "MARCA" : f"{self.marca}",
            "PROCESADOR" : f"{self.procesador}",
            "MEMORIA RAM" : "OK" if self.memoria >= 8 else "Aumentar memoria RAM",
            "BATERIA" : "OK" if random.choice([True, False]) else "Cambiar de Bateria"

        }
        return resultado
    
    def realizar_informe_uso(self):
        resultado_informe = {
            "Tipo": "Generica",
            "Uso Recomendado": "Tareas cotidianas",
            "hora de uso": 5,
            "Diagnostico actual": self.realizar_diagnostico_sistema()
        }
        return resultado_informe


    @staticmethod
    def comparar_costo(lap1, lap2):
        if lap1.costo == lap2.costo:
            return "Los costos son iguales"
        else:
            return "los costos son diferentes "

    @classmethod
    def asus_lap(cls, costo):
        marca = "asus"
        procesador = "i5"
        memoria = "16" 
        return cls(marca, procesador, memoria, costo)