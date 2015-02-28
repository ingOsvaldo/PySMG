#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 06/09/2013

@author: Osvaldo Cesar Trujillo Torres
'''

__license__   = 'GPL v3'
__copyright__ = '2014, Osvaldo Cesar Trujillo Torres <osvaldo.trujillo.ingenieria@gmail.com>'

import pygtk
pygtk.require("2.0")
import gtk
import os

import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import multiprocessing
from multiprocessing import Queue, Process
from Archivo import leer


class Plot():
    def __init__(self, ruta):
        self.ruta = ruta
        self.UNAM = u"Universidad Nacional Autónoma de México \n Instituto de Geofísica\n"
        self.MONITOR = u"Monitor de Neutrones de la Ciudad de México"
        self.EJEX = "Tiempo Local"
        self.PYGMS = "PyGMS"
        #self.resolucion = resolucion 
          
    def Call_GraficaTodas(self, resolucion):
        p = Process(target=self.GraficaTodas, args=(self.ruta, resolucion))
        p.start()        
        
    def Call_GraficaFechas(self,FechaDe, FechaHasta, resolucion):
        p = Process(target=self.GraficaFechas, args=(self.ruta, FechaDe, FechaHasta, resolucion))
        p.start()
        
    def GraficaTodas(self, *args):
        #print "Nuevo proceso lanzado ", "PID: ", os.getpid() 
        
        path = args[0]
        resolucion = args[1]
        if ((resolucion == 1) or (resolucion == 5) or (resolucion == 30)):
            EJEY = "Cuentas / "+ str(resolucion) +" min"
        elif(resolucion == 60):
            EJEY = "Cuentas / 1 hora"
        else:
            EJEY = u"Cuentas / 1 día"
        
    
        datos = leer(path)
        x = []
        y = []
        fechas = []
        
        contador = 0
        a = []
        b = []
        c = []
        
        for dato in datos:
            a.append(dato[0:10])
            b.append(dato[11:16])
            c.append(int(dato[20:]))
            
            
        while contador < len(datos):
            i = 0
            cuentas = 0
            
            while i < resolucion:
                if contador < len(datos):            
                    cuentas += c[contador]
                    i += 1
                    contador += 1
                else:
                    break
                
            y.append(cuentas)
            tmp = a[contador - 1] + b[contador - 1]
            fecha = datetime.datetime.strptime(tmp, "%Y-%m-%d%H:%M")
            x.append(mdates.date2num(fecha))
            fechas.append(tmp)
            
        strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10])
            
        plt.figure(self.PYGMS)
        
        plt.xticks(size = 'small', rotation = 25)
        plt.grid(which = 'major', axis = 'both')
        plt.xlabel(self.EJEX, size = 22)
        plt.ylabel(EJEY, size = 22)
        plt.suptitle(self.UNAM, size = 15)
        plt.title(self.MONITOR, size = 12)
        plt.plot_date(x, y, ",", label = strFechas, xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
        plt.legend()
        plt.minorticks_on()
        
        plt.show()    
        #print "Nuevo proceso detenido ", "PID: ", os.getpid()
        
    def GraficaFechas(self,*args):
        
        path = args[0]
        fechade = args[1]
        fechahasta = args[2]
        resolucion = args[3]
        
        
        if ((resolucion == 1) or (resolucion == 5) or (resolucion == 30)):
            EJEY = "Cuentas / "+ str(resolucion) +" min"
        elif(resolucion == 60):
            EJEY = "Cuentas / 1 hora"
        else:
            EJEY = u"Cuentas / 1 día"
            
        print "todo iniciado"
        
        try:
            datos = leer(path)
            i = 0
            j = 0
            x = []
            y = []
            fechas = []
            
            for elemento in datos:        
                if fechade in elemento:
                    break
                i = i + 1
                
            for elemento in datos:
                if fechahasta in elemento:
                    break
                j = j + 1
                
            lista = datos[i:(j + 1)]
            
            contador = 0
            a = []
            b = []
            c = []
            
            for dato in lista:
                a.append(dato[0:10])
                b.append(dato[11:16])
                c.append(int(dato[20:]))
                
            while contador < len(lista):
                i = 0
                cuentas = 0
                
                while i < resolucion:
                    if contador < len(lista):            
                        cuentas += c[contador]
                        i += 1
                        contador += 1
                    else:
                        break
                    
                y.append(cuentas)
                tmp = a[contador - 1] + b[contador - 1]
                fecha = datetime.datetime.strptime(tmp, "%Y-%m-%d%H:%M")
                x.append(mdates.date2num(fecha))
                fechas.append(tmp)
                
            strFechas = str(fechas[0][0:10]) + " a " + str(fechas[-1][0:10])
                
            plt.figure(self.PYGMS)
            
            plt.xticks(size = "small", rotation = 25)
            plt.grid(which = "major", axis = "both")
            plt.xlabel(self.EJEX, size = 22)
            plt.ylabel(EJEY, size = 22)
            plt.suptitle(self.UNAM, size = 15)
            plt.title(self.MONITOR, size = 12)
            plt.plot_date(x, y, ",", label = strFechas, xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
            plt.legend()
            plt.minorticks_on()
        
        except:
            dialogo = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK)
            dialogo.set_markup("<b>Parametros incorrectos</b>")
            dialogo.format_secondary_markup(u"Selecciona fechas validas")
            dialogo.run()
            dialogo.destroy()
            
        plt.show()