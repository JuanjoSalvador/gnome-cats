#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio

def get_cat_stream():
    return Gio.File.new_for_uri('http://cataas.com/cat')

class Handlers():
    def change_picture(self, picture):
        cat = GdkPixbuf.Pixbuf.new_from_stream_at_scale(get_cat_stream().read(),
                                                        width=450,
                                                        height=600,
                                                        preserve_aspect_ratio=True)
        picture.set_from_pixbuf(cat)
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
