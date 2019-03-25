# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert_question.ui'
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

class Ui_Dialog_insert_question(object):
    def setupUi(self, Dialog_insert_question):
        Dialog_insert_question.setObjectName(_fromUtf8("Dialog_insert_question"))
        Dialog_insert_question.resize(570, 589)
        self.label_year = QtGui.QLabel(Dialog_insert_question)
        self.label_year.setGeometry(QtCore.QRect(60, 166, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_year.setFont(font)
        self.label_year.setObjectName(_fromUtf8("label_year"))
        self.comboBox_year = QtGui.QComboBox(Dialog_insert_question)
        self.comboBox_year.setGeometry(QtCore.QRect(220, 161, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_year.setFont(font)
        self.comboBox_year.setObjectName(_fromUtf8("comboBox_year"))
        self.comboBox_semester = QtGui.QComboBox(Dialog_insert_question)
        self.comboBox_semester.setGeometry(QtCore.QRect(220, 234, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_semester.setFont(font)
        self.comboBox_semester.setObjectName(_fromUtf8("comboBox_semester"))
        self.lbl_select_subject = QtGui.QLabel(Dialog_insert_question)
        self.lbl_select_subject.setGeometry(QtCore.QRect(60, 309, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lbl_select_subject.setFont(font)
        self.lbl_select_subject.setObjectName(_fromUtf8("lbl_select_subject"))
        self.cmb_select_process = QtGui.QComboBox(Dialog_insert_question)
        self.cmb_select_process.setGeometry(QtCore.QRect(220, 304, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.cmb_select_process.setFont(font)
        self.cmb_select_process.setObjectName(_fromUtf8("cmb_select_process"))
        self.label_semester = QtGui.QLabel(Dialog_insert_question)
        self.label_semester.setGeometry(QtCore.QRect(60, 240, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_semester.setFont(font)
        self.label_semester.setObjectName(_fromUtf8("label_semester"))
        self.label_insert_question = QtGui.QLabel(Dialog_insert_question)
        self.label_insert_question.setGeometry(QtCore.QRect(181, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_insert_question.setFont(font)
        self.label_insert_question.setObjectName(_fromUtf8("label_insert_question"))
        self.btn_cancel = QtGui.QPushButton(Dialog_insert_question)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 530, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.btn_cancel.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Qt_interface/SE_syllabus/if_draw-08_725558.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon)
        self.btn_cancel.setIconSize(QtCore.QSize(20, 20))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.lbl_question = QtGui.QLabel(Dialog_insert_question)
        self.lbl_question.setGeometry(QtCore.QRect(60, 370, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_question.setFont(font)
        self.lbl_question.setObjectName(_fromUtf8("lbl_question"))
        self.btn_save = QtGui.QPushButton(Dialog_insert_question)
        self.btn_save.setGeometry(QtCore.QRect(60, 530, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.btn_save.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Qt_interface/SE_syllabus/Save-as.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QtCore.QSize(20, 20))
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.textEdit_question = QtGui.QTextEdit(Dialog_insert_question)
        self.textEdit_question.setGeometry(QtCore.QRect(60, 410, 451, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.textEdit_question.setFont(font)
        self.textEdit_question.setObjectName(_fromUtf8("textEdit_question"))
        self.label_year_2 = QtGui.QLabel(Dialog_insert_question)
        self.label_year_2.setGeometry(QtCore.QRect(60, 95, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_year_2.setFont(font)
        self.label_year_2.setObjectName(_fromUtf8("label_year_2"))
        self.comboBox_year_2 = QtGui.QComboBox(Dialog_insert_question)
        self.comboBox_year_2.setGeometry(QtCore.QRect(220, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_year_2.setFont(font)
        self.comboBox_year_2.setObjectName(_fromUtf8("comboBox_year_2"))

        self.retranslateUi(Dialog_insert_question)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textEdit_question.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog_insert_question)

    def retranslateUi(self, Dialog_insert_question):
        Dialog_insert_question.setWindowTitle(_translate("Dialog_insert_question", "Dialog", None))
        self.label_year.setText(_translate("Dialog_insert_question", "STUDENT  YEAR", None))
        self.lbl_select_subject.setText(_translate("Dialog_insert_question", "SELECT  SUBJECT", None))
        self.label_semester.setText(_translate("Dialog_insert_question", "SEMESTER", None))
        self.label_insert_question.setText(_translate("Dialog_insert_question", "INSERT QUESTIONS", None))
        self.btn_cancel.setText(_translate("Dialog_insert_question", "CANCEL", None))
        self.lbl_question.setText(_translate("Dialog_insert_question", "QUESTION", None))
        self.btn_save.setText(_translate("Dialog_insert_question", "SAVE", None))
        self.label_year_2.setText(_translate("Dialog_insert_question", "YEAR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_insert_question = QtGui.QDialog()
    ui = Ui_Dialog_insert_question()
    ui.setupUi(Dialog_insert_question)
    Dialog_insert_question.show()
    sys.exit(app.exec_())

