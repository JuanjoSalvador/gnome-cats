#!/usr/bin/env python3

import gi, urllib.request, threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject, GdkPixbuf

def get_cat():
    urllib.request.urlretrieve('http://cataas.com/cat', 'cat.jpg')

class Handlers():
    def change_picture(self, picture):
        threading.Thread(target=get_cat(), daemon=True).start()

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('cat.jpg',
                                                         width=450,
                                                         height=600,
                                                         preserve_aspect_ratio=True)
        picture.set_from_pixbuf(pixbuf)
        picture.show()

    def quit(*args):
        Gtk.main_quit() 


app = Gtk.Builder()
app.add_from_file("application.ui")
app.connect_signals(Handlers())

window = app.get_object("mainWindow")
window.show_all()

app.get_object("new_cat").clicked()

Gtk.main()
