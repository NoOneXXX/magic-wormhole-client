import os

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QMessageBox

from .TabCompleteQLineEdit import TabCompleteQLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from .retranslateUI_main_window import retranslate_UI
from ..service.common import get_defaul_path, resource_path
from ..service import picture_rc


class MainWindow_Setup:
    def __init__(self, ui, MainWindow):
        self._ui = ui
        # get code here
        # self._ui._wormholeTransfer.open_defer_mode(None)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(787, 842)
        palette_window = QPalette()
        palette_window.setColor(QPalette.Window, QtGui.QColor(160, 160, 164))
        MainWindow.autoFillBackground()
        MainWindow.setPalette(palette_window)
        self._ui.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.centralwidget.sizePolicy().hasHeightForWidth())
        self._ui.centralwidget.setSizePolicy(sizePolicy)
        self._ui.centralwidget.setObjectName("centralwidget")
        self._ui.gridLayout_2 = QtWidgets.QGridLayout(self._ui.centralwidget)
        self._ui.gridLayout_2.setObjectName("gridLayout_2")

        self._ui.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self._ui.verticalLayout_3.setObjectName("verticalLayout_3")
        self._ui.tabWidget = QtWidgets.QTabWidget(self._ui.centralwidget)
        self._ui.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self._ui.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self._ui.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self._ui.tabWidget.setObjectName("tabWidget")
        self._ui.tabWidget.setAutoFillBackground(True)
        self._ui.tabWidget.setPalette(palette_window)

        self._ui.tabTransmit = QtWidgets.QWidget()
        self._ui.tabTransmit.setObjectName("tabTransmit")
        self._ui.tabTransmit.setAutoFillBackground(True)
        # self._ui.tabTransmit.setPalette(palette_window)
        self._ui.gridLayout_8 = QtWidgets.QGridLayout(self._ui.tabTransmit)
        self._ui.gridLayout_8.setObjectName("gridLayout_8")

        self._ui.verticalWidget = QtWidgets.QWidget(self._ui.tabTransmit)
        self._ui.verticalWidget.setObjectName("verticalWidget")
        self._ui.verticalLayout = QtWidgets.QVBoxLayout(self._ui.verticalWidget)
        self._ui.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self._ui.verticalLayout.setObjectName("verticalLayout")
        self._ui.frame = QtWidgets.QFrame(self._ui.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self._ui.frame.sizePolicy().hasHeightForWidth())
        self._ui.frame.setSizePolicy(sizePolicy)
        self._ui.frame.setFrameShape(QtWidgets.QFrame.Box)
        self._ui.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self._ui.frame.setObjectName("frame")
        # self._ui.frame.setStyleSheet("background-color: #A0A0A4")

        self._ui.gridLayout_13 = QtWidgets.QGridLayout(self._ui.frame)
        self._ui.gridLayout_13.setObjectName("gridLayout_13")
        self._ui.txtSecretCode = QtWidgets.QLineEdit(self._ui.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self._ui.txtSecretCode.sizePolicy().hasHeightForWidth())
        self._ui.txtSecretCode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self._ui.txtSecretCode.setFont(font)
        self._ui.txtSecretCode.setText("[????????????????????????]")
        self._ui.txtSecretCode.setReadOnly(False)
        self._ui.txtSecretCode.setClearButtonEnabled(True)
        self._ui.txtSecretCode.setObjectName("txtSecretCode")
        self._ui.gridLayout_13.addWidget(self._ui.txtSecretCode, 1, 1, 1, 1)
        # self._ui.btnCopyCode = QtWidgets.QPushButton(self._ui.frame)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self._ui.btnCopyCode.sizePolicy().hasHeightForWidth())
        # self._ui.btnCopyCode.setSizePolicy(sizePolicy)
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/edit-copy-6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self._ui.btnCopyCode.setIcon(icon)
        # self._ui.btnCopyCode.setObjectName("btnCopyCode")
        # self._ui.gridLayout_13.addWidget(self._ui.btnCopyCode, 1, 4, 1, 1)
        # self._ui.btnSetCode = QtWidgets.QPushButton(self._ui.frame)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self._ui.btnSetCode.sizePolicy().hasHeightForWidth())
        # self._ui.btnSetCode.setSizePolicy(sizePolicy)
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/lock-silver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self._ui.btnSetCode.setIcon(icon1)
        # self._ui.btnSetCode.setIconSize(QtCore.QSize(32, 32))
        # self._ui.btnSetCode.setObjectName("btnSetCode")
        # self._ui.gridLayout_13.addWidget(self._ui.btnSetCode, 1, 3, 1, 1)
        self._ui.label_3 = QtWidgets.QLabel(self._ui.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self._ui.label_3.sizePolicy().hasHeightForWidth())
        self._ui.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._ui.label_3.setFont(font)
        self._ui.label_3.setStyleSheet("")
        self._ui.label_3.setObjectName("label_3")
        self._ui.gridLayout_13.addWidget(self._ui.label_3, 0, 0, 1, 3)
        self._ui.verticalLayout.addWidget(self._ui.frame)
        self._ui.widget_2 = QtWidgets.QWidget(self._ui.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self._ui.widget_2.sizePolicy().hasHeightForWidth())
        self._ui.widget_2.setSizePolicy(sizePolicy)
        self._ui.widget_2.setObjectName("widget_2")
        self._ui.gridLayout_9 = QtWidgets.QGridLayout(self._ui.widget_2)
        self._ui.gridLayout_9.setContentsMargins(0, -1, 0, 0)
        self._ui.gridLayout_9.setObjectName("gridLayout_9")

        self._ui.horizontalLayout = QtWidgets.QHBoxLayout()
        self._ui.horizontalLayout.setObjectName("horizontalLayout")
        self._ui.frame_3 = QtWidgets.QFrame(self._ui.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.frame_3.sizePolicy().hasHeightForWidth())
        self._ui.frame_3.setSizePolicy(sizePolicy)
        self._ui.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self._ui.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        # self._ui.frame_3.setStyleSheet("background-color: #A0A0A4")
        self._ui.frame_3.setObjectName("frame_3")
        self._ui.gridLayout_12 = QtWidgets.QGridLayout(self._ui.frame_3)
        self._ui.gridLayout_12.setContentsMargins(6, -1, -1, -1)
        self._ui.gridLayout_12.setObjectName("gridLayout_12")
        self._ui.btnBrowseFile = QtWidgets.QPushButton(self._ui.frame_3)
        self._ui.btnBrowseFile.setObjectName("btnBrowseFile")
        self._ui.gridLayout_12.addWidget(self._ui.btnBrowseFile, 7, 0, 1, 1)
        self._ui.txtFileName = QtWidgets.QLineEdit(self._ui.frame_3)
        self._ui.txtFileName.setObjectName("txtFileName")
        self._ui.gridLayout_12.addWidget(self._ui.txtFileName, 5, 0, 2, 4)
        self._ui.label_8 = QtWidgets.QLabel(self._ui.frame_3)
        self._ui.label_8.setObjectName("label_8")
        self._ui.gridLayout_12.addWidget(self._ui.label_8, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._ui.gridLayout_12.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._ui.gridLayout_12.addItem(spacerItem1, 12, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._ui.gridLayout_12.addItem(spacerItem2, 9, 0, 1, 1)
        self._ui.widget_6 = QtWidgets.QWidget(self._ui.frame_3)
        self._ui.widget_6.setObjectName("widget_6")
        self._ui.horizontalLayout_5 = QtWidgets.QHBoxLayout(self._ui.widget_6)
        self._ui.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self._ui.gridLayout_12.addWidget(self._ui.widget_6, 13, 0, 1, 4)
        self._ui.progressSendFile = QtWidgets.QProgressBar(self._ui.frame_3)
        self._ui.progressSendFile.setProperty("value", 0)
        self._ui.progressSendFile.setObjectName("progressSendFile")
        self._ui.gridLayout_12.addWidget(self._ui.progressSendFile, 11, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._ui.gridLayout_12.addItem(spacerItem3, 7, 1, 1, 3)
        self._ui.label_9 = QtWidgets.QLabel(self._ui.frame_3)
        self._ui.label_9.setObjectName("label_9")
        self._ui.gridLayout_12.addWidget(self._ui.label_9, 10, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._ui.gridLayout_12.addItem(spacerItem4, 14, 0, 1, 1)
        self._ui.btnSendFile = QtWidgets.QPushButton(self._ui.frame_3)
        # self._ui.btnSendFile.setStyleSheet("background-image:url(src/picture/icon_send.png);"
        #                                "border:1px solid blue")
        self._ui.btnSendFile.setStyleSheet("background-color: #0AAFDF")
        self._ui.btnSendFile.setObjectName("btnSendFile")
        self._ui.gridLayout_12.addWidget(self._ui.btnSendFile, 12, 0, 1, 1)
        self._ui.label_4 = QtWidgets.QLabel(self._ui.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._ui.label_4.setFont(font)
        self._ui.label_4.setObjectName("label_4")
        self._ui.gridLayout_12.addWidget(self._ui.label_4, 1, 0, 1, 1)
        self._ui.horizontalLayout.addWidget(self._ui.frame_3)
        self._ui.gridLayout_9.addLayout(self._ui.horizontalLayout, 0, 0, 1, 1)
        self._ui.verticalLayout.addWidget(self._ui.widget_2)
        self._ui.gridLayout_8.addWidget(self._ui.verticalWidget, 0, 0, 1, 1)
        icon3 = QtGui.QIcon()
        icon3.addFile(u":/pic/picture/icon_send.png", QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._ui.tabWidget.addTab(self._ui.tabTransmit, icon3, "")

        self._ui.tabReceive = QtWidgets.QWidget()
        self._ui.tabWidget.setPalette(palette_window)
        self._ui.tabReceive.setObjectName("tabReceive")
        # self._ui.tabWidget.setAutoFillBackground(True)
        # self._ui.tabWidget.setPalette(palette_window)
        self._ui.gridLayout_15 = QtWidgets.QGridLayout(self._ui.tabReceive)
        self._ui.gridLayout_15.setObjectName("gridLayout_15")
        self._ui.widget_4 = QtWidgets.QWidget(self._ui.tabReceive)
        self._ui.widget_4.setObjectName("widget_4")
        self._ui.verticalLayout_2 = QtWidgets.QVBoxLayout(self._ui.widget_4)
        self._ui.verticalLayout_2.setObjectName("verticalLayout_2")
        self._ui.widget_5 = QtWidgets.QWidget(self._ui.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self._ui.widget_5.sizePolicy().hasHeightForWidth())
        self._ui.widget_5.setSizePolicy(sizePolicy)
        self._ui.widget_5.setObjectName("widget_5")
        self._ui.horizontalLayout_3 = QtWidgets.QHBoxLayout(self._ui.widget_5)
        self._ui.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self._ui.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._ui.frame_5 = QtWidgets.QFrame(self._ui.widget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.frame_5.sizePolicy().hasHeightForWidth())
        self._ui.frame_5.setSizePolicy(sizePolicy)
        # self._ui.frame_5.setStyleSheet("background-color: #A0A0A4")
        self._ui.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self._ui.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self._ui.frame_5.setObjectName("frame_5")
        self._ui.gridLayout_16 = QtWidgets.QGridLayout(self._ui.frame_5)
        self._ui.gridLayout_16.setContentsMargins(-1, -1, 6, -1)
        self._ui.gridLayout_16.setObjectName("gridLayout_16")
        self._ui.txtFolderName = QtWidgets.QLineEdit(self._ui.frame_5)
        self._ui.txtFolderName.setObjectName("txtFolderName")
        self._ui.gridLayout_16.addWidget(self._ui.txtFolderName, 4, 0, 2, 4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._ui.gridLayout_16.addItem(spacerItem5, 1, 0, 1, 4)
        self._ui.label_15 = QtWidgets.QLabel(self._ui.frame_5)
        self._ui.label_15.setEnabled(True)
        self._ui.label_15.setObjectName("label_15")
        self._ui.gridLayout_16.addWidget(self._ui.label_15, 11, 2, 1, 1)
        self._ui.btnBrowseFolder = QtWidgets.QPushButton(self._ui.frame_5)
        self._ui.btnBrowseFolder.setMinimumSize(QtCore.QSize(0, 0))
        self._ui.btnBrowseFolder.setMaximumSize(QtCore.QSize(100, 16777215))
        self._ui.btnBrowseFolder.setObjectName("btnBrowseFolder")
        self._ui.gridLayout_16.addWidget(self._ui.btnBrowseFolder, 6, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._ui.gridLayout_16.addItem(spacerItem6, 7, 0, 1, 4)
        self._ui.progressRecvFile = QtWidgets.QProgressBar(self._ui.frame_5)
        self._ui.progressRecvFile.setProperty("value", 0)
        self._ui.progressRecvFile.setObjectName("progressRecvFile")
        self._ui.gridLayout_16.addWidget(self._ui.progressRecvFile, 14, 0, 1, 4)
        self._ui.label_16 = QtWidgets.QLabel(self._ui.frame_5)
        self._ui.label_16.setObjectName("label_16")
        self._ui.gridLayout_16.addWidget(self._ui.label_16, 8, 0, 1, 4)
        self._ui.label_5 = QtWidgets.QLabel(self._ui.frame_5)
        self._ui.label_5.setObjectName("label_5")
        self._ui.gridLayout_16.addWidget(self._ui.label_5, 9, 1, 1, 2)
        self._ui.label_17 = QtWidgets.QLabel(self._ui.frame_5)
        self._ui.label_17.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self._ui.label_17.setObjectName("label_17")
        self._ui.gridLayout_16.addWidget(self._ui.label_17, 9, 0, 1, 1)
        self._ui.label_18 = QtWidgets.QLabel(self._ui.frame_5)
        self._ui.label_18.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self._ui.label_18.setObjectName("label_18")
        self._ui.gridLayout_16.addWidget(self._ui.label_18, 11, 0, 1, 1)
        self._ui.label_11 = QtWidgets.QLabel(self._ui.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._ui.label_11.setFont(font)
        self._ui.label_11.setObjectName("label_11")
        self._ui.gridLayout_16.addWidget(self._ui.label_11, 0, 0, 1, 4)
        self._ui.label_12 = QtWidgets.QLabel(self._ui.frame_5)
        self._ui.label_12.setObjectName("label_12")
        self._ui.gridLayout_16.addWidget(self._ui.label_12, 13, 0, 1, 4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._ui.gridLayout_16.addItem(spacerItem7, 12, 0, 1, 4)
        self._ui.label_13 = QtWidgets.QLabel(self._ui.frame_5)
        self._ui.label_13.setObjectName("label_13")
        self._ui.gridLayout_16.addWidget(self._ui.label_13, 2, 0, 1, 4)
        self._ui.lblRecvFileName = QtWidgets.QLabel(self._ui.frame_5)
        self._ui.lblRecvFileName.setText("")
        self._ui.lblRecvFileName.setObjectName("lblRecvFileName")
        self._ui.gridLayout_16.addWidget(self._ui.lblRecvFileName, 9, 2, 1, 1)
        self._ui.widget_3 = QtWidgets.QWidget(self._ui.frame_5)
        self._ui.widget_3.setObjectName("widget_3")
        self._ui.horizontalLayout_4 = QtWidgets.QHBoxLayout(self._ui.widget_3)
        self._ui.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self._ui.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._ui.lblRecvTotal = QtWidgets.QLabel(self._ui.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.lblRecvTotal.sizePolicy().hasHeightForWidth())
        self._ui.lblRecvTotal.setSizePolicy(sizePolicy)
        self._ui.lblRecvTotal.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self._ui.lblRecvTotal.setText("")
        self._ui.lblRecvTotal.setObjectName("lblRecvTotal")
        self._ui.horizontalLayout_4.addWidget(self._ui.lblRecvTotal)
        self._ui.lblRecvRate = QtWidgets.QLabel(self._ui.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.lblRecvRate.sizePolicy().hasHeightForWidth())
        self._ui.lblRecvRate.setSizePolicy(sizePolicy)
        self._ui.lblRecvRate.setText("")
        self._ui.lblRecvRate.setAlignment(QtCore.Qt.AlignCenter)
        self._ui.lblRecvRate.setObjectName("lblRecvRate")
        self._ui.horizontalLayout_4.addWidget(self._ui.lblRecvRate)
        self._ui.lblRecvETA = QtWidgets.QLabel(self._ui.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.lblRecvETA.sizePolicy().hasHeightForWidth())
        self._ui.lblRecvETA.setSizePolicy(sizePolicy)
        self._ui.lblRecvETA.setText("")
        self._ui.lblRecvETA.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self._ui.lblRecvETA.setObjectName("lblRecvETA")
        self._ui.horizontalLayout_4.addWidget(self._ui.lblRecvETA)
        self._ui.gridLayout_16.addWidget(self._ui.widget_3, 15, 0, 1, 4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self._ui.gridLayout_16.addItem(spacerItem8, 11, 2, 1, 1)
        self._ui.horizontalLayout_3.addWidget(self._ui.frame_5)
        self._ui.verticalLayout_2.addWidget(self._ui.widget_5)
        self._ui.gridLayout_15.addWidget(self._ui.widget_4, 1, 0, 1, 1)
        self._ui.frame_4 = QtWidgets.QFrame(self._ui.tabReceive)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self._ui.frame_4.sizePolicy().hasHeightForWidth())
        self._ui.frame_4.setSizePolicy(sizePolicy)
        self._ui.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self._ui.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        # self._ui.frame_4.setStyleSheet("background-color: #A0A0A4")
        self._ui.frame_4.setObjectName("frame_4")
        self._ui.gridLayout_14 = QtWidgets.QGridLayout(self._ui.frame_4)
        self._ui.gridLayout_14.setContentsMargins(6, -1, -1, -1)
        self._ui.gridLayout_14.setObjectName("gridLayout_14")
        self._ui.txtSecretCodeRecv = TabCompleteQLineEdit(self._ui.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self._ui.txtSecretCodeRecv.sizePolicy().hasHeightForWidth())
        self._ui.txtSecretCodeRecv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self._ui.txtSecretCodeRecv.setFont(font)
        self._ui.txtSecretCodeRecv.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._ui.txtSecretCodeRecv.setText("")
        self._ui.txtSecretCodeRecv.setReadOnly(False)
        self._ui.txtSecretCodeRecv.setClearButtonEnabled(True)
        self._ui.txtSecretCodeRecv.setObjectName("txtSecretCodeRecv")
        self._ui.gridLayout_14.addWidget(self._ui.txtSecretCodeRecv, 1, 0, 1, 1)
        self._ui.label_10 = QtWidgets.QLabel(self._ui.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self._ui.label_10.sizePolicy().hasHeightForWidth())
        self._ui.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self._ui.label_10.setFont(font)
        self._ui.label_10.setStyleSheet("")
        self._ui.label_10.setObjectName("label_10")
        self._ui.gridLayout_14.addWidget(self._ui.label_10, 0, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/edit-paste-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._ui.btnSetCodeRecv = QtWidgets.QPushButton(self._ui.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.btnSetCodeRecv.sizePolicy().hasHeightForWidth())
        self._ui.btnSetCodeRecv.setSizePolicy(sizePolicy)
        # rec_tab = os.path.join('src/picture', 'img_button_rec.png')
        rec_tab = resource_path('src/picture/img_button_rec.png')
        icon4 = QtGui.QIcon()
        icon4.addFile(u":/pic/picture/img_button_rec.png", QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._ui.btnSetCodeRecv.setIcon(icon4)
        self._ui.btnSetCodeRecv.setIconSize(QtCore.QSize(32, 32))
        self._ui.btnSetCodeRecv.setObjectName("btnSetCodeRecv")
        self._ui.gridLayout_14.addWidget(self._ui.btnSetCodeRecv, 1, 3, 1, 1)
        self._ui.gridLayout_15.addWidget(self._ui.frame_4, 0, 0, 1, 1)
        # rec_tab = os.path.join('src/picture', 'img_tab_rec.png')
        rec_tab = resource_path('src/picture/img_tab_rec.png')
        icon5 = QtGui.QIcon()
        icon5.addFile(u":/pic/picture/img_tab_rec.png", QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._ui.tabWidget.addTab(self._ui.tabReceive, icon5, "")
        self._ui.tabWidget.setPalette(palette_window)
        self._ui.tabSettings = QtWidgets.QWidget()
        self._ui.tabSettings.setObjectName("tabSettings")
        self._ui.gridLayout_3 = QtWidgets.QGridLayout(self._ui.tabSettings)
        self._ui.gridLayout_3.setObjectName("gridLayout_3")
        self._ui.gridLayout_7 = QtWidgets.QGridLayout()
        self._ui.gridLayout_7.setObjectName("gridLayout_7")
        self._ui.widget_1 = QtWidgets.QWidget(self._ui.tabSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.widget_1.sizePolicy().hasHeightForWidth())
        self._ui.widget_1.setSizePolicy(sizePolicy)
        self._ui.widget_1.setObjectName("widget_1")
        self._ui.gridLayout = QtWidgets.QGridLayout(self._ui.widget_1)
        self._ui.gridLayout.setObjectName("gridLayout")
        self._ui.btnSaveSetup = QtWidgets.QPushButton(self._ui.widget_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.btnSaveSetup.sizePolicy().hasHeightForWidth())
        self._ui.btnSaveSetup.setSizePolicy(sizePolicy)
        self._ui.btnSaveSetup.setMinimumSize(QtCore.QSize(250, 0))
        self._ui.btnSaveSetup.setObjectName("btnSaveSetup")
        self._ui.gridLayout.addWidget(self._ui.btnSaveSetup, 0, 0, 1, 1)
        self._ui.gridLayout_7.addWidget(self._ui.widget_1, 1, 0, 1, 1)
        self._ui.widget_7 = QtWidgets.QWidget(self._ui.tabSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.widget_7.sizePolicy().hasHeightForWidth())
        self._ui.widget_7.setSizePolicy(sizePolicy)
        self._ui.widget_7.setObjectName("widget_7")
        self._ui.formLayout = QtWidgets.QFormLayout(self._ui.widget_7)
        self._ui.formLayout.setContentsMargins(100, -1, 100, -1)
        self._ui.formLayout.setHorizontalSpacing(20)
        self._ui.formLayout.setObjectName("formLayout")
        self._ui.label = QtWidgets.QLabel(self._ui.widget_7)
        self._ui.label.setObjectName("label")
        self._ui.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self._ui.label)
        self._ui.txtRelay = QtWidgets.QLineEdit(self._ui.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.txtRelay.sizePolicy().hasHeightForWidth())
        self._ui.txtRelay.setSizePolicy(sizePolicy)
        self._ui.txtRelay.setText("")
        self._ui.txtRelay.setObjectName("txtRelay")
        self._ui.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self._ui.txtRelay)
        self._ui.label_7 = QtWidgets.QLabel(self._ui.widget_7)
        self._ui.label_7.setObjectName("label_7")
        self._ui.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self._ui.label_7)
        self._ui.txtTransit = QtWidgets.QLineEdit(self._ui.widget_7)
        self._ui.txtTransit.setObjectName("txtTransit")
        self._ui.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self._ui.txtTransit)
        self._ui.label_2 = QtWidgets.QLabel(self._ui.widget_7)
        self._ui.label_2.setObjectName("label_2")
        self._ui.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self._ui.label_2)
        self._ui.txtAppID = QtWidgets.QLineEdit(self._ui.widget_7)
        self._ui.txtAppID.setObjectName("txtAppID")
        self._ui.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self._ui.txtAppID)
        self._ui.label_6 = QtWidgets.QLabel(self._ui.widget_7)
        self._ui.label_6.setObjectName("label_6")
        self._ui.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self._ui.label_6)
        self._ui.cmbLanguage = QtWidgets.QComboBox(self._ui.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._ui.cmbLanguage.sizePolicy().hasHeightForWidth())
        self._ui.cmbLanguage.setSizePolicy(sizePolicy)
        self._ui.cmbLanguage.setMinimumSize(QtCore.QSize(150, 0))
        self._ui.cmbLanguage.setObjectName("cmbLanguage")
        self._ui.cmbLanguage.addItem("")
        self._ui.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self._ui.cmbLanguage)
        self._ui.gridLayout_7.addWidget(self._ui.widget_7, 0, 0, 1, 1)
        self._ui.gridLayout_3.addLayout(self._ui.gridLayout_7, 0, 0, 1, 1)
        # icon6 = QtGui.QIcon()
        # icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icons/preferences-system-4.png"), QtGui.QIcon.Normal,
        #                 QtGui.QIcon.Off)
        # self._ui.tabWidget.addTab(self._ui.tabSettings, icon6, "")
        self._ui.tab = QtWidgets.QWidget()
        self._ui.tab.setObjectName("tab")
        self._ui.gridLayout_11 = QtWidgets.QGridLayout(self._ui.tab)
        self._ui.gridLayout_11.setObjectName("gridLayout_11")
        self._ui.txtLog = QtWidgets.QPlainTextEdit(self._ui.tab)
        self._ui.txtLog.setReadOnly(True)
        self._ui.txtLog.setObjectName("txtLog")
        self._ui.gridLayout_11.addWidget(self._ui.txtLog, 0, 0, 1, 1)
        # log_tab = os.path.join('src/picture', 'icon_logging.png')
        log_tab = resource_path('src/picture/img_logging.png')
        icon7 = QtGui.QIcon()
        icon7.addFile(u":/pic/picture/icon_logging", QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self._ui.tabWidget.addTab(self._ui.tab, icon7, "")
        self._ui.verticalLayout_3.addWidget(self._ui.tabWidget)
        self._ui.gridLayout_2.addLayout(self._ui.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self._ui.centralwidget)
        self._ui.menubar = QtWidgets.QMenuBar(MainWindow)
        self._ui.menubar.setGeometry(QtCore.QRect(0, 0, 787, 23))
        self._ui.menubar.setObjectName("menubar")
        self._ui.menuFile = QtWidgets.QMenu(self._ui.menubar)
        self._ui.menuFile.setObjectName("menuFile")
        self._ui.menuHelp = QtWidgets.QMenu(self._ui.menubar)
        self._ui.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self._ui.menubar)
        self._ui.statusbar = QtWidgets.QStatusBar(MainWindow)
        self._ui.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self._ui.statusbar)
        self._ui.actionWormhole = QtWidgets.QAction(MainWindow)
        self._ui.actionWormhole.setObjectName("actionWormhole")
        self._ui.actionOpenFile = QtWidgets.QAction(MainWindow)
        self._ui.actionOpenFile.setObjectName("actionOpenFile")
        self._ui.actionQuit = QtWidgets.QAction(MainWindow)
        self._ui.actionQuit.setObjectName("actionQuit")
        self._ui.actionViewGraph = QtWidgets.QAction(MainWindow)
        self._ui.actionViewGraph.setObjectName("actionViewGraph")
        self._ui.actionAbout = QtWidgets.QAction(MainWindow)
        self._ui.actionAbout.setObjectName("actionAbout")
        self._ui.menuFile.addAction(self._ui.actionWormhole)
        self._ui.menuFile.addSeparator()
        self._ui.menuFile.addAction(self._ui.actionQuit)
        self._ui.menuHelp.addAction(self._ui.actionAbout)
        self._ui.menubar.addAction(self._ui.menuFile.menuAction())
        self._ui.menubar.addAction(self._ui.menuHelp.menuAction())