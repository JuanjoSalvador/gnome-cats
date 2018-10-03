#!/usr/bin/env python3

import gi, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gio

def get_cat_ref():
    return Gio.File.new_for_uri('https://cataas.com/cat')

class App(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         application_id="com.jotadevs.GnomeCats",
                         **kwargs)
        self.cat_file = Gio.File.new_tmp()[0]
        self.cat_pixbuf = None

    def do_startup(self):
        Gtk.Application.do_startup(self)
        self.ui = Gtk.Builder.new_from_file(Gio.File.new_for_path(__file__)
                                                    .get_parent()
                                                    .get_path()
                                                    + "/application.ui")
        self.ui.get_object("aboutWindow").destroy()
        self.ui.connect_signals(self)

        self.add_window(self.ui.get_object("mainWindow"))
        self.get_window_by_id(1).present()

        self.load_spinner = self.ui.get_object("load_spinner")
        self.load_and_show_new_image(self.ui.get_object("image"))

    def do_activate(self):
        pass

    def load_and_show_new_image(self, image):
        self.ui.get_object("save_image").hide()
        image.hide()
        self.load_spinner.start()
        get_cat_ref().read_async(0, None, self.on_ready_new_image, image)

    def on_ready_new_image(self, cat, res, image):
        self.cat_file.replace(
                          None,
                          False,
                          Gio.FileCreateFlags.NONE,
                          None
                    ).splice(
                          cat.read_finish(res),
                          Gio.OutputStreamSpliceFlags.CLOSE_TARGET,
                          None)
        self.cat_pixbuf = GdkPixbuf.Pixbuf.new_from_stream(self.cat_file.read())
        self.load_spinner.stop()
        self.scale_image(image, image.get_allocation())
        image.show()
        self.ui.get_object("save_image").show()

    def scale_image(self, image, dest, *args):
        if self.cat_pixbuf:
            fact = min(dest.width / self.cat_pixbuf.get_width(),
                       dest.height / self.cat_pixbuf.get_height())

            image.set_from_pixbuf(GdkPixbuf
                                      .Pixbuf
                                      .scale_simple(
                                           self.cat_pixbuf,
                                           self.cat_pixbuf.get_width() * fact,
                                           self.cat_pixbuf.get_height() * fact,
                                           GdkPixbuf.InterpType.BILINEAR))

    def save_image(self, parent):
        if self.cat_file:
            save_dialog = Gtk.FileChooserNative.new(None,
                                                    parent,
                                                    Gtk.FileChooserAction.SAVE,
                                                    None,
                                                    None)
            jpg_filter = Gtk.FileFilter()
            jpg_filter.add_pattern("*.jpg")
            jpg_filter.add_mime_type("image/jpeg")
            jpg_filter.set_name("JPEG image")
            save_dialog.add_filter(jpg_filter)
            if save_dialog.run() == Gtk.ResponseType.ACCEPT:
                save_dialog.get_file(
                          ).replace(
                                None,
                                False,
                                Gio.FileCreateFlags.NONE,
                                None
                          ).splice(
                                self.cat_file.read(),
                                Gio.OutputStreamSpliceFlags.CLOSE_TARGET,
                                None)

    def show_about(self, *args):
        self.ui.add_objects_from_file(Gio.File.new_for_path(__file__)
                                              .get_parent()
                                              .get_path()
                                              + "/application.ui",
                                      ["aboutWindow"])
        self.ui.get_object("aboutWindow").present()

    def do_shutdown(self):
        self.cat_file.delete()
        Gtk.Application.do_shutdown(self)

App().run(sys.argv)
