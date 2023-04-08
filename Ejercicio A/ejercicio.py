
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []
        self.empleados = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def eliminar_edificios_en_ciudad(self, ciudad):
        self.edificios = [edificio for edificio in self.edificios if edificio not in ciudad.edificios]

        
class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
        
        
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre


class Ciudad:
    def __init__(self,nombre):
        self.nombre = nombre
        self.edificios = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

    def destruir(self):
        self.edificios = []


yoohoo = Empresa('YooHoo!')
new_york = Ciudad('New York')
los_angeles = Ciudad('Los Ángeles')
edificio_a = Edificio('A')
edificio_b = Edificio('B')
edificio_c = Edificio('C')
martin = Empleado('Martin')
salim = Empleado('Salim')
xing = Empleado('Xing')



yoohoo.agregar_edificio(edificio_a)
yoohoo.agregar_edificio(edificio_b)
yoohoo.agregar_edificio(edificio_c)
yoohoo.agregar_empleado(martin)
yoohoo.agregar_empleado(salim)
yoohoo.agregar_empleado(xing)
new_york.agregar_edificio(edificio_a)
new_york.agregar_edificio(edificio_b)
los_angeles.agregar_edificio(edificio_c)

new_york.destruir()
yoohoo.eliminar_edificios_en_ciudad(new_york)
