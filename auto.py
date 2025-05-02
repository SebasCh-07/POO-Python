class Auto:
    def __init__(self, marca, modelo, año, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_inf(self):
        return(f"Auto Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")
    
    def actualizar_kilometraje(self, kilometraje_nuevo):
        if kilometraje_nuevo > self.kilometraje:
            self.kilometraje = kilometraje_nuevo
            return(f"Se actulizo el Kilometraje a {kilometraje_nuevo}")
        else:
            return("No se puede reducir el Kilometraje")

    def realizar_viaje (self, Kilometros_viaje):
        if Kilometros_viaje > 0:
            self.kilometraje += Kilometros_viaje
            return(f"Se sumó {Kilometros_viaje} km")
        else:
            return("Los kilometros debes ser Positivos")
        
    def estado_auto(self):
        if self.kilometraje < 20000:
            return("Estoy como nuevo")
        elif self.kilometraje >= 20000 or self.kilometraje <= 100000:
            return("Ya estoy usado")
        elif self.kilometraje > 100000:
            return("Ya déjame descansar por favor")
        
    @classmethod
    def carToyo_new (cls, kilometraje = 0):
        marca = "Toyota"
        modelo = "Hilux"
        año = "2025" 
        return cls(marca, modelo, año, kilometraje)
    @classmethod
    def carBMW_new (cls, kilometraje = 0):
        marca = "BMW"
        modelo = "M3 GTR"
        año = "2005" 
        return cls(marca, modelo, año, kilometraje)
    @staticmethod
    def comparar_kilometraje(car1, car2):
        if car1.kilometraje == car2.kilometraje:
            return f"El kilometraje de {car1.marca} {car1.modelo} y {car2.marca} {car2.modelo} son iguales"
        else:
            return f"El kilometraje de {car1.marca} {car1.modelo} y {car2.marca} {car2.modelo} son diferentes"
    @staticmethod
    def comparar_año(car1, car2):
        anio1 = int(car1.año)
        anio2 = int(car2.año)
        if anio1 == anio2:
            return "Los dos autos son del mismo año"
        elif anio1 > anio2:
            return f"El auto mas actual es {car1.marca} {car1.modelo}"
        else:
            return f"El auto mas actual es {car2.marca} {car2.modelo}"


