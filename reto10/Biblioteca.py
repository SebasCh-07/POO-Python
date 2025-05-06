class Libro:
    contador_libros = 0

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Libro.contador_libros += 1

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}")

    @staticmethod
    def es_grande(paginas):
        return paginas > 300

    @classmethod
    def total_libros(cls):
        return cls.contador_libros


# Clase de Prueba
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
libro3 = Libro("Don Quijote", "Miguel de Cervantes", 863)

for libro in [libro1, libro2, libro3]:
    libro.mostrar_info()
    print("¿Es grande?", Libro.es_grande(libro.paginas))

print("Total de libros creados:", Libro.total_libros())
