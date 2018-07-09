import gi, threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
from lib.window import ApplicationWindow

"""
Main window for GNOME Cats
"""
app = ApplicationWindow()

# Running DBus server on another thread
# thread = threading.Thread(target=Session_DBus.run_dbus_server)
# thread.daemon = True
# thread.start()

# Main loop
Gtk.main()