# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_login(object):
    def setupUi(self, Dialog_login):
        Dialog_login.setObjectName(_fromUtf8("Dialog_login"))
        Dialog_login.resize(705, 348)
        Dialog_login.setStyleSheet(" background-image:url(SE_syllabus/videoblocks-two-feathers-down-moving-slowly-in-a-soft-light-decorative-blue-animation-for-background-or-illustration_rbxjcaiwz_thumbnail-full01.png)")


#         Dialog_login.setStyleSheet(_fromUtf8("QDialog{\n"
# "        background-image:url(:/newPrefix/videoblocks-two-feathers-down-moving-slowly-in-a-soft-light-decorative-blue-animation-for-background-or-illustration_rbxjcaiwz_thumbnail-full01.png)\n"
# "}"))
        self.groupBox = QtGui.QGroupBox(Dialog_login)
        self.groupBox.setGeometry(QtCore.QRect(320, 70, 341, 211))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_user_name = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_user_name.setGeometry(QtCore.QRect(130, 50, 189, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_user_name.setFont(font)
        self.lineEdit_user_name.setObjectName(_fromUtf8("lineEdit_user_name"))
        self.lineEdit_password = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_password.setGeometry(QtCore.QRect(130, 100, 189, 26))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setInputMask(_fromUtf8(""))
        self.lineEdit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.pushButton_login = QtGui.QPushButton(self.groupBox)
        self.pushButton_login.setGeometry(QtCore.QRect(130, 150, 91, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet(_fromUtf8(""))
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.pushButton = QtGui.QPushButton(Dialog_login)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 301, 281))
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border:1px;\n"
"}"))
        self.pushButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/gdqqylhslbhemylnuhrn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(300, 300))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog_login)
        QtCore.QMetaObject.connectSlotsByName(Dialog_login)

    def retranslateUi(self, Dialog_login):
        Dialog_login.setWindowTitle(_translate("Dialog_login", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog_login", "SignIn", None))
        self.label_2.setText(_translate("Dialog_login", "User Name", None))
        self.label_3.setText(_translate("Dialog_login", "Password", None))
        self.pushButton_login.setText(_translate("Dialog_login", "Login", None))

# import xy_rc
# import xz_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_login = QtGui.QDialog()
    ui = Ui_Dialog_login()
    ui.setupUi(Dialog_login)
    Dialog_login.show()
    sys.exit(app.exec_())

