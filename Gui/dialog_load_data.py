# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_load_data.ui'
#
# Created: Tue Apr  5 17:49:05 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 500)
        Dialog.setMinimumSize(QtCore.QSize(600, 500))
        Dialog.setMaximumSize(QtCore.QSize(600, 500))
        self.comboBox_data_format = QtGui.QComboBox(Dialog)
        self.comboBox_data_format.setGeometry(QtCore.QRect(40, 50, 251, 27))
        self.comboBox_data_format.setObjectName("comboBox_data_format")
        self.comboBox_data_format.addItem("")
        self.comboBox_data_format.addItem("")
        self.comboBox_data_format.addItem("")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 101, 17))
        self.label.setObjectName("label")
        self.btn_data_import_path = QtGui.QPushButton(Dialog)
        self.btn_data_import_path.setGeometry(QtCore.QRect(400, 180, 99, 27))
        self.btn_data_import_path.setObjectName("btn_data_import_path")
        self.text_data_import_path = QtGui.QLineEdit(Dialog)
        self.text_data_import_path.setGeometry(QtCore.QRect(40, 180, 351, 27))
        self.text_data_import_path.setText("")
        self.text_data_import_path.setObjectName("text_data_import_path")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 151, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 230, 141, 17))
        self.label_3.setObjectName("label_3")
        self.text_data_output_folder = QtGui.QLineEdit(Dialog)
        self.text_data_output_folder.setGeometry(QtCore.QRect(40, 250, 351, 27))
        self.text_data_output_folder.setObjectName("text_data_output_folder")
        self.btn_data_output_folder = QtGui.QPushButton(Dialog)
        self.btn_data_output_folder.setGeometry(QtCore.QRect(400, 250, 99, 27))
        self.btn_data_output_folder.setObjectName("btn_data_output_folder")
        self.btn_ok = QtGui.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(410, 350, 99, 27))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtGui.QPushButton(Dialog)
        self.btn_cancel.setGeometry(QtCore.QRect(300, 350, 99, 27))
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Import Data", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_data_format.setItemText(0, QtGui.QApplication.translate("Dialog", "Single Image", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_data_format.setItemText(1, QtGui.QApplication.translate("Dialog", "Multiple Images", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_data_format.setItemText(2, QtGui.QApplication.translate("Dialog", "OrthoMap", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Data Format:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_data_import_path.setText(QtGui.QApplication.translate("Dialog", "Select File(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Imported Data path:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Export Results to:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_data_output_folder.setText(QtGui.QApplication.translate("Dialog", "Select Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setText(QtGui.QApplication.translate("Dialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

