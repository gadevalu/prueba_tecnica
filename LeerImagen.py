from PIL import Image 
from fpdf import FPDF

imagen= Image.open(r"D:\Universidad\Coursera\PROTECCION\Letrero.jpg")

#cubrir el 90 % del tamaño de la hoja, en caso de que la imagen supere el tamaño
AnchoA4= 716
VerticalA4= 1123
sizecurrent=imagen.size

if sizecurrent[0]>AnchoA4 or sizecurrent[1]>VerticalA4:
    relacionaspecto = sizecurrent[0]/sizecurrent[1]

    #Saber Orientación de la Imagen: "ancho mayor a alto es horizontal"
    if sizecurrent[0]>sizecurrent[1]:
        nuevoancho = int(round(AnchoA4 * relacionaspecto, 0))
        imagen = imagen.resize((nuevoancho, AnchoA4))
    else :
        nuevoalto = int(round(AnchoA4 * relacionaspecto, 0))
        imagen = imagen.resize((nuevoalto, AnchoA4))
imagen.show() 