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

import pygtk
pygtk.require("2.0")
import gtk
import sys

from Vista import PyApp, Datos
from Archivo import leer
from Plot import *

def main_datos(w, fecha1, hora1, fecha2, hora2, fecha3, hora3, fecha4, hora4, entry, res, check):
    
    fecha1 = fecha1.entry.get_text()
    hora1 = hora1.entry.get_text()
    fecha2 = fecha2.entry.get_text()
    hora2 = hora2.entry.get_text()
    fecha3 = fecha3.entry.get_text()
    hora3 = hora3.entry.get_text()
    fecha4 = fecha4.entry.get_text()
    hora4 = hora4.entry.get_text()
    
    fechade1 = fecha1 + "\t" + hora1
    fechahasta1 = fecha2 + "\t" + hora2
    
    fechade2 = fecha3 + "\t" + hora3
    fechahasta2 = fecha4 + "\t" + hora4
    
    ruta = entry.get_text()
    
    barra = 0
    
    resolucion = res.get_active_text()
    
    g = Plot(ruta)
    
    if fecha1 == "Seleccione una fecha" or hora1 == "Seleccione una hora" or fecha2 == "Seleccione una fecha" or hora2 == "Seleccione una hora" or fecha3 == "Seleccione una fecha" or hora3 == "Seleccione una hora" or fecha4 == "Seleccione una fecha" or hora4 == "Seleccione una hora":
        dialogo = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK)
        dialogo.set_markup("<b>Parametros incorrectos</b>")
        dialogo.format_secondary_markup(u"Selecciona fechas validas para calcular datos")
        dialogo.run()
        dialogo.destroy()
    else:        
        if check.get_active():
            if resolucion == "Minima (1 minuto)":
                dato1 = media1(fechade1, fechahasta1, ruta)
                dato2 = media2(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                g.Call_GraficaFechas(fechade1, fechahasta2, 1)
                PyApp()
                gtk.main()
            elif resolucion == "5 minutos":
                dato1 = media1x5min(fechade1, fechahasta1, ruta)
                dato2 = media2x5min(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                g.Call_GraficaFechas(fechade1, fechahasta2, 5)
                PyApp()
                gtk.main()
            elif resolucion == "30 minutos":
                dato1 = media1x30min(fechade1, fechahasta1, ruta)
                dato2 = media2x30min(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                g.Call_GraficaFechas(fechade1, fechahasta2, 30)
                PyApp()
                gtk.main()
            elif resolucion == "1 hora":
                dato1 = media1x1hora(fechade1, fechahasta1, ruta)
                dato2 = media2x1hora(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                g.Call_GraficaFechas(fechade1, fechahasta2, 60)
                PyApp()
                gtk.main()
            elif resolucion == "1 dia":
                dato1 = media1x1dia(fechade1, fechahasta1, ruta)
                dato2 = media2x1dia(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                g.Call_GraficaFechas(fechade1, fechahasta2, 1440)
                PyApp()
                gtk.main()
        else:
            if resolucion == "Minima (1 minuto)":
                dato1 = media1(fechade1, fechahasta1, ruta)
                dato2 = media2(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                PyApp()
                gtk.main()
            elif resolucion == "5 minutos":
                dato1 = media1x5min(fechade1, fechahasta1, ruta)
                dato2 = media2x5min(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                PyApp()
                gtk.main()
            elif resolucion == "30 minutos":
                dato1 = media1x30min(fechade1, fechahasta1, ruta)
                dato2 = media2x30min(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                PyApp()
                gtk.main()
            elif resolucion == "1 hora":
                dato1 = media1x1hora(fechade1, fechahasta1, ruta)
                dato2 = media2x1hora(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                PyApp()
                gtk.main()
            elif resolucion == "1 dia":
                dato1 = media1x1dia(fechade1, fechahasta1, ruta)
                dato2 = media2x1dia(fechade2, fechahasta2, ruta, fechade1, fechahasta1)
                Datos(dato1, dato2)
                PyApp()
                gtk.main()
           
        
             


def media1(fechade1, fechahasta1, ruta):
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade1 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta1 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    for dato in lista:
        y.append(int(dato[20:]))
        fechas.append(dato)
        
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = float(suma) / cont
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade1[11:16] + " a " + fechahasta1[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])
    
    cadena = ("1", strFechas, round(media,2), minmax, "100%")
    
    return cadena
    
def media2(fechade2, fechahasta2, ruta, fechade1, fechahasta1):
    comp = media1(fechade1, fechahasta1, ruta)[2]
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade2 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta2 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    for dato in lista:
        y.append(int(dato[20:]))
        fechas.append(dato)
        
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = suma / float(cont)
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade2[11:16] + " a " + fechahasta2[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])   
    
    tmp = media - comp
    
    tmp1 = (tmp * 100) / comp
    
    r = round(tmp1,2)
    
    res = str(r) + "%"
    
    m = round(media,2)
    
    
    cadena = ("2", strFechas, m, minmax, res)
    
    return cadena


def media1x5min(fechade1, fechahasta1, ruta):
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade1 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta1 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    contador = 0
    c = []
    
    for dato in lista:
        c.append(int(dato[20:]))
        fechas.append(dato)
        
        
    while contador < len(lista):
        i = 0
        cuentas = 0
        
        while i < 5:
            if contador < len(lista):            
                cuentas += c[contador]
                i += 1
                contador += 1
            else:
                break
            
        y.append(cuentas)
    
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = float(suma) / cont
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade1[11:16] + " a " + fechahasta1[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])
    
    cadena = ("1", strFechas, round(media,2), minmax, "100%")
    
    return cadena


def media1x30min(fechade1, fechahasta1, ruta):
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade1 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta1 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    contador = 0
    c = []
    
    for dato in lista:
        c.append(int(dato[20:]))
        fechas.append(dato)
        
    while contador < len(lista):
        i = 0
        cuentas = 0
        
        while i < 30:
            if contador < len(lista):            
                cuentas += c[contador]
                i += 1
                contador += 1
            else:
                break
            
        y.append(cuentas)
    
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = float(suma) / cont
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade1[11:16] + " a " + fechahasta1[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])
    
    cadena = ("1", strFechas, round(media,2), minmax, "100%")
    
    return cadena


def media1x1hora(fechade1, fechahasta1, ruta):
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade1 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta1 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    contador = 0
    c = []
    
    for dato in lista:
        c.append(int(dato[20:]))
        fechas.append(dato)
        
    while contador < len(lista):
        i = 0
        cuentas = 0
        
        while i < 60:
            if contador < len(lista):            
                cuentas += c[contador]
                i += 1
                contador += 1
            else:
                break
            
        y.append(cuentas)
    
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = float(suma) / cont
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade1[11:16] + " a " + fechahasta1[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])
    
    cadena = ("1", strFechas, round(media,2), minmax, "100%")
    
    return cadena


def media1x1dia(fechade1, fechahasta1, ruta):
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade1 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta1 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    contador = 0
    c = []
    
    for dato in lista:
        c.append(int(dato[20:]))
        fechas.append(dato)
        
    while contador < len(lista):
        i = 0
        cuentas = 0
        
        while i < 1440:
            if contador < len(lista):            
                cuentas += c[contador]
                i += 1
                contador += 1
            else:
                break
            
        y.append(cuentas)
    
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = float(suma) / cont
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade1[11:16] + " a " + fechahasta1[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])
    
    cadena = ("1", strFechas, round(media,2), minmax, "100%")
    
    return cadena


def media2x5min(fechade2, fechahasta2, ruta, fechade1, fechahasta1):
    comp = media1x5min(fechade1, fechahasta1, ruta)[2]
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade2 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta2 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    contador = 0
    c = []
    
    for dato in lista:
        c.append(int(dato[20:]))
        fechas.append(dato)
        
    while contador < len(lista):
        i = 0
        cuentas = 0
        
        while i < 5:
            if contador < len(lista):            
                cuentas += c[contador]
                i += 1
                contador += 1
            else:
                break
            
        y.append(cuentas)
        
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = suma / float(cont)
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade2[11:16] + " a " + fechahasta2[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])   
    
    tmp = media - comp
    
    tmp1 = (tmp * 100) / comp
    
    r = round(tmp1,2)
    
    res = str(r) + "%"
    
    m = round(media,2)
    
    
    cadena = ("2", strFechas, m, minmax, res)
    
    return cadena


def media2x30min(fechade2, fechahasta2, ruta, fechade1, fechahasta1):
    comp = media1x30min(fechade1, fechahasta1, ruta)[2]
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade2 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta2 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    contador = 0
    c = []
    
    for dato in lista:
        c.append(int(dato[20:]))
        fechas.append(dato)
        
        
    while contador < len(lista):
        i = 0
        cuentas = 0
        
        while i < 30:
            if contador < len(lista):            
                cuentas += c[contador]
                i += 1
                contador += 1
            else:
                break
            
        y.append(cuentas)
        
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = suma / float(cont)
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade2[11:16] + " a " + fechahasta2[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])   
    
    tmp = media - comp
    
    tmp1 = (tmp * 100) / comp
    
    r = round(tmp1,2)
    
    res = str(r) + "%"
    
    m = round(media,2)
    
    
    cadena = ("2", strFechas, m, minmax, res)
    
    return cadena



def media2x1hora(fechade2, fechahasta2, ruta, fechade1, fechahasta1):
    comp = media1x1hora(fechade1, fechahasta1, ruta)[2]
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade2 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta2 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    contador = 0
    c = []
    
    for dato in lista:
        c.append(int(dato[20:]))
        fechas.append(dato)
    
        
    while contador < len(lista):
        i = 0
        cuentas = 0
        
        while i < 60:
            if contador < len(lista):            
                cuentas += c[contador]
                i += 1
                contador += 1
            else:
                break
            
        y.append(cuentas)
        
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = suma / float(cont)
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade2[11:16] + " a " + fechahasta2[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])   
    
    tmp = media - comp
    
    tmp1 = (tmp * 100) / comp
    
    r = round(tmp1,2)
    
    res = str(r) + "%"
    
    m = round(media,2)
    
    
    cadena = ("2", strFechas, m, minmax, res)
    
    return cadena


def media2x1dia(fechade2, fechahasta2, ruta, fechade1, fechahasta1):
    comp = media1x1dia(fechade1, fechahasta1, ruta)[2]
    datos = leer(ruta)
    i = 0
    j = 0
    y = []
    fechas = []
    cont = 0
    
    for elemento in datos:        
        if fechade2 in elemento:
            break
        i = i + 1
        
    for elemento in datos:
        if fechahasta2 in elemento:
            break
        j = j + 1
        
    lista = datos[i:(j + 1)]
    
    contador = 0
    c = []
    
    for dato in lista:
        c.append(int(dato[20:]))
        fechas.append(dato)
        
        
    while contador < len(lista):
        i = 0
        cuentas = 0
        
        while i < 1440:
            if contador < len(lista):            
                cuentas += c[contador]
                i += 1
                contador += 1
            else:
                break
            
        y.append(cuentas)
        
    suma = 0
    
    for i in y:
        suma += i
        cont += 1
        
    media = suma / float(cont)
            
    strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10] + "\n\t   " + fechade2[11:16] + " a " + fechahasta2[11:16])
    
    y.sort()
    
    minmax = str(y[0]) + "/" + str(y[-1])   
    
    tmp = media - comp
    
    tmp1 = (tmp * 100) / comp
    
    r = round(tmp1,2)
    
    res = str(r) + "%"
    
    m = round(media,2)
    
    
    cadena = ("2", strFechas, m, minmax, res)
    
    return cadena




if __name__ == "__main__":
    sys.exit(main_datos())