import numpy as np
import matplotlib.pyplot as plt
import cv2

class Image():
    def __init__(self):
        self.__Img = self.Img_O()
        self.__M_Img = self.Binarizacion()
        self.__D_Img = self.Dilatacion()

    def Img_O():
        dir = input("Ingrese la dirección de la imágen a cargar: ")
        Img = cv2.imread(dir)
        Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)
        
    def Ver_Img(self):
         plt.figure(figsize=(15,6))
         plt.imshow(self.__Img)
    
    def Binarizacion(self):
        img = self.__Img
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mitad = np.mean(img)
        self.__M_Img = cv2.threshold(img, mitad, 255, cv2.THRESH_BINARY)
        
    
    def Dilatacion(self):
        loops = int(input("Ingrese el número de iteraciones: "))
        col = int(input("Ingrese la cantidad de columnas del kernel: "))
        rows = int(input("Ingrese la cantidad de filas del kernel: "))
        ker = np.ones([rows, col])

        self.__D_Img = cv2.dilatate(self.__M_Img, ker, loops)
