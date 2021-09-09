from PyQt5 import QtCore


class w_retranslateUI:
    def __init__(self, mainDialog,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件传输"))
        self._main_dialog = mainDialog
        self._main_dialog.label_3.setText(_translate("MainWindow", "生成密钥"))
        self._main_dialog.label_9.setText(_translate("MainWindow", "已发送"))
        self._main_dialog.btnSendFile.setText(_translate("MainWindow", "发送"))
        self._main_dialog.btnBrowseFile.setText(_translate("MainWindow", "选择文件"))
        self._main_dialog.label_4.setText(_translate("MainWindow", "发送文件"))
        self._main_dialog.label_15.setText(_translate("MainWindow", "文件大小（M）:"))
        self._main_dialog.label_20.setText(_translate("MainWindow", ""))
        self._main_dialog.label_8.setText(_translate("MainWindow", "已选择发送路径"))
        self._main_dialog.tabWidget.setTabText(self._main_dialog.tabWidget.indexOf(self._main_dialog.tabTransmit), _translate("MainWindow", "发送"))
        self._main_dialog.label_12.setText(_translate("MainWindow", "已接收"))
        self._main_dialog.btnBrowseFolder.setText(_translate("MainWindow", "选择文件"))
        self._main_dialog.label_13.setText(_translate("MainWindow", "已选择接收路径"))
        self._main_dialog.label_17.setText(_translate("MainWindow", "文件名字:"))
        self._main_dialog.label_18.setText(_translate("MainWindow", "文件大小 (M):"))
        self._main_dialog.label_11.setText(_translate("MainWindow", "接收文件"))
        self._main_dialog.label_14.setText(_translate("MainWindow", ""))
        self._main_dialog.label_5.setText(_translate("MainWindow", ""))
        self._main_dialog.btnSetCodeRecv.setText(_translate("MainWindow", "确认\n"
                                                             "接收"))
        self._main_dialog.label_10.setText(_translate("MainWindow", "接收密钥"))
        self._main_dialog.tabWidget.setTabText(self._main_dialog.tabWidget.indexOf(self._main_dialog.tabReceive), _translate("MainWindow", "接收"))
        self._main_dialog.btnSaveSetup.setText(_translate("MainWindow", "Salva"))
        self._main_dialog.label.setText(_translate("MainWindow", "Rendez-Vous relay:"))
        self._main_dialog.label_7.setText(_translate("MainWindow", "Transit relay:"))
        self._main_dialog.label_2.setText(_translate("MainWindow", "App ID:"))
        self._main_dialog.label_6.setText(_translate("MainWindow", "Lingua:"))
        self._main_dialog.cmbLanguage.setItemText(0, _translate("MainWindow", "Default sistema"))
        self._main_dialog.tabWidget.setTabText(self._main_dialog.tabWidget.indexOf(self._main_dialog.tabSettings), _translate("MainWindow", "111"))
        self._main_dialog.tabWidget.setTabText(self._main_dialog.tabWidget.indexOf(self._main_dialog.tab), _translate("MainWindow", "日志"))
        self._main_dialog.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self._main_dialog.actionWormhole.setText(_translate("MainWindow", "Connetti wormhole"))
        self._main_dialog.actionOpenFile.setText(_translate("MainWindow", "Seleziona file..."))
        self._main_dialog.actionQuit.setText(_translate("MainWindow", "Esci"))
        self._main_dialog.actionViewGraph.setText(_translate("MainWindow", "Grafico stato..."))
        self._main_dialog.actionAbout.setText(_translate("MainWindow", "About..."))