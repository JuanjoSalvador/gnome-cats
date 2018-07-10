import gi, threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from lib.window import ApplicationWindow

"""
Main window for GNOME Cats
"""
app = ApplicationWindow()

# Main loop
Gtk.main()