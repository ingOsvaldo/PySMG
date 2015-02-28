'''
Created on 01/09/2013

@author: Osvaldo Cesar Trujillo Torres
'''

__license__   = 'GPL v3'
__copyright__ = '2014, Osvaldo Cesar Trujillo Torres <osvaldo.trujillo.ingenieria@gmail.com>'


def leer(ruta):
    archivo = open(ruta, "r")
    lineas = archivo.readlines()
    archivo.close()
    
    contador = 0
    y = lineas[6:]
    
    while contador < len(y):
        tmp = int(y[contador][20:])
        if tmp == 0:
            del y[contador]
            contador -= 1
            
        contador += 1
    
    return y

def setFecha(ruta):
    archivo = open(ruta, "r")
    lineas = archivo.readlines()
    archivo.close()
    
    datos = lineas[6:]
    
    
    fechas = ["Seleccione una fecha"]
    indice = 0
    
    for i in datos:
        temp = i[0:10]
        
        if fechas[indice] != temp:            
            fechas.append(temp)
            indice += 1
            
    return fechas


def setHora(ruta):
    archivo = open(ruta, "r")
    lineas = archivo.readlines()
    archivo.close()
    
    datos = lineas[6:]
    
    horas = ['Seleccione una hora']
    indice = 0
    
    for i in datos:
        temp = i[11:16]
        
        if horas[indice] != temp:
            horas.append(temp)
            indice = indice + 1
            if temp == "23:59":
                break
    
    return horas


def ceros(lista):
    contador = 0
    
    for n in lista:
        if n == 0:
            del lista[contador]
        
        contador += 1
            
    return lista
    
    