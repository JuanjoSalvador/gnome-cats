import urllib.request, threading

class Api():

    def get_cat():
        urllib.request.urlretrieve('http://cataas.com/cat', 'cat.jpg')