from auto import Auto

porsche = Auto("Porsche", "911 Carrera GTS", 2010, 25000)
toyo = Auto.carToyo_new(30000)
bmw = Auto.carBMW_new(30000)

print(Auto.comparar_kilometraje(porsche,toyo))
print(Auto.comparar_año(bmw, porsche))