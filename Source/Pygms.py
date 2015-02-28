#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 29/08/2013

@author: Osvaldo Cesar Trujillo Torres
'''

__license__   = 'GPL v3'
__copyright__ = '2014, Osvaldo Cesar Trujillo Torres <osvaldo.trujillo.ingenieria@gmail.com>'

import pygtk
pygtk.require("2.0")
import gtk
import os

from Archivo import setFecha, setHora, leer
from Plot import *
from Ayuda import main
from Datos import main_datos

class Pygms():
    '''
    Clase principal
    '''


    def __init__(self):
        '''
        Constructor de la interfaz gráfica
        '''
#AJUSTES DE LA VENTANA
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_resizable(0)
        self.window.set_title("PyGMS - Instituto de Geofísica")
        
#VBOX
        vbox = gtk.VBox(False, 0)
        vbox1 = gtk.VBox(False, 0)
        vbox1.set_border_width(10)
        
        hbox = gtk.HBox(False, 5)
        
        vbox.pack_end(vbox1)
        vbox1.pack_end(hbox)
        
#MENU
        menu_bar = gtk.MenuBar()
        
        #MENU ARCHIVO
        archivo = gtk.Menu()
        abrir_menu_archivo = gtk.MenuItem("Abrir...")
        exportar_menu_archivo = gtk.MenuItem("Exportar...")
        salir_menu_archivo = gtk.MenuItem("Salir")
        
        archivo.append(abrir_menu_archivo)
        archivo.append(exportar_menu_archivo)
        archivo.append(salir_menu_archivo)
        
        salir_menu_archivo.connect("activate", self.destruir)
        
        abrir_menu_archivo.show()
        exportar_menu_archivo.show()
        exportar_menu_archivo.set_sensitive(False)
        salir_menu_archivo.show()
        
        menu_archivo = gtk.MenuItem("Archivo")
        menu_archivo.show()
        menu_archivo.set_submenu(archivo)                
        
        #MENU AYUDA
        ayuda = gtk.Menu()
        acerca_menu_ayuda = gtk.MenuItem("Acerca de...")
                
        ayuda.append(acerca_menu_ayuda)        
        
        acerca_menu_ayuda.connect("activate", main)
        
        acerca_menu_ayuda.show()
        
        menu_ayuda = gtk.MenuItem("Ayuda")
        menu_ayuda.show()
        menu_ayuda.set_submenu(ayuda)
        
        #MOSTRAR MENUS EN LA BARRA
        menu_bar.append(menu_archivo)
        menu_bar.append(menu_ayuda)
        
        #MOSTRAR LA BARRA DE MENU EN LA VENTANA
        vbox.pack_start(menu_bar)
        
        
#FRAMES
        frame_examinar = gtk.Frame()        
        frame_fechas = gtk.Frame()
        frame_fechas.set_sensitive(False)
        frame_resolucion = gtk.Frame()
        frame_resolucion.set_sensitive(False)
        frame_estadistica = gtk.Frame()
        frame_estadistica.set_sensitive(False)
        frame_botonera = gtk.Frame()
        #ETIQUETAS
        frame_examinar.set_label("Archivo de Datos")
        frame_fechas.set_label("Fechas")
        frame_resolucion.set_label("Resolución")
        frame_estadistica.set_label("Estadistica")
        frame_botonera.set_label("")
        #MOSTRAR FRAMES
        vbox1.pack_start(frame_examinar)
        vbox1.pack_start(frame_fechas)
        vbox1.pack_start(frame_resolucion)
        vbox1.pack_start(frame_estadistica)
        vbox1.pack_start(frame_botonera)
        
#FRAME EXAMINAR
        tabla_examinar = gtk.Table(2, 6, gtk.TRUE)
        tabla_examinar.set_border_width(5)
        tabla_examinar.set_row_spacings(2)
        tabla_examinar.set_col_spacings(2)
        frame_examinar.add(tabla_examinar)
        
        lbl_examinar = gtk.Label("Examinar: ")
        tabla_examinar.attach(lbl_examinar, 0, 1, 0, 1)
        
        txt_examinar = gtk.Entry()
        tabla_examinar.attach(txt_examinar, 1, 6, 0, 1)
        
        btn_examinar = gtk.Button("Examinar...")
        btn_examinar.connect("clicked", self.abrir, txt_examinar)
        tabla_examinar.attach(btn_examinar, 5, 6, 1, 2)
        
        btn_cargar = gtk.Button("Cargar")
        tabla_examinar.attach(btn_cargar, 4, 5, 1, 2)
        
#FRAME FECHAS
        tabla_fechas = gtk.Table(4, 3, gtk.TRUE)
        tabla_fechas.set_border_width(5)
        tabla_fechas.set_row_spacings(2)
        tabla_fechas.set_col_spacings(2)
        frame_fechas.add(tabla_fechas)
        
        radio_todas = gtk.RadioButton(None, "Graficar todas las fechas")
        tabla_fechas.attach(radio_todas, 0, 2, 0, 1)
        
        radio_selec = gtk.RadioButton(radio_todas, "Seleccionar fechas: ")
        tabla_fechas.attach(radio_selec, 0, 2, 1, 2)
        
        lbl_de = gtk.Label("De: ")
        lbl_de.set_alignment(1, 0)
        tabla_fechas.attach(lbl_de, 0, 1, 2, 3)
        
        lbl_hasta = gtk.Label("Hasta: ")
        lbl_hasta.set_alignment(1, 0)
        tabla_fechas.attach(lbl_hasta, 0, 1, 3, 4)
        
        combo_fecha_de = gtk.Combo()
        combo_fecha_de.set_sensitive(False)
        tabla_fechas.attach(combo_fecha_de, 1, 2, 2, 3)
        
        combo_fecha_hasta = gtk.Combo()
        combo_fecha_hasta.set_sensitive(False)        
        tabla_fechas.attach(combo_fecha_hasta, 1, 2, 3, 4)
        
        combo_hora_de = gtk.Combo()
        combo_hora_de.set_sensitive(False)
        tabla_fechas.attach(combo_hora_de, 2, 3, 2, 3)
        
        combo_hora_hasta = gtk.Combo()
        combo_hora_hasta.set_sensitive(False)
        tabla_fechas.attach(combo_hora_hasta, 2, 3, 3, 4)
        
#FRAME RESOLUCION
        tabla_resolucion = gtk.Table(1, 2, gtk.TRUE)
        tabla_resolucion.set_border_width(10)
        tabla_resolucion.set_row_spacings(5)
        tabla_resolucion.set_col_spacings(5)
        frame_resolucion.add(tabla_resolucion)

        lbl_resolucion = gtk.Label("Resolución: ")
        lbl_resolucion.set_alignment(0, 1)
        tabla_resolucion.attach(lbl_resolucion, 0, 1, 0, 1)
        
        combo_resolucion = gtk.ComboBox()
        lista_resolucion = gtk.ListStore(str)
        lista_resolucion.append(["Minima (1 minuto)"])
        lista_resolucion.append(["5 minutos"])
        lista_resolucion.append(["30 minutos"])
        lista_resolucion.append(["1 hora"])
        lista_resolucion.append(["1 dia"])
        cell = gtk.CellRendererText()
        combo_resolucion.pack_start(cell)
        combo_resolucion.add_attribute(cell, "text", 0)
        combo_resolucion.set_wrap_width(1)
        combo_resolucion.set_model(lista_resolucion)
        combo_resolucion.connect("changed", self.changed)
        combo_resolucion.set_active(1)        
        tabla_resolucion.attach(combo_resolucion, 1, 2, 0, 1)
        
#FRAME ESTADISTICA
        tabla_estadistica = gtk.Table(6, 4, gtk.FALSE)
        tabla_estadistica.set_border_width(5)
        tabla_estadistica.set_row_spacings(2)
        tabla_estadistica.set_col_spacings(2)
        frame_estadistica.add(tabla_estadistica)
        
        lbl_promedio = gtk.Label("Rango:")
        lbl_promedio.set_alignment(0, 1)
        tabla_estadistica.attach(lbl_promedio, 0, 1, 0, 1)
        
        label_de = gtk.Label("De: ")
        label_de.set_alignment(1, 0)
        tabla_estadistica.attach(label_de, 0, 1, 1, 2)
        
        combo_st_ini_de_f = gtk.Combo()
        tabla_estadistica.attach(combo_st_ini_de_f, 1, 2, 1, 2)
        
        combo_st_ini_de_h = gtk.Combo()
        tabla_estadistica.attach(combo_st_ini_de_h, 2, 3, 1, 2)
        
        label_hasta = gtk.Label("Hasta: ")
        label_hasta.set_alignment(1, 0)
        tabla_estadistica.attach(label_hasta, 0, 1, 2, 3)
        
        combo_st_ini_hasta_f = gtk.Combo()
        tabla_estadistica.attach(combo_st_ini_hasta_f, 1, 2, 2, 3)
        
        combo_st_ini_hasta_h = gtk.Combo()
        tabla_estadistica.attach(combo_st_ini_hasta_h, 2, 3, 2, 3)
        
        lbl_comporativo = gtk.Label("comparativo:")
        lbl_comporativo.set_alignment(0, 1)
        tabla_estadistica.attach(lbl_comporativo, 0, 1, 3, 4)
        
        label_de_c = gtk.Label("De: ")
        label_de_c.set_alignment(1, 0)
        tabla_estadistica.attach(label_de_c, 0, 1, 4, 5)
        
        combo_st_fin_de_f = gtk.Combo()
        tabla_estadistica.attach(combo_st_fin_de_f, 1, 2, 4, 5)
        
        combo_st_fin_de_h = gtk.Combo()
        tabla_estadistica.attach(combo_st_fin_de_h, 2, 3, 4, 5)
        
        label_hasta_c = gtk.Label("Hasta: ")
        label_hasta_c.set_alignment(1, 0)
        tabla_estadistica.attach(label_hasta_c, 0, 1, 5, 6)
        
        combo_st_fin_hasta_f = gtk.Combo()
        tabla_estadistica.attach(combo_st_fin_hasta_f, 1, 2, 5, 6)
        
        combo_st_fin_hasta_h = gtk.Combo()
        tabla_estadistica.attach(combo_st_fin_hasta_h, 2, 3, 5, 6)
        
        check_graficar = gtk.CheckButton(label = "Generar gráfica")
        tabla_estadistica.attach(check_graficar, 3, 4, 0, 1)
        
        combo_resolucion_s = gtk.ComboBox()
        lista_resolucion_s = gtk.ListStore(str)
        lista_resolucion_s.append(["Minima (1 minuto)"])
        lista_resolucion_s.append(["5 minutos"])
        lista_resolucion_s.append(["30 minutos"])
        lista_resolucion_s.append(["1 hora"])
        lista_resolucion_s.append(["1 dia"])
        cell_s = gtk.CellRendererText()
        combo_resolucion_s.pack_start(cell_s)
        combo_resolucion_s.add_attribute(cell_s, "text", 0)
        combo_resolucion_s.set_wrap_width(1)
        combo_resolucion_s.set_model(lista_resolucion_s)
        combo_resolucion_s.set_active(0)        
        tabla_estadistica.attach(combo_resolucion_s, 3, 4, 1, 2)
        
        btn_calcular = gtk.Button("Calcular")
        tabla_estadistica.attach(btn_calcular, 3, 4, 5, 6)
        
#BOTONES
        vbox_botones = gtk.VBox()
        vbox_botones.set_border_width(5)
        botonera = gtk.HButtonBox()
        barra = gtk.ProgressBar()
        
        #Apariencia
        botonera.set_layout(gtk.BUTTONBOX_END)
        botonera.set_spacing(10)
        
        btn_graficar = gtk.Button("Graficar")
        btn_graficar.set_sensitive(False)
        botonera.add(btn_graficar)
        
        btn_salir = gtk.Button("Salir")
        btn_salir.connect("clicked", self.destruir)
        botonera.add(btn_salir)
        
        vbox_botones.pack_end(botonera)
        
        frame_botonera.add(vbox_botones)
        
#MOSTRAR LA VENTANA
        self.window.add(vbox)
        self.window.show_all()
        self.window.connect("destroy", self.destruir)
        
#CONECTAR FUNCIONES
        abrir_menu_archivo.connect("activate", self.abrir, txt_examinar)
        btn_cargar.connect("clicked", self.cargarDatos, frame_fechas, frame_resolucion, txt_examinar, btn_graficar,
                           combo_fecha_de, combo_fecha_hasta, combo_hora_de, combo_hora_hasta, radio_todas,
                           exportar_menu_archivo, frame_estadistica, combo_st_ini_de_f, combo_st_ini_de_h,combo_st_ini_hasta_f, 
                           combo_st_ini_hasta_h, combo_st_fin_de_f, combo_st_fin_de_h, combo_st_fin_hasta_f, 
                           combo_st_fin_hasta_h) 
        radio_todas.connect("toggled", self.ocultar, combo_fecha_de, combo_hora_de, combo_fecha_hasta, combo_hora_hasta)
        radio_selec.connect("toggled", self.ver, combo_fecha_de, combo_hora_de, combo_fecha_hasta, combo_hora_hasta)
        btn_graficar.connect("clicked", self.graficar, txt_examinar, combo_fecha_de, combo_fecha_hasta, combo_hora_de, 
                             combo_hora_hasta, barra, radio_todas, radio_selec, combo_resolucion)
        exportar_menu_archivo.connect("activate", self.exportar, txt_examinar, combo_fecha_de, combo_fecha_hasta, combo_hora_de, 
                             combo_hora_hasta)
        btn_calcular.connect("clicked", main_datos, combo_st_ini_de_f, combo_st_ini_de_h,combo_st_ini_hasta_f, 
                           combo_st_ini_hasta_h, combo_st_fin_de_f, combo_st_fin_de_h, combo_st_fin_hasta_f, 
                           combo_st_fin_hasta_h, txt_examinar, combo_resolucion_s, check_graficar)
        
        
#FUNCIONES VARIAS        
    def main(self):
        gtk.main()        
        
    def destruir(self, widget, data = "None"):
        '''
        Función para cerrar la aplicación
        '''
        gtk.main_quit()
        
    def changed(self, combobox):
        '''
        Función que verifica si la resolución es de 1 minuto
        '''
        index = combobox.get_active()
        if index == 0:
            dialogo = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_WARNING, gtk.BUTTONS_OK)
            dialogo.set_markup(u"<b>Resolución mínima</b>")
            dialogo.format_secondary_markup(u"Recuerda que no hay datos de 1 minuto hasta despues del 18 de Septiembre de 2008")
            dialogo.run()
            dialogo.destroy()
        return
        
        
    def abrir(self, widget, entry):
        '''
        Fución que muestra el dialogo para seleccionar un archivo de datos,
        establece la ruta del archivo.
        '''
        dialogo = gtk.FileChooserDialog("Archivo de datos", 
                                        None, 
                                        gtk.FILE_CHOOSER_ACTION_OPEN, 
                                        (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                         gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialogo.set_default_response(gtk.RESPONSE_OK)
        
        filtro = gtk.FileFilter()
        filtro.set_name("Archivos de texto")
        filtro.add_pattern("*.txt")
        dialogo.add_filter(filtro)
        
        respuesta = dialogo.run()
        
        if respuesta == gtk.RESPONSE_OK:
            entry.set_text(dialogo.get_filename())
            
        dialogo.destroy()
        
    
    def exportar(self, w, entry, combofechade, combofechahasta, combohorade, combohorahasta):
        ruta = entry.get_text()
        
        
        
        dialogo = gtk.FileChooserDialog("Guardar como...", 
                                        None, 
                                        gtk.FILE_CHOOSER_ACTION_SAVE, 
                                        (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                         gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialogo.set_default_response(gtk.RESPONSE_OK)
        
        filtro = gtk.FileFilter()
        filtro.set_name("Archivos de texto")
        filtro.add_pattern("*.txt")
        dialogo.add_filter(filtro)
        
        respuesta = dialogo.run()
        archivo = dialogo.get_filename()
        
        fecha1 = combofechade.entry.get_text()
        fecha2 = combofechahasta.entry.get_text()
        hora1 = combohorade.entry.get_text()
        hora2 = combohorahasta.entry.get_text()
        
        fechade = fecha1 + "\t" + hora1
        fechahasta = fecha2 + "\t" + hora2
        
        datos = leer(ruta)
        i = 0
        j = 0
        
        for elemento in datos:        
            if fechade in elemento:
                break
            i = i + 1
            
        for elemento in datos:
            if fechahasta in elemento:
                break
            j = j + 1
            
        lista = datos[i:(j + 1)]
        
        if respuesta == gtk.RESPONSE_OK:
            f = open(archivo, "w")
            f.write("Mexico City, Neutron Monitor\n")
            f.write("Data resolution: 1 minute\n")
            f.write("Data Customized\n")
            f.write("\n")
            f.write("\n")
            f.write("Date\t\tTIme\t\tData\n")
            datos = leer(ruta)
            for n in lista:
                f.write(n)
            f.close()
            d = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_INFO, gtk.BUTTONS_OK)
            d.set_markup("<b>Terminado</b>")
            d.format_secondary_markup(u"La exportación de datos terminó satisfactoriamente.")
            d.run()
            d.destroy()
            
        dialogo.destroy()
    
        
    def cargarDatos(self, widget, frame_fechas, frame_resolucion, entry, btn_graficar, 
                    combofechade, combofechahasta, combohorade, combohorahasta, radiotodas, menu, frame_estadistica,
                    combodef1, combodeh1, combohastaf1, combohastah1, combodef2, combodeh2, combohastaf2, combohastah2):
        ruta = entry.get_text()
        
        try:
            archivo = open(ruta, "r")
        except:
            dialogo = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK)
            dialogo.set_markup("<b>El archivo no existe</b>")
            dialogo.format_secondary_markup(u"El archivo que especificó no existe, los datos no se cargarán correctamente")
            dialogo.run()
            dialogo.destroy()
        else:
            #VALIDA ARCHIVO
            if self.validar(ruta) == 1:
                #ARMA LOS COMBOS DE LAS FECHA
                combofechade.set_popdown_strings(setFecha(ruta))
                combofechahasta.set_popdown_strings(setFecha(ruta))
                combohorade.set_popdown_strings(setHora(ruta))
                combohorahasta.set_popdown_strings(setHora(ruta))
                #ARMA LOS COMBOS DE LA ESTADISTICA
                combodef1.set_popdown_strings(setFecha(ruta))
                combohastaf1.set_popdown_strings(setFecha(ruta))
                combodef2.set_popdown_strings(setFecha(ruta))
                combohastaf2.set_popdown_strings(setFecha(ruta))
                combohastah1.set_popdown_strings(setHora(ruta))
                combodeh1.set_popdown_strings(setHora(ruta))
                combodeh2.set_popdown_strings(setHora(ruta))
                combohastah2.set_popdown_strings(setHora(ruta))
                
                radiotodas.set_active(1)
                            
                frame_fechas.set_sensitive(True)
                frame_resolucion.set_sensitive(True)
                btn_graficar.set_sensitive(True)
                menu.set_sensitive(True)
                frame_estadistica.set_sensitive(True)
                archivo.close()
            else:
                dialogo = gtk.MessageDialog(None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK)
                dialogo.set_markup("<b>Archivo no valido</b>")
                dialogo.format_secondary_markup(u"El archivo que especificó no es valido.")
                dialogo.run()
                dialogo.destroy()
                
                
    def validar(self, ruta):
        if ruta.find(".txt") != -1:
            archivo = open(ruta, "r")
            linea = []
            comparar = ['Mexico City, Neutron Monitor\n', 
                        'Data resolution: 1 minute\n', 
                        'from 1-10-2013 to 30-10-2013\n', 
                        '\n', 
                        '\n', 
                        'Date\t\tTIme\t\tData\n']
            contador = 0
            while contador < 6:
                linea.append(archivo.readline())
                contador += 1
            if linea[0] == comparar[0]:
                if linea[1] == comparar[1]:
                    if linea[3] == comparar[3]:
                        if linea[4] == comparar[4]:
                            if linea[5] == comparar[5]:
                                return 1
            else:
                return 0
        else:
            return 0
            
    
    def ocultar(self, w, combofechade, combohorade, combofechahasta, combohorahasta):
        combofechade.set_sensitive(False)
        combofechahasta.set_sensitive(False)
        combohorade.set_sensitive(False)
        combohorahasta.set_sensitive(False)
    
    def ver(self, w, combofechade, combohorade, combofechahasta, combohorahasta):
        combofechade.set_sensitive(True)
        combofechahasta.set_sensitive(True)
        combohorade.set_sensitive(True)
        combohorahasta.set_sensitive(True)
        
    def graficar(self, w, entry, combofechade, combofechahasta, combohorade, combohorahasta, barra, 
                 radiot, radios, res):
        
        ruta  =  entry.get_text()
        resolucion = res.get_active_text()
        
        fecha1 = combofechade.entry.get_text()
        fecha2 = combofechahasta.entry.get_text()
        hora1 = combohorade.entry.get_text()
        hora2 = combohorahasta.entry.get_text()
        
        g = Plot(ruta)
        
        if radiot.get_active():
            
            if resolucion == "Minima (1 minuto)":
                g.Call_GraficaTodas(1)
            elif resolucion == "5 minutos":                
                g.Call_GraficaTodas(5)
            elif resolucion == "30 minutos":
                g.Call_GraficaTodas(30)
            elif resolucion == "1 hora":
                g.Call_GraficaTodas(60)
            elif resolucion == "1 dia":
                g.Call_GraficaTodas(1440)
        else:
            fechade = fecha1 + "\t" + hora1
            fechahasta = fecha2 + "\t" + hora2
            
            if resolucion == "Minima (1 minuto)":
                g.Call_GraficaFechas(fechade, fechahasta, 1)
            elif resolucion == "5 minutos":
                g.Call_GraficaFechas(fechade, fechahasta, 5)
            elif resolucion == "30 minutos":
                g.Call_GraficaFechas(fechade, fechahasta, 30)
            elif resolucion == "1 hora":
                g.Call_GraficaFechas(fechade, fechahasta, 60)
            elif resolucion == "1 dia":
                g.Call_GraficaFechas(fechade, fechahasta, 1440)
            
            
if __name__ == "__main__":
    g = Pygms()
    print "Proceso principal lanzado ", "PID: ", os.getppid() 
    g.main()
    print "Proceso principal detenido ", "PID: ", os.getppid()
