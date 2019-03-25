# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tagging.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(669, 434)
        self.lbl_select_subject = QtGui.QLabel(Dialog)
        self.lbl_select_subject.setGeometry(QtCore.QRect(40, 240, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lbl_select_subject.setFont(font)
        self.lbl_select_subject.setObjectName(_fromUtf8("lbl_select_subject"))
        self.comboBox_semester = QtGui.QComboBox(Dialog)
        self.comboBox_semester.setGeometry(QtCore.QRect(210, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_semester.setFont(font)
        self.comboBox_semester.setObjectName(_fromUtf8("comboBox_semester"))
        self.label_student_year = QtGui.QLabel(Dialog)
        self.label_student_year.setGeometry(QtCore.QRect(40, 126, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_student_year.setFont(font)
        self.label_student_year.setObjectName(_fromUtf8("label_student_year"))
        self.label_semester = QtGui.QLabel(Dialog)
        self.label_semester.setGeometry(QtCore.QRect(40, 185, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_semester.setFont(font)
        self.label_semester.setObjectName(_fromUtf8("label_semester"))
        self.label_year = QtGui.QLabel(Dialog)
        self.label_year.setGeometry(QtCore.QRect(40, 66, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_year.setFont(font)
        self.label_year.setObjectName(_fromUtf8("label_year"))
        self.comboBox_student_year = QtGui.QComboBox(Dialog)
        self.comboBox_student_year.setGeometry(QtCore.QRect(210, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_student_year.setFont(font)
        self.comboBox_student_year.setObjectName(_fromUtf8("comboBox_student_year"))
        self.comboBox_year = QtGui.QComboBox(Dialog)
        self.comboBox_year.setGeometry(QtCore.QRect(210, 61, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_year.setFont(font)
        self.comboBox_year.setObjectName(_fromUtf8("comboBox_year"))
        self.cmb_select_process = QtGui.QComboBox(Dialog)
        self.cmb_select_process.setGeometry(QtCore.QRect(40, 280, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.cmb_select_process.setFont(font)
        self.cmb_select_process.setObjectName(_fromUtf8("cmb_select_process"))
        self.pushButton_similarity = QtGui.QPushButton(Dialog)
        self.pushButton_similarity.setGeometry(QtCore.QRect(40, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.pushButton_similarity.setFont(font)
        self.pushButton_similarity.setObjectName(_fromUtf8("pushButton_similarity"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_select_subject.setText(_translate("Dialog", "SELECT  SUBJECT", None))
        self.label_student_year.setText(_translate("Dialog", "STUDENT YEAR", None))
        self.label_semester.setText(_translate("Dialog", "SEMESTER", None))
        self.label_year.setText(_translate("Dialog", "YEAR", None))
        self.pushButton_similarity.setText(_translate("Dialog", "similarity", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

