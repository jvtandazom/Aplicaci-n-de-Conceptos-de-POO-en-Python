# Definición de la clase base
class Animal:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado (privado)
        self.__edad = edad      # Atributo encapsulado (privado)

    # Método público para acceder al atributo privado
    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    # Método que debe ser sobrescrito por las subclases
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

# Definición de la clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.raza = raza

    # Sobrescribiendo el método de la clase base
    def hacer_sonido(self):
        return "Guau"

    def obtener_raza(self):
        return self.raza

# Definición de otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.color = color

    # Sobrescribiendo el método de la clase base
    def hacer_sonido(self):
        return "Miau"

    def obtener_color(self):
        return self.color

# Función para demostrar el polimorfismo
def imprimir_sonido(animal):
    print(f"{animal.obtener_nombre()} dice: {animal.hacer_sonido()}")

# Crear instancias de las clases
perro = Perro("Rex", 5, "Labrador")
gato = Gato("Garfirl", 3, "Gris")

# Mostrar la información de los objetos
print(f"Nombre del perro: {perro.obtener_nombre()}")
print(f"Edad del perro: {perro.obtener_edad()}")
print(f"Raza del perro: {perro.obtener_raza()}")
imprimir_sonido(perro)

print(f"Nombre del gato: {gato.obtener_nombre()}")
print(f"Edad del gato: {gato.obtener_edad()}")
print(f"Color del gato: {gato.obtener_color()}")
imprimir_sonido(gato)

# Este código ha sido desarrollado por Jonathan Tandazo
