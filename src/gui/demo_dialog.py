import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from os.path import expanduser

from PyQt5.QtWidgets import QMainWindow
from ..service.common import get_platform



class open_dialog():

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()

        # self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        default_dir = expanduser("~")
        if get_platform().endswith('dows'):
            default_dir = 'C:\\users\\%username%\\Desktop'

        fileName, _ = QFileDialog.getOpenFileName(self, "选择文件", default_dir,
                                                  "所有文件 (*);;Zip 文件 (*.zip);;Tar 文件 (*.tar)", options=options)
        if fileName:
            print(fileName)

    def confim_download_dir(self):
        dirs_ = QFileDialog.getExistingDirectory(self,
                                                 "Open a folder",
                                                 expanduser("~"),
                                                 QFileDialog.ShowDirsOnly
                                                 )
        if dirs_:
            print('this is goal')

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)



