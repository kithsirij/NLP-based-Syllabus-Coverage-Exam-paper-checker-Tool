# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_topic_with_content.ui'
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

class Ui_Dialog_add_topic_content(object):
    def setupUi(self, Dialog_add_topic_content):
        Dialog_add_topic_content.setObjectName(_fromUtf8("Dialog_add_topic_content"))
        Dialog_add_topic_content.resize(1042, 406)
        self.cmb_select_subject = QtGui.QComboBox(Dialog_add_topic_content)
        self.cmb_select_subject.setGeometry(QtCore.QRect(230, 210, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.cmb_select_subject.setFont(font)
        self.cmb_select_subject.setObjectName(_fromUtf8("cmb_select_subject"))
        self.label_4 = QtGui.QLabel(Dialog_add_topic_content)
        self.label_4.setGeometry(QtCore.QRect(400, 20, 281, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.btn_clear = QtGui.QPushButton(Dialog_add_topic_content)
        self.btn_clear.setGeometry(QtCore.QRect(390, 340, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.btn_clear.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/if_draw-08_725558.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon)
        self.btn_clear.setIconSize(QtCore.QSize(25, 25))
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.btn_add_content = QtGui.QPushButton(Dialog_add_topic_content)
        self.btn_add_content.setGeometry(QtCore.QRect(230, 340, 130, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.btn_add_content.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/folder_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_content.setIcon(icon1)
        self.btn_add_content.setIconSize(QtCore.QSize(25, 25))
        self.btn_add_content.setObjectName(_fromUtf8("btn_add_content"))
        self.lbl_topic = QtGui.QLabel(Dialog_add_topic_content)
        self.lbl_topic.setGeometry(QtCore.QRect(40, 287, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lbl_topic.setFont(font)
        self.lbl_topic.setObjectName(_fromUtf8("lbl_topic"))
        self.lineEdit_add_topic = QtGui.QLineEdit(Dialog_add_topic_content)
        self.lineEdit_add_topic.setGeometry(QtCore.QRect(230, 280, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lineEdit_add_topic.setFont(font)
        self.lineEdit_add_topic.setObjectName(_fromUtf8("lineEdit_add_topic"))
        self.lbl_select_subject = QtGui.QLabel(Dialog_add_topic_content)
        self.lbl_select_subject.setGeometry(QtCore.QRect(40, 216, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lbl_select_subject.setFont(font)
        self.lbl_select_subject.setObjectName(_fromUtf8("lbl_select_subject"))
        self.lbl_add_content = QtGui.QLabel(Dialog_add_topic_content)
        self.lbl_add_content.setGeometry(QtCore.QRect(40, 347, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lbl_add_content.setFont(font)
        self.lbl_add_content.setObjectName(_fromUtf8("lbl_add_content"))
        self.label_year = QtGui.QLabel(Dialog_add_topic_content)
        self.label_year.setGeometry(QtCore.QRect(40, 76, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_year.setFont(font)
        self.label_year.setObjectName(_fromUtf8("label_year"))
        self.comboBox_semester = QtGui.QComboBox(Dialog_add_topic_content)
        self.comboBox_semester.setGeometry(QtCore.QRect(230, 145, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_semester.setFont(font)
        self.comboBox_semester.setObjectName(_fromUtf8("comboBox_semester"))
        self.comboBox_year = QtGui.QComboBox(Dialog_add_topic_content)
        self.comboBox_year.setGeometry(QtCore.QRect(230, 71, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_year.setFont(font)
        self.comboBox_year.setObjectName(_fromUtf8("comboBox_year"))
        self.label_semester = QtGui.QLabel(Dialog_add_topic_content)
        self.label_semester.setGeometry(QtCore.QRect(40, 150, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_semester.setFont(font)
        self.label_semester.setObjectName(_fromUtf8("label_semester"))
        self.listWidget = QtGui.QListWidget(Dialog_add_topic_content)
        self.listWidget.setGeometry(QtCore.QRect(560, 70, 441, 301))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Dialog_add_topic_content)
        QtCore.QObject.connect(self.btn_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_add_topic.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog_add_topic_content)

    def retranslateUi(self, Dialog_add_topic_content):
        Dialog_add_topic_content.setWindowTitle(_translate("Dialog_add_topic_content", "Dialog", None))
        self.label_4.setText(_translate("Dialog_add_topic_content", "ADD TOPIC AND CONTENT", None))
        self.btn_clear.setText(_translate("Dialog_add_topic_content", "CLEAR", None))
        self.btn_add_content.setText(_translate("Dialog_add_topic_content", "ADD CONTENT", None))
        self.lbl_topic.setText(_translate("Dialog_add_topic_content", "ADD TOPIC", None))
        self.lbl_select_subject.setText(_translate("Dialog_add_topic_content", "SELECT SUBJECT", None))
        self.lbl_add_content.setText(_translate("Dialog_add_topic_content", "ADD CONTENT", None))
        self.label_year.setText(_translate("Dialog_add_topic_content", "YEAR", None))
        self.label_semester.setText(_translate("Dialog_add_topic_content", "SEMESTER", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_add_topic_content = QtGui.QDialog()
    ui = Ui_Dialog_add_topic_content()
    ui.setupUi(Dialog_add_topic_content)
    Dialog_add_topic_content.show()
    sys.exit(app.exec_())

