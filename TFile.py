# from src.gui.main_dialog import Ui_MainWindow
# from src.gui.main_window import Ui_MainWindow
from src.gui.windows_dialog.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from src.service.wormhole_transfer import transfer_file
import twisted.internet
import qt5reactor
import sys

from src.service import picture_rc

# Fix for pyinstaller packages app to avoid ReactorAlreadyInstalledError
# See https://github.com/kivy/kivy/issues/4182 and
# https://github.com/pyinstaller/pyinstaller/issues/3390
if "twisted.internet.reactor" in sys.modules:
    del sys.modules["twisted.internet.reactor"]

app = QApplication([])
qt5reactor.install()


# class MainWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self, reactors_, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#         tf = transfer_file(reactors_)
#         self.setupUi(self, tf)
#         self.show()
#         self.setWindowIcon(QtGui.QIcon(os.path.join('src/picture', 'piecasso.ico')))

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, reactors_, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        tf = transfer_file(reactors_)
        self.setupUi(self, tf)
        self.show()
        self.setWindowIcon(QtGui.QIcon(u":/pic/picture/piecasso.ico"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.setApplicationName("文件传输")
    reactor = twisted.internet.reactor
    window = MainWindow(reactor)
    sys.exit(reactor.run())
