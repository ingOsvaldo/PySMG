#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 29/08/2013

@author: Osvaldo Cesar Trujillo Torres
@copyright: 2014, Osvaldo Cesar Trujillo Torres
@contact: <osvaldo.trujillo.ingenieria@gmail.com>
@license: GNU/GPL v3
@version: 2.0
'''

__license__   = 'GPL v3'
__copyright__ = '2014, Osvaldo Cesar Trujillo Torres <osvaldo.trujillo.ingenieria@gmail.com>'


def leer(ruta):
    '''
    Función que lee el archivo de datos del Monitor de Neutrones de la Ciudad de México.
    
    Esta función recibe como parámetro la ruta del archivo de datos elegido por el usuario
    y devuelve el contenido de dicho archivo.
    
    @param ruta: recibe la ruta del archivo de datos.
    '''
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
    '''
    Función que lee el archivo de datos del Telescopio de Neutrones solares.
    
    Esta función recibe como parámetro la ruta del archivo de datos elegido por el usuario
    y devuelve el contenido de dicho archivo.
    
    @param files: recibe la ruta del archivo de datos.
    '''
    files = [files]
    datos = []
    
    if len(files) == 1:
        archivo = open(files[0], "r")
        lineas = archivo.readlines()
        archivo.close()
        datos = lineas[5:-1]       
                
    return datos



def setFecha(ruta, tipo_archivo):
    '''
    Función que establece el arreglo de fechas de un archivo de datos.
    
    @param ruta: recibe la ruta del archivo de datos.
    @param tipo_archivo: recibe el tipo de archivo de datos.
    '''
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
    '''
    Función que establece el arreglo de horas de un archivo de datos.
    
    @param ruta: recibe la ruta del archivo de datos.
    @param tipo_archivo: recibe el tipo de archivo de datos.
    '''
    
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
    '''
    Función que identifia los ceros (0) que contiene un archivo.
    
    Actualmente no se usa.
    '''
    contador = 0
    
    for n in lista:
        if n == 0:
            del lista[contador]
        
        contador += 1
            
    return lista
    
    