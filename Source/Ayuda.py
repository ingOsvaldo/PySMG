#!/usr/bin/env python
# -*- coding: utf-8 -*-
__license__   = 'GPL v3'
__copyright__ = '2014, Osvaldo Cesar Trujillo Torres <osvaldo.trujillo.ingenieria@gmail.com>'

import pygtk
pygtk.require('2.0')
import gtk
import pango
import webbrowser
import textwrap
import os

class Ayuda:
    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.delete)
        window.set_border_width(10)
        window.set_title ("Acerca de PySMG")
        window.set_resizable(0)

        table = gtk.VBox(False,0)
        window.add(table)

        # Create a new notebook, place the position of the tabs
        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_TOP)
        table.add(notebook)
        notebook.show()
        self.show_tabs = True
        self.show_border = True

        # FRAME DE INFORMACIÓN
        vbox = gtk.VBox(False,0)
        
        frame = gtk.Frame("Acerca de PySMG")
        frame.set_border_width(10)
        frame.set_size_request(510, 450)
                
        # SE AGREGA LA PAGINA AL CUADERNO
        label = gtk.Label("Acerca de PySMG")
        notebook.append_page(frame,label)
        
        pygms = gtk.Image()
	pygms_path = os.getcwd()+"/Images/graph.png"
        pygms.set_from_file(pygms_path)
        pygms.show()
        vbox.add(pygms)
        
        titulo = gtk.Label("PySMG 2.0")
        cambio = pango.FontDescription("Black 24")
        titulo.modify_font(cambio)
        vbox.add(titulo)
        
        descripcion = '''Programa para analizar y graficar datos de detectores de partículas solares'''
        des = gtk.Label(descripcion)
        vbox.add(des)
        
        copy = gtk.Label("\nCopyright © 2014 Osvaldo Cesar Trujillo Torres\n")
        cambio = pango.FontDescription("Black 12")
        copy.modify_font(cambio)
        vbox.add(copy)
        
        link = "http://www.geofisica.unam.mx/observatorios/rayos_cosmicos/grupo_raycos/index.html"
        url = gtk.Button("Visita el Grupo de Rayos cósmicos de la UNAM")
        url.connect("clicked", self.navegador)
        vbox.add(url)
        
        
        # FRAME DE CRÉDITOS
        vboxB = gtk.VBox(False,0)
        
        frameB = gtk.Frame("Créditos de PySMG")
        frameB.set_border_width(10)
        frameB.set_size_request(510, 400)
                
        # SE AGREGA LA PAGINA AL CUADERNO
        label = gtk.Label("Créditos de PySMG")
        notebook.append_page(frameB,label)
        
        h = gtk.HBox(False,0)
        vboxB.add(h)
        
        unam = gtk.Image()
	unam_path = os.getcwd()+"/Images/unam.gif"
        unam.set_from_file(unam_path)
        unam.show()
        h.add(unam)
        
        geofisica = gtk.Image()
	geofisica_path = os.getcwd()+"/Images/logo_geofisica1.png"
        geofisica.set_from_file(geofisica_path)
        geofisica.show()
        h.add(geofisica)
        
        asesor = gtk.Label("Asesor:")
        cambio = pango.FontDescription("Black 24")
        asesor.modify_font(cambio)
        vboxB.add(asesor)
        
        dr = gtk.Label("Dr. Luis Xavier González Méndez\n")
        cambio = pango.FontDescription("22")
        dr.modify_font(cambio)
        vboxB.add(dr)
        
        developer = gtk.Label("Diseño y Desarrollo:")
        cambio = pango.FontDescription("Black 24")
        developer.modify_font(cambio)
        vboxB.add(developer)
        
        ing = gtk.Label("Ing. Osvaldo Cesar Trujillo Torres\n")
        cambio = pango.FontDescription("22")
        ing.modify_font(cambio)
        vboxB.add(ing)
        
        # FRAME DE LICENCIA
        vboxC = gtk.VBox(False,0)
        
        frameC = gtk.Frame("Licencia de PySMG")
        frameC.set_border_width(10)
        frameC.set_size_request(510, 400)
                
        # SE AGREGA LA PAGINA AL CUADERNO
        label = gtk.Label("Licencia de PySMG")
        notebook.append_page(frameC,label)
        
        texto = '''PySMG es software libre: puede redistribuirlo y/o modificarlo bajo los
términos de la Licencia Pública General de GNU según se encuentra
publicada por la Free Software Foundation, de la versión 3 de dicha Licencia o bien (según su elección) de cualquier versión posterior.

Este programa se distribuye con la esperanza de que sea útil, pero SIN
NINGUNA GARANTÍA, incluso sin la garantía MERCANTIL implícita ni la de
garantizar la ADECUACIÓN A UN PROPÓSITO PARTICULAR. Véase la 
Licencia Pública General de GNU para más detalles.

Debería haber recibido una copia de la Licencia Pública General de GNU
junto con este programa. Si no ha sido así, consulte <http://
www.gnu.org/licenses/>.'''
        licencia = gtk.Label(texto)
        vboxC.add(licencia)
        
        
        frame.add(vbox)
        frameB.add(vboxB)
        frameC.add(vboxC)
        frame.show()
        table.show()
        window.show_all()

    def delete(self, widget, event=None):
        gtk.main_quit()
        return False
    
    def navegador(self, widget):
        webbrowser.open("http://www.geofisica.unam.mx/observatorios/rayos_cosmicos/grupo_raycos/index.html")

def main(w):
    Ayuda()
    gtk.main()
    return 0

'''if __name__ == "__main__":
    sys.exit(main())
'''
if __name__ == "__main__":
    Ayuda()
    gtk.main()
