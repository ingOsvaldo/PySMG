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


def leer_SN(files):
    files = [files]
    datos = []
    
    if len(files) == 1:
        archivo = open(files[0], "r")
        lineas = archivo.readlines()
        archivo.close()
        datos = lineas[5:-1]       
                
    return datos



def setFecha(ruta, tipo_archivo):
    fechas = ["Seleccione una fecha"]
    
    if tipo_archivo == "sn":
        archivo = open(ruta, "r")
        lineas = archivo.readlines()
        fecha1 = lineas[3][5:11]
        #fechaf = lineas[-2][3:9]
        hora1 = lineas[4][5:11]
        lineas_tmp = lineas[5:-1]
        
        if fecha1 == lineas_tmp[2][3:9]:
            fechas.append(fecha1)
            #fechas.append(fechaf)
    
    if tipo_archivo == "txt":  
        archivo = open(ruta, "r")
        lineas = archivo.readlines()
        archivo.close()
        
        datos = lineas[6:]
        indice = 0
        
        for i in datos:
            temp = i[0:10]
            
            if fechas[indice] != temp:            
                fechas.append(temp)
                indice += 1
            
    return fechas


def setHora(ruta, tipo_archivo):
    horas = ['Seleccione una hora']
    indice = 0
    
    if tipo_archivo == "sn":
        archivo = open(ruta, "r")
        lineas = archivo.readlines()
        fecha1 = lineas[3][5:11]
        fechaf = lineas[-2][3:9]
        hora1 = lineas[4][5:11]
        lineas_tmp = lineas[5:-1]
        
        for i in lineas_tmp:
            temp = i[10:14]
        
            if horas[indice][0:2] != temp[0:2]:
                horas.append(temp[0:2] + ":" + temp[2:4])
                indice = indice + 1
                if temp == "23:59":
                    break    
    
    if tipo_archivo == "txt":
        archivo = open(ruta, "r")
        lineas = archivo.readlines()
        archivo.close()
        
        datos = lineas[6:]
        
        
        
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
    
    