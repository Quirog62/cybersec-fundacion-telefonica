from PIL import Image
from io import BytesIO
import binascii

def ocultarImagen(imagenCubierta,imagenVisible,imagenOculta):
    cubierta = open(imagenCubierta,'wb')
    cubierta.write(open(imagenVisible,'rb').read())
    #Se va a guardar la frase 'SUPER SECRETO' en la imagen, que luego me va ayudar a encontrar la imagen oculta
    textoOcultoBytes = b'\x53\x55\x50\x45\x52\x20\x53\x45\x43\x52\x45\x54\x4f'
    cubierta.write(textoOcultoBytes)
    cubierta.write(open(imagenOculta,'rb').read())
    cubierta.close()

def recuperarImagen(imagen):
    with open(imagen, 'rb') as img_bin:
        buff = BytesIO()
        buff.write(img_bin.read())
        buff.seek(0)
        bytesarray = buff.read()
        #Busco la frase 'SUPER SECRETO' en la cubierta y hago un split
        img = bytesarray.split(b"\x53\x55\x50\x45\x52\x20\x53\x45\x43\x52\x45\x54\x4f")[1] + b"\x53\x55\x50\x45\x52\x20\x53\x45\x43\x52\x45\x54\x4f"
        img_out = BytesIO()
        img_out.write(img)
        img = Image.open(img_out)
        img.show()

print("(1) Ocultar una imagen dentro de otra")
print("(2) Recuperar una imagen escondida")
opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    image1 = input("Ingrese el nombre de la imagen que se usara como salida: ")
    image2 = input("Ingrese el nombre de la imagen que sera visible: ")
    image3 = input("Ingrese el nombre de la imagen que sera invisible:")
    ocultarImagen(image1,image2,image3)
elif opcion == 2:
    image1 = input("Ingrese el nombre de la imagen que tiene escondida otra imagen: ")
    recuperarImagen(image1)
else:
    print("INGRESASTE UNA OPCION INVALIDA!!!")



