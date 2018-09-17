import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Granite  # Imports GTK and Granite libs. Don't know if Granite will work as version is apparently not 5.0 on PyGObject


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Connect")

        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Connect"
        self.set_titlebar(header)
        self.set_default_size(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)




window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()