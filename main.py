from funciones import *
while True:
    x=int(input("seleccione 1 para un conteo celular en imágenes de formato .png y .jpg\n seleccione 2 para visualizar imágenes de formato .dcm\n seleccione 3 para salir" ))
    if x==1:
        binary_image = binarizar_imagen()
        conteo = count_cells(binary_image)
        grafica(binary_image[1], binary_image[0])
    elif x==2:
        directory = input("ingrese la ruta de los archivos")
        dicom_list = obtener_archivos_dcm(directory)
        mostrar_imagenes_dicom(dicom_list)

        print(f"Se cargaron {len(dicom_list)} archivos DICOM.")
    elif x==3:
        break
     