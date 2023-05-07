import csv
from PlanAhorro import Plan
class ManejadorPlan:
    listaplan= []

    def __init__(self):
        self.__listaplan=[]

    def cargar_lista(self):
        archivo='Planes.csv'
        with open (archivo, 'r', newline='') as archivo_csv:
                lector_csv = csv.reader(archivo_csv, delimiter=';')
                for fila in lector_csv:
                    planaho= Plan(fila[0],fila[1],fila[2],int(fila[3]))
                    self.__listaplan.append(planaho)


    def actualizar_valor_vehiculos(self):
        for fila in self.__listaplan:
            print (fila.get_codigo())
            print (fila.get_modelo())
            print (fila.get_version())
            valor=int(input("Ingrese valor de vehículo actual "))
            if fila.get_valor()==valor:
                nuevoval=int(input("Ingrese el nuevo valor del vehículo "))
                fila.actualizar_valor(nuevoval)
            else:
                print ("Valor ingresado incorrecto")

    def mostrar_datosvehic_valorc(self):
        nuevovcuota=int(input("Ingrese el valor de cuota "))
        print ("Vehículos con valor de cuota al inferior dado:")
        for fila in self.__listaplan:
            if (fila.valorcuota()<=nuevovcuota):
                print(fila.get_codigo())
                print(fila.get_modelo())
                print(fila.get_version())

    def mostrar_cuotalicitar(self):
        for fila in self.__listaplan:
            print ("El monto de las cuotas a licitar del vehiculo es:")
            print(fila.get_modelo())
            print(fila.get_version())
            print(int(Plan.get__cuotalicitas()*fila.valorcuota()))

    def modificar_cuotas(self):
        nuevascuotas=int(input("Ingrese la nueva cantidad de cuotas a licitar "))
        Plan.modificar_cuotalicitar(nuevascuotas)
