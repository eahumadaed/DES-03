from .models import Vehiculo, Chofer, RegistroContabilidad

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo.objects.create(patente=patente, marca=marca, modelo=modelo, year=year)
    return vehiculo

def crear_chofer(rut, nombre, apellido):
    chofer = Chofer.objects.create(rut=rut, nombre=nombre, apellido=apellido)
    return chofer

def crear_registro_contable(vehiculo_patente, fecha_compra, valor):
    vehiculo = Vehiculo.objects.get(patente=vehiculo_patente)
    registro = RegistroContabilidad.objects.create(vehiculo=vehiculo, fecha_compra=fecha_compra, valor=valor)
    return registro

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()
    return chofer

def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    if vehiculo.chofer:
        vehiculo.chofer.activo = False
        vehiculo.chofer.save()
    return vehiculo

def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()
    return chofer

def habilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    if vehiculo.chofer:
        vehiculo.chofer.activo = True
        vehiculo.chofer.save()
    return vehiculo

def obtener_vehiculo(patente):
    return Vehiculo.objects.get(patente=patente)

def obtener_chofer(rut):
    return Chofer.objects.get(rut=rut)

def asignar_chofer_a_vehiculo(rut, patente):
    chofer = Chofer.objects.get(rut=rut)
    vehiculo = Vehiculo.objects.get(patente=patente)
    chofer.vehiculo = vehiculo
    chofer.save()
    return vehiculo

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        print(f"Vehículo {vehiculo.patente} - Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}")
        try:
            if vehiculo.chofer:
                print(f"  Chofer: {vehiculo.chofer.nombre} {vehiculo.chofer.apellido} - {'Activo' if vehiculo.chofer.activo else 'Inactivo'}")
            else:
                print("  Chofer: Ninguno")
        except Chofer.DoesNotExist:
            print("  Chofer: Ninguno")
        if hasattr(vehiculo, 'registrocontabilidad'):
            print(f"  Registro Contable - Fecha de Compra: {vehiculo.registrocontabilidad.fecha_compra}, Valor: {vehiculo.registrocontabilidad.valor}")
        else:
            print("  Registro Contable: No disponible")
        print()
