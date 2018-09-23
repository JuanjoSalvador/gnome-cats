#!/usr/bin/env python3

import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio

def get_cat_file():
    return Gio.File.new_for_uri('https://cataas.com/cat')

class App(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         application_id="com.jotadevs.GnomeCats",
                         **kwargs)
        self.cat_pixbuf = None

    def do_startup(self):
        Gtk.Application.do_startup(self)
        self.ui = Gtk.Builder.new_from_file(Gio.File.new_for_path(__file__)
                                                    .get_parent()
                                                    .get_path()
                                                    + "/application.ui")
        self.ui.connect_signals(self)

        self.add_window(self.ui.get_object("mainWindow"))
        self.get_window_by_id(1).present()

        self.load_spinner = self.ui.get_object("load_spinner")
        self.load_and_show_new_image(self.ui.get_object("image"))

    def do_activate(self):
        pass

    def load_and_show_new_image(self, image):
        image.hide()
        self.load_spinner.start()
        get_cat_file().read_async(0, None, self.on_ready_new_image, image)

    def on_ready_new_image(self, cat, res, image):
        self.cat_pixbuf = GdkPixbuf.Pixbuf.new_from_stream(cat.read_finish(res))
        self.load_spinner.stop()
        self.scale_image(image, image.get_allocation())
        image.show()

    def scale_image(self, image, dest, *args):
        if self.cat_pixbuf:
            factor = min(dest.width / self.cat_pixbuf.get_width(),
                         dest.height / self.cat_pixbuf.get_height())

            scaled = GdkPixbuf.Pixbuf.scale_simple(
                                          self.cat_pixbuf,
                                          self.cat_pixbuf.get_width() * factor,
                                          self.cat_pixbuf.get_height() * factor,
                                          GdkPixbuf.InterpType.BILINEAR
                                      )
            image.set_from_pixbuf(scaled)

App().run(sys.argv)
