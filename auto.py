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


auto_new = Auto("Porsche", "911 Carrera GTS", 2010)
print(auto_new.mostrar_inf())
print(auto_new.actualizar_kilometraje(20000))
print(auto_new.realizar_viaje(30000))
print(auto_new.estado_auto())

print(auto_new.__dict__)
