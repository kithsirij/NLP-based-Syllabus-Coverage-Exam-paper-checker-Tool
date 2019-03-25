# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_subject.ui'
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

class Ui_Dialog_add_subject(object):
    def setupUi(self, Dialog_add_subject):
        Dialog_add_subject.setObjectName(_fromUtf8("Dialog_add_subject"))
        Dialog_add_subject.resize(568, 374)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        Dialog_add_subject.setFont(font)
        Dialog_add_subject.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Qt_interface/SE_syllabus/4zIr6y.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_add_subject.setWindowIcon(icon)
        self.lbl_subject_name = QtGui.QLabel(Dialog_add_subject)
        self.lbl_subject_name.setGeometry(QtCore.QRect(50, 235, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lbl_subject_name.setFont(font)
        self.lbl_subject_name.setObjectName(_fromUtf8("lbl_subject_name"))
        self.label_add_subject = QtGui.QLabel(Dialog_add_subject)
        self.label_add_subject.setGeometry(QtCore.QRect(220, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_add_subject.setFont(font)
        self.label_add_subject.setObjectName(_fromUtf8("label_add_subject"))
        self.lineEdit_subject_name = QtGui.QLineEdit(Dialog_add_subject)
        self.lineEdit_subject_name.setGeometry(QtCore.QRect(190, 230, 321, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lineEdit_subject_name.setFont(font)
        self.lineEdit_subject_name.setObjectName(_fromUtf8("lineEdit_subject_name"))
        self.label_year = QtGui.QLabel(Dialog_add_subject)
        self.label_year.setGeometry(QtCore.QRect(50, 95, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_year.setFont(font)
        self.label_year.setObjectName(_fromUtf8("label_year"))
        self.label_semester = QtGui.QLabel(Dialog_add_subject)
        self.label_semester.setGeometry(QtCore.QRect(50, 165, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_semester.setFont(font)
        self.label_semester.setObjectName(_fromUtf8("label_semester"))
        self.pushButton_save = QtGui.QPushButton(Dialog_add_subject)
        self.pushButton_save.setGeometry(QtCore.QRect(190, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.pushButton_save.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Qt_interface/SE_syllabus/Save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon1)
        self.pushButton_save.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.pushButton_cancel = QtGui.QPushButton(Dialog_add_subject)
        self.pushButton_cancel.setGeometry(QtCore.QRect(340, 290, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        self.pushButton_cancel.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Qt_interface/SE_syllabus/if_draw-08_725558.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_cancel.setIcon(icon2)
        self.pushButton_cancel.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.comboBox_year = QtGui.QComboBox(Dialog_add_subject)
        self.comboBox_year.setGeometry(QtCore.QRect(190, 91, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_year.setFont(font)
        self.comboBox_year.setObjectName(_fromUtf8("comboBox_year"))
        self.comboBox_semester = QtGui.QComboBox(Dialog_add_subject)
        self.comboBox_semester.setGeometry(QtCore.QRect(190, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_semester.setFont(font)
        self.comboBox_semester.setObjectName(_fromUtf8("comboBox_semester"))

        self.retranslateUi(Dialog_add_subject)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_subject_name.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog_add_subject)

    def retranslateUi(self, Dialog_add_subject):
        Dialog_add_subject.setWindowTitle(_translate("Dialog_add_subject", "Dialog", None))
        self.lbl_subject_name.setText(_translate("Dialog_add_subject", "SUBJECT NAME", None))
        self.label_add_subject.setText(_translate("Dialog_add_subject", "ADD SUBJECT", None))
        self.label_year.setText(_translate("Dialog_add_subject", "YEAR", None))
        self.label_semester.setText(_translate("Dialog_add_subject", "SEMESTER", None))
        self.pushButton_save.setText(_translate("Dialog_add_subject", "SAVE", None))
        self.pushButton_cancel.setText(_translate("Dialog_add_subject", "CANCEL", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_add_subject = QtGui.QDialog()
    ui = Ui_Dialog_add_subject()
    ui.setupUi(Dialog_add_subject)
    Dialog_add_subject.show()
    sys.exit(app.exec_())

