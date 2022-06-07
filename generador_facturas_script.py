#BIOHAZARD86
#BILLS.PDF GENERATOR FROM CSV

import sys
import json
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import random


def error_exit(message):
    sys.stderr.write(message)
    sys.exit(1)

#Funcion que comprueba que una cadena no sea mayor de X numero de caracteres
#Si es mayor, la corta y le añade un ...
def comprueba_cadena(cadena):
    # comprueba si la cadena tiene mas de 50 caracteres
    if len(cadena) > 60:
        #si tiene mas de 50, cortamos la cadena y aniadimos al final "..."
        cadena = cadena[:60] + "[...]"
    return cadena
    

#Funcion que genera el template de la factura
#Es decir, pone debajo de la factura el disenio que queramos, en este caso los datos de la empresa
def template(c):
    template = ImageReader('template.png')
    c.drawImage(template, 0, 0, height=842, width=595, mask='auto')


def genera_factura(numero_factura,fecha,total,nombre,direccion_envio,ciudad_envio,provincia_envio,codigo_postal_envio):

    #Creamos el pdf
    c = canvas.Canvas("archivos/FACTURA_"+numero_factura+".pdf") 

    
    template(c)
    linea_contador = 700
    
    c.setFont("Helvetica", 9) #Fuente y tamanio
    c.drawString(88,655,numero_factura)
    c.drawString(80,644,fecha)
    c.drawString(328,linea_contador,nombre)
    ##incrementamos la linea_contador
    linea_contador = linea_contador - 10
    
    if nombre != "":
        c.drawString(328,linea_contador, nombre)
        linea_contador = linea_contador - 10


    if direccion_envio != "":
        c.drawString(328,linea_contador,direccion_envio)
        linea_contador = linea_contador - 10

    if ciudad_envio != "":
        c.drawString(328,linea_contador,ciudad_envio)
        linea_contador = linea_contador - 10

    if codigo_postal_envio != "":
        c.drawString(328,linea_contador,codigo_postal_envio)
    linea_contador = linea_contador - 10  

    if provincia_envio != "":
        c.drawString(328,linea_contador, provincia_envio)
        linea_contador = linea_contador - 10





    c.setFont("Helvetica", 13) #choose your font type and font size
    c.drawString(70,564,"Descripción")
    c.drawString(350,564,"Precio")
    c.drawString(420,564,"Cantidad")
    c.drawString(510,564,"Total")
    c.setFont("Helvetica", 9) #choose your font type and font size
    #c.drawString(45,514,comprueba_cadena(producto))
    c.drawString(45,514,"*PRODUCTO*")
    c.drawString(355,514,total)
    c.drawString(435,514,"*CANTIDAD*")
    c.drawString(515,514,total)
    c.drawString(473,293,total)
    c.drawString(473,250,total)



    #limpiamos todas las variables
    numero_factura = ""
    fecha = ""
    total = ""
    nombre = ""
    direccion_envio = ""
    ciudad_envio = ""
    provincia_envio = ""
    codigo_postal_envio = ""
    



    """
    c.drawString(100,700,"FECHA")
    c.drawString(200,700,fecha)
    c.drawString(100,650,"MONEDA")
    c.drawString(200,650,moneda)
    c.drawString(100,600,"SUBTOTAL")
    c.drawString(200,600,subtotal)
    c.drawString(100,550,"ENVIO")
    c.drawString(200,550,envio)
    c.drawString(100,500,"IMPUESTOS")
    c.drawString(200,500,impuestos)
    c.drawString(100,450,"TOTAL")
    c.drawString(200,450,total)
    c.drawString(100,400,"CANTIDAD")
    c.drawString(200,400,cantidad)
    c.drawString(100,350,"PRODUCTO")
    c.drawString(200,350,producto)
    c.drawString(100,300,"PRECIO")
    c.drawString(200,300,precio_producto)
    c.drawString(100,250,"NOMBRE")
    c.drawString(200,250,nombre_facturacion)
    c.drawString(100,200,"DIRECCION")
    c.drawString(200,200,direccion_facturacion)
    c.drawString(100,150,"CODIGO POSTAL")
    c.drawString(200,150,codigo_postal)
    c.drawString(100,100,"PAIS")
    c.drawString(200,100,pais)
    c.drawString(100,50,"TELEFONO")
    c.drawString(200,50,telefono)
    """

    c.save()





def sacar_datos_linea(linea):

    numero_factura = linea[0]
    fecha = linea[1]
    total = linea[2]
    nombre = linea[3]
    direccion_envio = linea[4]
    ciudad_envio = linea[5]
    provincia_envio = linea[6]
    codigo_postal_envio = linea[7]
    

    #enviamos a la funcion los datos que hemos sacado de cada campo.
    genera_factura(numero_factura,fecha,total,nombre,direccion_envio,ciudad_envio,provincia_envio,codigo_postal_envio)




#No se usa, usamos CSV
def leer_json():
    # read file
    f = open('datos.json')

    json_data = json.load(f)


    #pruebas>
    sacar_datos_linea(json_data[0])
    sacar_datos_linea(json_data[1])
    sacar_datos_linea(json_data[2])

    f.close()



#Abre el archivo de datos y va leyendo linea a linea y pasandolo a la funcion que saca los datos de cada linea
def leer_archivo():
    # Leemos el archivo linea a linea y lo guardamos en una lista
    with open('datos.csv','r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        total_acumulador = 0
        
        for row in spamreader:
            #print(', '.join(row))
            data = list(row)
            print("----------------------------------------------------")
            print(data)
            sacar_datos_linea(data)
            

        print("----------------------------------------------------")
        sys.stdout.write("\n")
        sys.stdout.write("SUMA TOTAL FACTURAS:")
        sys.stdout.write(str(total_acumulador))
        sys.stdout.write("\n")

    return total_acumulador

    

    
def main():
    #llamada a la funcion de ejemplo con datos de prueba
    #genera_factura('123456789', 'juan@gmail.com', '2018-01-01', 'EUR', '10.00', '2.00', '8.00', '12.00', '1', 'producto', '10.00', 'nombre', 'direccion', 'codigo postal', 'pais', 'telefono', 'paypal', '21')
    
    #Llamada a la funcion que lee el archivo
    leer_archivo()
    #leemos el archivo de datos y mostramos que todo ha ido bien
    sys.stdout.write("Todo ha ido bien")



if __name__ == '__main__':
    main()