import gi
import threading, os
<<<<<<< HEAD
import simpleaudio as sa
=======
>>>>>>> f596961cc8bdebb7244bb2a89c03cd31450dc837

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

        app_builder.add_from_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), "application.ui"))

        app_builder.connect_signals(ApplicationWindow)

        window = app_builder.get_object("mainWindow")
        window.show_all()

        thread = threading.Thread(target=Api.get_cat())
        thread.daemon = True
        thread.start()

        image = ApplicationWindow.builder.get_object('cat_picture')
<<<<<<< HEAD
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('cat.jpg', width=450, height=600, preserve_aspect_ratio=True)
=======
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('cat.jpg', width=600, height=600, preserve_aspect_ratio=True)
>>>>>>> f596961cc8bdebb7244bb2a89c03cd31450dc837
        image.set_from_pixbuf(pixbuf)
        image.show()

    def on_button_meow(self, *args):
        image = ApplicationWindow.builder.get_object('cat_picture')

<<<<<<< HEAD
        thread_image = threading.Thread(target=Api.get_cat())
        thread_image.daemon = True
        thread_image.start()

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('cat.jpg', width=450, height=600, preserve_aspect_ratio=True)
=======
        thread = threading.Thread(target=Api.get_cat())
        thread.daemon = True
        thread.start()

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('cat.jpg', width=600, height=600, preserve_aspect_ratio=True)
>>>>>>> f596961cc8bdebb7244bb2a89c03cd31450dc837
        image.set_from_pixbuf(pixbuf)
        image.show()

    def on_button_close(self, *args):
        """
        Close the server and client.
        """

        Gtk.main_quit(*args)
<<<<<<< HEAD
=======

    
>>>>>>> f596961cc8bdebb7244bb2a89c03cd31450dc837
