import os
import pydicom
import matplotlib.pyplot as plt
import cv2
import numpy as np
  
def obtener_archivos_dcm(ruta_carpeta):
    lista_archivos_dcm = []

    for raiz, archivos in os.walk(ruta_carpeta):
        archivos = sorted(archivos, key=lambda x: int(x.split('-')[-1].split('.')[0]))
        for nombre_archivo in archivos:
            if nombre_archivo.lower().endswith('.dcm'):
                ruta_completa = os.path.join(raiz, nombre_archivo)
                try:
                    archivo_dcm = pydicom.dcmread(ruta_completa)
                    lista_archivos_dcm.append(archivo_dcm)
                except Exception as e:
                    print(f"Error al leer el archivo {ruta_completa}: {e}")

    return lista_archivos_dcm

def mostrar_imagenes_dicom(archivos_dcm):
    for imagen_dcm in archivos_dcm:
        plt.imshow(imagen_dcm.pixel_array, cmap=plt.cm.bone)
        plt.title("Imagen DICOM")
        plt.show()

def Img_O():
        dir = input(r"Ingrese la dirección de la imágen a cargar: ")
        Img = cv2.imread(dir)
        if Img is not None:
            Img = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)
        else:
            print("Error: No se pudo cargar la imagen.")
        return Img

def binarizar_imagen(threshold_value=127):
    image = Img_O()
    gris = cv2.imread(image, cv2.COLOR_RGB2GRAY)
    
    _, binarizada = cv2.threshold(gris, threshold_value, 255, cv2.THRESH_BINARY)
    info = [binarizada, image]
    return info

def count_cells(binary_image):
    loops = int(input("Ingrese el número de iteraciones para la dilatación de la imágen: "))
    col = int(input("Ingrese la cantidad de columnas del kernel para la dilatación de la imágen: "))
    rows = int(input("Ingrese la cantidad de filas del kernel para la dilatación de la imágen: "))
    ker = np.ones((rows, col), np.uint8)
    d= cv2.dilate(binary_image, ker, iterations=loops)
        
    loopsE = int(input("Ingrese el número de iteraciones para la erosión de la imágen: "))
    colE = int(input("Ingrese la cantidad de columnas del kernel para la erosión de la imágen: "))
    rowsE = int(input("Ingrese la cantidad de filas del kernel para la erosión de la imágen: "))
    kerE = np.ones((rowsE, colE), np.uint8)
    imagen_cell= cv2.erode(d, kerE, iterations=loopsE)

    conteo_cell,mask=cv2.connectedComponents(imagen_cell)
    print( conteo_cell)
    return imagen_cell

def grafica(ima1, ima2):
    plt.figure(figsize=(15,6))
    plt.subplot(1,2,1)
    plt.imshow(ima1, cmap='gray', vmin=0, vmax=255)
    plt.subplot(1,2,2)
    plt.imshow(ima2, cmap='gray', vmin=0, vmax=255)
    plt.show()


# ruta_carpeta = 'C:\\Users\\samue\\OneDrive\\Escritorio\\Taller 3\\archivosDCM'
# archivos_dcm = obtener_archivos_dcm(ruta_carpeta)
# print(f"Se han encontrado {len(archivos_dcm)} archivos DICOM.")
# mostrar_imagenes_dicom(archivos_dcm)

# ruta_imagen = r'C:\Users\samue\OneDrive\Escritorio\Taller 3\Imagen célula.jpg'

#ruta imágen
#C:\Users\luisa\Documents\UdeA\Materias\2024-1\InfoII\Unidad3\Taller3\Taller3\Imagen célula.jpg

#ruta dicom
#C:\Users\luisa\Documents\UdeA\Materias\2024-1\InfoII\Unidad3\Taller3\Taller3\archivosDCM

