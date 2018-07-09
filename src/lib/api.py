import urllib.request
import gi
from gi.repository import GdkPixbuf

class Api():

    def get_cat():
        urllib.request.urlretrieve('http://cataas.com/cat', 'cat.jpg')