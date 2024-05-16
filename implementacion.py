from funciones import *

def main():
    while True:
        print("Bienvenido al sistema X!\nEste le permitirá hacer un conteo aproximádo de celulas mediante imágenes,\nasí como la visualización de los archivos dicom de un paciente ")
        menu = int(input("Seleccione la acción que desea ejecutar:\n 1.Conteo de células\n 2.Visualización de archivos dicom\n 3.Salir del sistema"))
        if menu ==1:
            pass
        if menu==2:
            pass
        if menu==3:
            op1_3 = int(input("¿Desea cerrar el programa?:\n 1.Si\n 2.No\n Usted eligió: "))
            if op1_3 == 1: 
                break
            if op1_3 == 2:
                continue
            else:
                print("Por favor ingrese una opción válida")
                continue
   

