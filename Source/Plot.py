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
from Archivo import *


class Plot():
    def __init__(self, ruta):
        self.ruta = ruta
        self.UNAM = u"Universidad Nacional Autónoma de México \n Instituto de Geofísica\n"
        self.MONITOR = u"Monitor de Neutrones de la Ciudad de México"
        self.EJEX = "Tiempo Local"
        self.PySMG = "PySMG"
        #self.resolucion = resolucion 
          
    def Call_GraficaTodas(self, resolucion, tipo_archivo, canales):
        if tipo_archivo == "txt":
            p = Process(target=self.GraficaTodas, args=(self.ruta, resolucion))
            p.start()
        if tipo_archivo == "sn":
            p = Process(target=self.GraficaTodasSN, args=(self.ruta, resolucion, canales))
            p.start()        
        
    def Call_GraficaFechas(self,FechaDe, FechaHasta, resolucion, tipo_archivo, canales):
        if tipo_archivo == "txt":
            p = Process(target=self.GraficaFechas, args=(self.ruta, FechaDe, FechaHasta, resolucion))
            p.start()
        if tipo_archivo == "sn":
            p = Process(target=self.GraficaFechasSN, args=(self.ruta, FechaDe, FechaHasta, resolucion, canales))
            p.start()
            
    def GraficaTodas(self, *args):        
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
            
        plt.figure(self.PySMG)
        
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
                
            plt.figure(self.PySMG)
            
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
        
    def GraficaTodasSN(self, *args):
        path = args[0]
        resolucion = args[1]
        canales = args[2]
                
        datos = leer_SN(path)
        x = []
        s1_anti = []
        s2_anti = []
        s3_anti = []
        s4_anti = []
        s1 = []
        s2 = []
        s3 = []
        s4 = []
        fechas = []
        
        contador = 0
        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        i = []
        j = []
        
        for dato in datos:
            date = dato[3:9]
            da = "20"+date[0:2]+"-"+date[2:4]+"-"+date[4:6]
            a.append(da)
            hour = dato[10:16]
            ho = hour[0:2]+":"+hour[2:4]+":"+hour[4:6]
            b.append(ho)
            c.append(int(dato[17:22]))
            d.append(int(dato[23:27]))
            e.append(int(dato[28:32]))
            f.append(int(dato[33:36]))
            g.append(int(dato[37:42]))
            h.append(int(dato[43:48]))
            i.append(int(dato[49:53]))
            j.append(int(dato[54:58]))
            
            
        while contador < len(datos):
            ii = 0
            cuentasS1_anti = 0
            cuentasS2_anti = 0
            cuentasS3_anti = 0
            cuentasS4_anti = 0
            cuentasS1 = 0
            cuentasS2 = 0
            cuentasS3 = 0
            cuentasS4 = 0
            
            while ii < resolucion:
                if contador < len(datos):            
                    cuentasS1_anti += c[contador]
                    cuentasS2_anti += d[contador]
                    cuentasS3_anti += e[contador]
                    cuentasS4_anti += f[contador]
                    cuentasS1 += g[contador]
                    cuentasS2 += h[contador]
                    cuentasS3 += i[contador]
                    cuentasS4 += j[contador]
                    ii += 1
                    contador += 1
                else:
                    break
                
            s1_anti.append(cuentasS1_anti)
            s2_anti.append(cuentasS2_anti)
            s3_anti.append(cuentasS3_anti)
            s4_anti.append(cuentasS4_anti)
            s1.append(cuentasS1)
            s2.append(cuentasS2)
            s3.append(cuentasS3)
            s4.append(cuentasS4)
            tmp = a[contador - 1] + b[contador - 1]
            fecha = datetime.datetime.strptime(tmp, "%Y-%m-%d%H:%M:%S")
            x.append(mdates.date2num(fecha))
            fechas.append(tmp)
            
        strFechasDe = "De: "+str(fechas[0][0:4])+"/"+str(fechas[0][5:7])+"/"+str(fechas[0][8:10]) 
        strFechasHasta = " A: "+str(fechas[-2][0:4])+"/"+str(fechas[-2][5:7])+"/"+str(fechas[-2][8:10])
        strFechas = strFechasDe + strFechasHasta
        
        if canales['s1a'] == 1 or canales['s2a'] == 1 or canales['s3a'] == 1 or canales['s4a'] == 1:
            cantidadConAnti = 0
            
            if canales['s1a'] == 1:
                cantidadConAnti += 1
            if canales['s2a'] == 1:
                cantidadConAnti += 1
            if canales['s3a'] == 1:
                cantidadConAnti += 1
            if canales['s4a'] == 1:
                cantidadConAnti += 1
            
            graficaConAnti = 1
            
            f1 = plt.figure("PySMG - Telescopio de Neutrones Solares - 1")
            f1.suptitle(strFechas, size = 15)
            
            if canales['s1a'] == 1:
                ax = plt.subplot(cantidadConAnti, 1, graficaConAnti)
                ax.grid(which = "major", axis = "x")
                ax.plot_date(x, s1_anti, ",", label = "s1_anti", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                ax.legend()
                graficaConAnti +=1
            
            if canales['s2a'] == 1:
                ax = plt.subplot(cantidadConAnti, 1, graficaConAnti)
                ax.grid(which = "major", axis = "x")
                ax.plot_date(x, s2_anti, ",", label = "s2_anti", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                ax.legend()
                graficaConAnti += 1
            
            if canales['s3a'] == 1:
                ax = plt.subplot(cantidadConAnti, 1, graficaConAnti)
                ax.grid(which = "major", axis = "x")
                ax.plot_date(x, s3_anti, ",", label = "s3_anti", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                ax.legend()
                graficaConAnti += 1
            
            if canales['s4a'] == 1:
                ax = plt.subplot(cantidadConAnti, 1, graficaConAnti)
                ax.grid(which = "major", axis = "x")
                ax.plot_date(x, s4_anti, ",", label = "s4_anti", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                ax.legend()
                graficaConAnti += 1
        
        if canales['s1'] == 1 or canales['s2'] == 1 or canales['s3'] == 1 or canales['s4'] == 1:
            cantidadSinAnti = 0
            
            if canales['s1'] == 1:
                cantidadSinAnti += 1
            if canales['s2'] == 1:
                cantidadSinAnti += 1
            if canales['s3'] == 1:
                cantidadSinAnti += 1
            if canales['s4'] == 1:
                cantidadSinAnti += 1
            
            graficaSinAnti = 1
            
            f2 = plt.figure("PySMG - Telescopio de Neutrones Solares - 2")
            f2.suptitle(strFechas, size = 15)
            
            if canales['s1'] == 1:
                ax2 = plt.subplot(cantidadSinAnti, 1, graficaSinAnti)
                ax2.grid(which = "major", axis = "x")
                ax2.plot_date(x, s1, ",", label = "s1", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                ax2.legend()
                graficaSinAnti += 1
            
            if canales['s2'] == 1:
                ax2 = plt.subplot(cantidadSinAnti, 1, graficaSinAnti)
                ax2.grid(which = "major", axis = "x")
                ax2.plot_date(x, s2, ",", label = "s2", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                ax2.legend()
                graficaSinAnti += 1
            
            if canales['s3'] == 1:
                ax2 = plt.subplot(cantidadSinAnti, 1, graficaSinAnti)
                ax2.grid(which = "major", axis = "x")
                ax2.plot_date(x, s3, ",", label = "s3", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                ax2.legend()
                graficaSinAnti += 1
            
            if canales['s4'] == 1:
                ax2 = plt.subplot(cantidadSinAnti, 1, graficaSinAnti)
                ax2.grid(which = "major", axis = "x")
                ax2.plot_date(x, s4, ",", label = "s4", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                ax2.legend()       
                graficaSinAnti += 1     
        
        plt.show()
        
        
    def GraficaFechasSN(self, *args):
    
        path = args[0]
        fechade = args[1][0:6] + " " + args[1][7:9] + args[1][10:12]
        fechahasta = args[2][0:6] + " " + args[2][7:9] + args[2][10:12]
        resolucion = args[3]
        canales = args[4]
        
        
        try:
            datos = leer_SN(path)
            i = 0
            j = 0
            x = []
            s1_anti = []
            s2_anti = []
            s3_anti = []
            s4_anti = []
            s1 = []
            s2 = []
            s3 = []
            s4 = []
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
            d = []
            e = []
            f = []
            g = []
            h = []
            i = []
            j = []
            
            for dato in lista:
                date = dato[3:9]
                da = "20"+date[0:2]+"-"+date[2:4]+"-"+date[4:6]
                a.append(da)
                hour = dato[10:16]
                ho = hour[0:2]+":"+hour[2:4]+":"+hour[4:6]
                b.append(ho)
                c.append(int(dato[17:22]))
                d.append(int(dato[23:27]))
                e.append(int(dato[28:32]))
                f.append(int(dato[33:36]))
                g.append(int(dato[37:42]))
                h.append(int(dato[43:48]))
                i.append(int(dato[49:53]))
                j.append(int(dato[54:58]))
            
            
            while contador < len(lista):
                ii = 0
                cuentasS1_anti = 0
                cuentasS2_anti = 0
                cuentasS3_anti = 0
                cuentasS4_anti = 0
                cuentasS1 = 0
                cuentasS2 = 0
                cuentasS3 = 0
                cuentasS4 = 0
                
                while ii < resolucion:
                    if contador < len(lista):            
                        cuentasS1_anti += c[contador]
                        cuentasS2_anti += d[contador]
                        cuentasS3_anti += e[contador]
                        cuentasS4_anti += f[contador]
                        cuentasS1 += g[contador]
                        cuentasS2 += h[contador]
                        cuentasS3 += i[contador]
                        cuentasS4 += j[contador]
                        ii += 1
                        contador += 1
                    else:
                        break
                    
                s1_anti.append(cuentasS1_anti)
                s2_anti.append(cuentasS2_anti)
                s3_anti.append(cuentasS3_anti)
                s4_anti.append(cuentasS4_anti)
                s1.append(cuentasS1)
                s2.append(cuentasS2)
                s3.append(cuentasS3)
                s4.append(cuentasS4)
                tmp = a[contador - 1] + b[contador - 1]
                fecha = datetime.datetime.strptime(tmp, "%Y-%m-%d%H:%M:%S")
                x.append(mdates.date2num(fecha))
                fechas.append(tmp)
            
            strFechasDe = "De: "+str(fechas[0][0:4])+"/"+str(fechas[0][5:7])+"/"+str(fechas[0][8:10]) 
            strFechasHasta = " A: "+str(fechas[-2][0:4])+"/"+str(fechas[-2][5:7])+"/"+str(fechas[-2][8:10])
            strFechas = strFechasDe + strFechasHasta
                        
            if canales['s1a'] == 1 or canales['s2a'] == 1 or canales['s3a'] == 1 or canales['s4a'] == 1:
                cantidadConAnti = 0
            
                if canales['s1a'] == 1:
                    cantidadConAnti += 1
                if canales['s2a'] == 1:
                    cantidadConAnti += 1
                if canales['s3a'] == 1:
                    cantidadConAnti += 1
                if canales['s4a'] == 1:
                    cantidadConAnti += 1
                
                graficaConAnti = 1
                    
                f1 = plt.figure("PySMG - Telescopio de Neutrones Solares - 1")
                f1.suptitle(strFechas, size = 15)                                
                
                if canales['s1a'] == 1:
                    ax = plt.subplot(cantidadConAnti, 1, graficaConAnti)
                    ax.grid(which = "major", axis = "x")
                    ax.plot_date(x, s1_anti, ",", label = "s1_anti", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                    ax.legend()
                    graficaConAnti += 1
                
                if canales['s2a'] == 1:
                    ax = plt.subplot(cantidadConAnti, 1, graficaConAnti)
                    ax.grid(which = "major", axis = "x")
                    ax.plot_date(x, s2_anti, ",", label = "s2_anti", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                    ax.legend()
                    graficaConAnti += 1
                
                if canales['s3a'] == 1:
                    ax = plt.subplot(cantidadConAnti, 1, graficaConAnti)
                    ax.grid(which = "major", axis = "x")
                    ax.plot_date(x, s3_anti, ",", label = "s3_anti", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                    ax.legend()
                    graficaConAnti += 1
                
                if canales['s4a'] == 1:
                    ax = plt.subplot(cantidadConAnti, 1, graficaConAnti)
                    ax.grid(which = "major", axis = "x")
                    ax.plot_date(x, s4_anti, ",", label = "s4_anti", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                    ax.legend()
                    graficaConAnti += 1
            
            
            if canales['s1'] == 1 or canales['s2'] == 1 or canales['s3'] == 1 or canales['s4'] == 1:
                cantidadSinAnti = 0
                
                if canales['s1'] == 1:
                    cantidadSinAnti += 1
                if canales['s2'] == 1:
                    cantidadSinAnti += 1
                if canales['s3'] == 1:
                    cantidadSinAnti += 1
                if canales['s4'] == 1:
                    cantidadSinAnti += 1
                
                graficaSinAnti = 1
                
                f2 = plt.figure("PySMG - Telescopio de Neutrones Solares - 2")
                f2.suptitle(strFechas, size = 15)
                
                if canales['s1'] == 1:
                    ax2 = plt.subplot(cantidadSinAnti, 1, graficaSinAnti)
                    ax2.grid(which = "major", axis = "x")
                    ax2.plot_date(x, s1, ",", label = "s1", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                    ax2.legend()
                    graficaSinAnti += 1
                
                if canales['s2'] == 1:
                    ax2 = plt.subplot(cantidadSinAnti, 1, graficaSinAnti)
                    ax2.grid(which = "major", axis = "x")
                    ax2.plot_date(x, s2, ",", label = "s2", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                    ax2.legend()
                    graficaSinAnti += 1
                
                if canales['s3'] == 1:
                    ax2 = plt.subplot(cantidadSinAnti, 1, graficaSinAnti)
                    ax2.grid(which = "major", axis = "x")
                    ax2.plot_date(x, s3, ",", label = "s3", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                    ax2.legend()
                    graficaSinAnti += 1
                
                if canales['s4'] == 1:
                    ax2 = plt.subplot(cantidadSinAnti, 1, graficaSinAnti)
                    ax2.grid(which = "major", axis = "x")
                    ax2.plot_date(x, s4, ",", label = "s4", xdate = True, linestyle = "-", color = "g", drawstyle = "steps")
                    ax2.legend()
                    graficaSinAnti += 1
            
            plt.show()
            
        except:
            dialogo = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK)
            dialogo.set_markup("<b>Parametros incorrectos</b>")
            dialogo.format_secondary_markup(u"Selecciona fechas validas")
            dialogo.run()
            dialogo.destroy()