#!/usr/bin/env python3

import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio

def get_cat_file():
    return Gio.File.new_for_uri('http://cataas.com/cat')

class App():
    def __init__(self):
        ui = Gtk.Builder()
        ui.add_from_file(os.path.join(os.path.dirname(__file__), "application.ui"))
        ui.connect_signals(self)

        window = ui.get_object("mainWindow")
        window.show_all()

        self.load_spinner = ui.get_object("load_spinner")
        self.load_new_image(ui.get_object("cat_image"))
                              

    def load_new_image(self, image):
        image.hide()
        self.load_spinner.start()
        get_cat_file().read_async(0, None, self.on_ready_new_image, image)

    def on_ready_new_image(self, cat_stream, result, image):
        self.cat_stream = cat_stream.read_finish(result)
        self.scale_and_show_image(image, image.get_allocation())
        self.load_spinner.stop()

    def scale_and_show_image(self, image, dest, *args):
        image.set_from_pixbuf(GdkPixbuf.Pixbuf.new_from_stream_at_scale(
                                    self.cat_stream,
                                    width=dest.width,
                                    height=dest.height,
                                    preserve_aspect_ratio=True))
        image.show()

    def quit(*args):
        Gtk.main_quit() 

App()
Gtk.main()
