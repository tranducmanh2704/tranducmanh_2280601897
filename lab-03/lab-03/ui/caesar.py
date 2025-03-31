# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/caesar.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 10, 201, 41))
        self.label.setObjectName("label")
        self.PlainText = QtWidgets.QLabel(self.centralwidget)
        self.PlainText.setGeometry(QtCore.QRect(50, 100, 71, 16))
        self.PlainText.setObjectName("PlainText")
        self.KE = QtWidgets.QLabel(self.centralwidget)
        self.KE.setGeometry(QtCore.QRect(60, 220, 55, 16))
        self.KE.setMaximumSize(QtCore.QSize(55, 16))
        self.KE.setObjectName("KE")
        self.CIPHER = QtWidgets.QLabel(self.centralwidget)
        self.CIPHER.setGeometry(QtCore.QRect(40, 350, 81, 16))
        self.CIPHER.setObjectName("CIPHER")
        self.btn_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(180, 440, 93, 28))
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(400, 440, 93, 28))
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.txt_plain_text = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_plain_text.setGeometry(QtCore.QRect(140, 60, 441, 87))
        self.txt_plain_text.setObjectName("txt_plain_text")
        self.txt_key = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_key.setGeometry(QtCore.QRect(140, 190, 431, 87))
        self.txt_key.setObjectName("txt_key")
        self.txt_ciphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(140, 320, 411, 87))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">CAESAR CIPHER</span></p></body></html>"))
        self.PlainText.setText(_translate("MainWindow", "Plain Text:"))
        self.KE.setText(_translate("MainWindow", "Key:"))
        self.CIPHER.setText(_translate("MainWindow", "CipherText:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
