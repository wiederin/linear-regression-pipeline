# Form implementation generated from reading ui file 'controlboard.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import data_loader
import pandas as pd


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        # i added
        files = data_loader.find_files()

        # start generated code from updates
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1404, 746)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        mainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1401, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.data_module = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.data_module.setContentsMargins(0, 0, 0, 0)
        self.data_module.setObjectName("data_module")
        self.data_module_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_module_label.sizePolicy().hasHeightForWidth())
        self.data_module_label.setSizePolicy(sizePolicy)
        self.data_module_label.setMinimumSize(QtCore.QSize(0, 0))
        self.data_module_label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.data_module_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.data_module_label.setObjectName("data_module_label")
        self.data_module.addWidget(self.data_module_label)
        self.d_l_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_l_frame.sizePolicy().hasHeightForWidth())
        self.d_l_frame.setSizePolicy(sizePolicy)
        self.d_l_frame.setObjectName("d_l_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.d_l_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(30, 10, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalFrame_2 = QtWidgets.QFrame(self.d_l_frame)
        self.verticalFrame_2.setMaximumSize(QtCore.QSize(340, 16777215))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lfs_button = QtWidgets.QPushButton(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfs_button.sizePolicy().hasHeightForWidth())
        self.lfs_button.setSizePolicy(sizePolicy)
        self.lfs_button.setObjectName("lfs_button")
        self.verticalLayout.addWidget(self.lfs_button, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lf_button = QtWidgets.QPushButton(self.verticalFrame_2)
        self.lf_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lf_button.sizePolicy().hasHeightForWidth())
        self.lf_button.setSizePolicy(sizePolicy)
        self.lf_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lf_button.setObjectName("lf_button")
        self.verticalLayout.addWidget(self.lf_button)
        self.file_list_view = QtWidgets.QTableWidget(self.verticalFrame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_list_view.sizePolicy().hasHeightForWidth())
        self.file_list_view.setSizePolicy(sizePolicy)
        self.file_list_view.setMinimumSize(QtCore.QSize(300, 160))
        self.file_list_view.setMaximumSize(QtCore.QSize(130, 100))
        self.file_list_view.setObjectName("file_list_view")
        self.file_list_view.setColumnCount(1)
        self.file_list_view.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.file_list_view.setHorizontalHeaderItem(0, item)
        self.verticalLayout.addWidget(self.file_list_view)
        self.horizontalLayout_3.addWidget(self.verticalFrame_2)
        self.data_overview = QtWidgets.QPlainTextEdit(self.d_l_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_overview.sizePolicy().hasHeightForWidth())
        self.data_overview.setSizePolicy(sizePolicy)
        self.data_overview.setMaximumSize(QtCore.QSize(540, 300))
        self.data_overview.setObjectName("data_overview")
        self.horizontalLayout_3.addWidget(self.data_overview)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.d_l_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMaximumSize(QtCore.QSize(300, 120))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        self.data_module.addWidget(self.d_l_frame)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.data_module.addWidget(self.line)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 300, 591, 411))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.plotter_module = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.plotter_module.setContentsMargins(0, 0, 0, 0)
        self.plotter_module.setObjectName("plotter_module")
        self.plotter_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.plotter_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.plotter_label.setObjectName("plotter_label")
        self.plotter_module.addWidget(self.plotter_label)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(590, 300, 811, 411))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.trainer_module = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.trainer_module.setContentsMargins(0, 0, 0, 0)
        self.trainer_module.setObjectName("trainer_module")
        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.trainer_module.addWidget(self.line_2)
        self.trainer_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.trainer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.trainer_label.setObjectName("trainer_label")
        self.trainer_module.addWidget(self.trainer_label)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        # end of generated code from updates

        # i added
        self.lfs_button.clicked.connect(self.lfs_button_called)
        self.lf_button.clicked.connect(self.lf_button_called)

        self.file_list_view.setHorizontalHeaderLabels(["file"])
        self.file_list_view.setColumnCount(1)
        self.file_list_view.setRowCount(len(files))
        self.file_list_view.setColumnWidth(0, 300)
        for i, file in enumerate(files):
            item = QTableWidgetItem(file)
            self.file_list_view.setItem(i, 0, item)
        # end

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "controlboard"))
        self.data_module_label.setText(_translate("mainWindow", "data loader"))
        self.lfs_button.setText(_translate("mainWindow", "reload available files"))
        self.lf_button.setText(_translate("mainWindow", "load file"))
        self.plotter_label.setText(_translate("mainWindow", "plotter"))
        self.trainer_label.setText(_translate("mainWindow", "trainer"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))


    def lfs_button_called(self):
        self.file_list_view.clear()
        self.file_list_view.setHorizontalHeaderLabels(["file"])
        files = data_loader.find_files()
        for i, file in enumerate(files):
            item = QTableWidgetItem(file)
            self.file_list_view.setItem(i, 0, item)

    def lf_button_called(self):
        _translate = QtCore.QCoreApplication.translate
        path = self.file_list_view.selectedItems()[0].data(0)
        # parse csv
        df = pd.read_csv(path)
        self.data_overview.clear()
        self.data_overview.insertPlainText(str(df))


import sys
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())