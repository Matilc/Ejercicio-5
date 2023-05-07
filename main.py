from ManejadorPlanAhorro import ManejadorPlan
import os
def menu_opciones():
    print("Menú de opciones:")
    print("1. Actualizar valor de vehículos")
    print("2. Mostrar código de plan, modelo, versión de vehículo")
    print("3. Mostrar monto para licitar vehículo")
    print("4. Modificar cantidad de cuota a licitar")
    print("5. Salir")

if __name__=='__main__':
    lista_plan=ManejadorPlan()
    lista_plan.cargar_lista()
    while True:
        os.system('cls')
        menu_opciones()
        menu={
              "1": "lista_plan.actualizar_valor_vehiculos()",
              "2": "lista_plan.mostrar_datosvehic_valorc()",
              "3": "lista_plan.mostrar_cuotalicitar()",
              "4": "lista_plan.modificar_cuotas()",
              "5": "print ('Gracias por usar nuestro sistema')"
        }
        opcion=input ("Ingrese la opción que desea: ")
        os.system('cls')
        if opcion in menu:
              if opcion=='5':
                   eval(menu[opcion])
                   break
              else:
                   eval(menu[opcion])
        else:
             print ("Ha ingresado una opción incorrecta, por favor, ingrese una opción nuevamente")
        aux=input("\nIngrese cualquier tecla para continuar\n")