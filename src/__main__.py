#!/usr/bin/env python3

import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio

def get_cat_file():
    return Gio.File.new_for_uri('http://cataas.com/cat')

class App():
    cat_pixbuf = None

    def __init__(self):
        ui = Gtk.Builder.new_from_file(os.path.join(os.path.dirname(__file__),
                                                    "application.ui"))
        ui.connect_signals(self)

        window = ui.get_object("mainWindow")
        window.show_all()

        self.load_spinner = ui.get_object("load_spinner")
        self.load_new_image(ui.get_object("image"))

    def load_new_image(self, image):
        self.cat_stream = None
        image.hide()
        self.load_spinner.start()
        get_cat_file().read_async(0, None, self.on_ready_new_image, image)

    def on_ready_new_image(self, cat_stream, result, image):
        self.cat_pixbuf = GdkPixbuf.Pixbuf.new_from_stream(cat_stream.read_finish(result))
        self.load_spinner.stop()
        self.scale_and_show_image(image, image.get_allocation())

    def scale_and_show_image(self, image, dest, *args):
        if self.cat_pixbuf:
            factor = min(dest.width / self.cat_pixbuf.get_width(),
                         dest.height / self.cat_pixbuf.get_height())

            scaled = GdkPixbuf.Pixbuf.scale_simple(self.cat_pixbuf,
                                                   self.cat_pixbuf.get_width() * factor,
                                                   self.cat_pixbuf.get_height() * factor,
                                                   GdkPixbuf.InterpType.BILINEAR)
            image.set_from_pixbuf(scaled)
            image.show()

    def quit(*args):
        Gtk.main_quit() 

App()
Gtk.main()
