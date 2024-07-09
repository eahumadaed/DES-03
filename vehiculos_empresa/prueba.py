from gestion.services import *

#Crear chofer
crear_chofer('12345678K', 'Juan', 'Perez')
imprimir_datos_vehiculos()

# Crear papu
crear_vehiculo('ABC123', 'Toyota', 'Corolla', 2020)
imprimir_datos_vehiculos()

# Asignar chofer al papu
asignar_chofer_a_vehiculo('12345678K', 'ABC123')
imprimir_datos_vehiculos()

# Deshabilitar un chofer
deshabilitar_chofer('12345678K')
imprimir_datos_vehiculos()

# Habilitar un chofer
habilitar_chofer('12345678K')

imprimir_datos_vehiculos()
