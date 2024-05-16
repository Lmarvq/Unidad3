import numpy as np
import matplotlib.pyplot as plt
import cv2

class Image:
    def __init__(self):
        self.__Img = None
        self.__M_Img = None
        self.__D_E_Img = None

    def Img_O(self):
        dir = input("Ingrese la dirección de la imágen a cargar: ")
        Img = cv2.imread(dir)
        if Img is not None:
            Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)
        else:
            print("Error: No se pudo cargar la imagen.")
        return Img

    def Asignar_Img(self):
        self.__Img = self.Img_O()
        
    def Ver_Img(self):
        if self.__Img is None:
            print("No hay imagen cargada.")
            return
        
        op1 = int(input("Seleccione que tantas imágenes desea graficar,\ntenga presente que en la segunda opción\n verá la imágen original y la modificada\n por dilatación y erosión, por lo que ha de\n hacer estas operaciones antes de seleccionar esta opción:\n 1. Solo una\n 2. 2 imágenes"))
        if op1 == 1:
            plt.figure(figsize=(8, 8))
            plt.imshow(self.__Img)
        elif op1 == 2:
            if self.__D_E_Img is None:
                print("No hay imagen dilatada y erosionada disponible.")
                return
            plt.figure(figsize=(16, 8))
            plt.subplot(1, 2, 1)
            plt.imshow(self.__Img)
            plt.subplot(1, 2, 2)
            plt.imshow(self.__D_E_Img, cmap='gray')
        plt.show()
    
    def Binarizacion(self):
        if self.__Img is None:
            print("No hay imagen cargada.")
            return
        
        img_gray = cv2.cvtColor(self.__Img, cv2.COLOR_RGB2GRAY)
        mitad = np.mean(img_gray)
        _, self.__M_Img = cv2.threshold(img_gray, mitad, 255, cv2.THRESH_BINARY)
        return self.__M_Img
    
    def Dilatacion_Erosion(self):
        if self.__M_Img is None:
            print("No hay imagen binarizada disponible.")
            return
        
        loops = int(input("Ingrese el número de iteraciones para la dilatación de la imágen: "))
        col = int(input("Ingrese la cantidad de columnas del kernel para la dilatación de la imágen: "))
        rows = int(input("Ingrese la cantidad de filas del kernel para la dilatación de la imágen: "))
        ker = np.ones((rows, col), np.uint8)
        self.__D_E_Img = cv2.dilate(self.__M_Img, ker, iterations=loops)
        
        loopsE = int(input("Ingrese el número de iteraciones para la erosión de la imágen: "))
        colE = int(input("Ingrese la cantidad de columnas del kernel para la erosión de la imágen: "))
        rowsE = int(input("Ingrese la cantidad de filas del kernel para la erosión de la imágen: "))
        kerE = np.ones((rowsE, colE), np.uint8)
        self.__D_E_Img = cv2.erode(self.__D_E_Img, kerE, iterations=loopsE)
        return self.__D_E_Img

i = Image()