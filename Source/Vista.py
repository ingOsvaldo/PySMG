'''
Created on 28/10/2013

@author: osvaldo
'''
__license__   = 'GPL v3'
__copyright__ = '2014, Osvaldo Cesar Trujillo Torres <osvaldo.trujillo.ingenieria@gmail.com>'

import gtk
#from Datos import media1

class prueba():
    datos = []


def Datos(dato1, dato2):
    prueba.datos = [dato1, dato2]
    return prueba.datos

class PyApp(gtk.Window): 
    def __init__(self):
        super(PyApp, self).__init__()
        
        self.set_size_request(550, 160)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        self.set_title("Resultados")
        

        vbox = gtk.VBox(False, 8)
        
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        vbox.pack_start(sw, True, True, 0)

        store = self.create_model()

        treeView = gtk.TreeView(store)
        treeView.connect("row-activated", self.on_activated)
        treeView.set_rules_hint(True)
        sw.add(treeView)

        self.create_columns(treeView)
        self.statusbar = gtk.Statusbar()
        
        vbox.pack_start(self.statusbar, False, False, 0)

        self.add(vbox)
        self.show_all()


    def create_model(self):
        store = gtk.ListStore(str, str, str, str, str)

        
        for d in prueba.datos:
            store.append([d[0], d[1], d[2], d[3], d[4]])

        return store


    def create_columns(self, treeView):
    
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn(" ", rendererText, text=0)
        column.set_sort_column_id(0)    
        treeView.append_column(column)
        
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Rangos", rendererText, text=1)
        column.set_sort_column_id(1)
        treeView.append_column(column)

        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Media", rendererText, text=2)
        column.set_sort_column_id(2)
        treeView.append_column(column)
        
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Min/Max", rendererText, text=3)
        column.set_sort_column_id(3)
        treeView.append_column(column)

        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Media (%)", rendererText, text=4)
        column.set_sort_column_id(4)
        treeView.append_column(column)
        
        

    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        self.statusbar.push(0, text)



#PyApp()
#gtk.main()