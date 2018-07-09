import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, GObject, GdkPixbuf

from lib.api import Api

class ApplicationWindow(Gtk.Window):
    """
    ApplicationWindow is the main window instance
    """

    builder = Gtk.Builder()

    def __init__(self):
        app_builder = ApplicationWindow.builder

        app_builder.add_from_file("application.ui")

        app_builder.connect_signals(ApplicationWindow)

        window = app_builder.get_object("mainWindow")
        window.show_all()

        Api.get_cat()
        image = ApplicationWindow.builder.get_object('cat_picture')
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('cat.jpg', width=600, height=600, preserve_aspect_ratio=True)
        image.set_from_pixbuf(pixbuf)
        image.show()

    def on_button_meow(self, *args):
        Api.get_cat()
        image = ApplicationWindow.builder.get_object('cat_picture')
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('cat.jpg', width=600, height=600, preserve_aspect_ratio=True)
        image.set_from_pixbuf(pixbuf)
        image.show()

    def on_button_close(self, *args):
        """
        Close the server and client.
        """

        Gtk.main_quit(*args)