from PyQt5 import QtCore
# from .main_window import Ui_MainWindow

class retranslate_UI():
    def __init__(self, main_windown, MainWindow):
        self._wormholeTransfer = main_windown._wormholeTransfer
        self._main_windown = main_windown
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件传送"))
        # self._main_windown.btnCopyCode.setText(_translate("MainWindow", "复制"))
        # self._main_windown.btnSetCode.setText(_translate("MainWindow", "生成\n"
        #                                                  "密钥"))
        self._main_windown.label_3.setText(_translate("MainWindow", "密钥"))
        self._main_windown.btnBrowseFile.setText(_translate("MainWindow", "选择文件"))
        self._main_windown.label_8.setText(_translate("MainWindow", "已选择文件路经"))
        self._main_windown.label_9.setText(_translate("MainWindow", "已传送"))
        self._main_windown.btnSendFile.setText(_translate("MainWindow", "发送"))
        self._main_windown.label_4.setText(_translate("MainWindow", "发送文件"))
        self._main_windown.tabWidget.setTabText(self._main_windown.tabWidget.indexOf(self._main_windown.tabTransmit), _translate("MainWindow", "发送"))
        self._main_windown.btnBrowseFolder.setText(_translate("MainWindow", "选择文件"))
        self._main_windown.label_16.setText(_translate("MainWindow", "接收文件:"))
        self._main_windown.label_17.setText(_translate("MainWindow", "名称:"))
        self._main_windown.label_18.setText(_translate("MainWindow", "文件大小 (bytes):"))
        self._main_windown.label_11.setText(_translate("MainWindow", "接收文件"))
        self._main_windown.label_12.setText(_translate("MainWindow", "已接收"))
        self._main_windown.label_13.setText(_translate("MainWindow", "默认文件保存路径:"))
        self._main_windown.label_10.setText(_translate("MainWindow", "输入密钥"))
        # self._main_windown.btnPasteCode.setText(_translate("MainWindow", "Incolla"))
        self._main_windown.btnSetCodeRecv.setText(_translate("MainWindow", "确认\n"
                                                             "接收"))
        self._main_windown.tabWidget.setTabText(self._main_windown.tabWidget.indexOf(self._main_windown.tabReceive), _translate("MainWindow", "接收"))
        self._main_windown.btnSaveSetup.setText(_translate("MainWindow", "文件保存路径"))
        self._main_windown.label.setText(_translate("MainWindow", "Rendez-Vous relay:"))
        self._main_windown.label_7.setText(_translate("MainWindow", "Transit relay:"))
        self._main_windown.label_2.setText(_translate("MainWindow", "App ID:"))
        self._main_windown.label_6.setText(_translate("MainWindow", "Lingua:"))
        self._main_windown.cmbLanguage.setItemText(0, _translate("MainWindow", "Default sistema"))
        self._main_windown.tabWidget.setTabText(self._main_windown.tabWidget.indexOf(self._main_windown.tabSettings), _translate("MainWindow", "Setup"))
        self._main_windown.tabWidget.setTabText(self._main_windown.tabWidget.indexOf(self._main_windown.tab), _translate("MainWindow", "Logging"))
        self._main_windown.menuFile.setTitle(_translate("MainWindow", "File"))
        self._main_windown.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self._main_windown.actionWormhole.setText(_translate("MainWindow", "Connetti wormhole"))
        self._main_windown.actionOpenFile.setText(_translate("MainWindow", "Seleziona file..."))
        self._main_windown.actionQuit.setText(_translate("MainWindow", "Esci"))
        self._main_windown.actionViewGraph.setText(_translate("MainWindow", "Grafico stato..."))
        self._main_windown.actionAbout.setText(_translate("MainWindow", "About..."))







