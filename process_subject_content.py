# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process_subject_content.ui'
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

class Ui_Dialog_process(object):
    def setupUi(self, Dialog_process):
        Dialog_process.setObjectName(_fromUtf8("Dialog_process"))
        Dialog_process.resize(864, 672)
        self.cmb_select_process = QtGui.QComboBox(Dialog_process)
        self.cmb_select_process.setGeometry(QtCore.QRect(530, 133, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.cmb_select_process.setFont(font)
        self.cmb_select_process.setObjectName(_fromUtf8("cmb_select_process"))
        self.lbl_select_subject = QtGui.QLabel(Dialog_process)
        self.lbl_select_subject.setGeometry(QtCore.QRect(350, 138, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lbl_select_subject.setFont(font)
        self.lbl_select_subject.setObjectName(_fromUtf8("lbl_select_subject"))
        self.btn_process = QtGui.QPushButton(Dialog_process)
        self.btn_process.setGeometry(QtCore.QRect(40, 610, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.btn_process.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/14d42564.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_process.setIcon(icon)
        self.btn_process.setIconSize(QtCore.QSize(24, 24))
        self.btn_process.setObjectName(_fromUtf8("btn_process"))
        self.lbl_process = QtGui.QLabel(Dialog_process)
        self.lbl_process.setGeometry(QtCore.QRect(370, 20, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_process.setFont(font)
        self.lbl_process.setObjectName(_fromUtf8("lbl_process"))
        self.label_year = QtGui.QLabel(Dialog_process)
        self.label_year.setGeometry(QtCore.QRect(40, 76, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_year.setFont(font)
        self.label_year.setObjectName(_fromUtf8("label_year"))
        self.comboBox_semester = QtGui.QComboBox(Dialog_process)
        self.comboBox_semester.setGeometry(QtCore.QRect(160, 134, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_semester.setFont(font)
        self.comboBox_semester.setObjectName(_fromUtf8("comboBox_semester"))
        self.comboBox_year = QtGui.QComboBox(Dialog_process)
        self.comboBox_year.setGeometry(QtCore.QRect(160, 71, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.comboBox_year.setFont(font)
        self.comboBox_year.setObjectName(_fromUtf8("comboBox_year"))
        self.label_semester = QtGui.QLabel(Dialog_process)
        self.label_semester.setGeometry(QtCore.QRect(40, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_semester.setFont(font)
        self.label_semester.setObjectName(_fromUtf8("label_semester"))
        self.tableWidget = QtGui.QTableWidget(Dialog_process)
        self.tableWidget.setGeometry(QtCore.QRect(40, 200, 781, 244))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(40)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.pushButton_delete = QtGui.QPushButton(Dialog_process)
        self.pushButton_delete.setGeometry(QtCore.QRect(360, 550, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.pushButton_delete.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/Delete_Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon1)
        self.pushButton_delete.setIconSize(QtCore.QSize(22, 21))
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.pushButton_update_content = QtGui.QPushButton(Dialog_process)
        self.pushButton_update_content.setGeometry(QtCore.QRect(200, 550, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.pushButton_update_content.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_update_content.setIcon(icon2)
        self.pushButton_update_content.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_update_content.setObjectName(_fromUtf8("pushButton_update_content"))
        self.label_question = QtGui.QLabel(Dialog_process)
        self.label_question.setGeometry(QtCore.QRect(40, 467, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_question.setFont(font)
        self.label_question.setObjectName(_fromUtf8("label_question"))
        self.lineEdit_topic = QtGui.QLineEdit(Dialog_process)
        self.lineEdit_topic.setGeometry(QtCore.QRect(40, 500, 601, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.lineEdit_topic.setFont(font)
        self.lineEdit_topic.setObjectName(_fromUtf8("lineEdit_topic"))
        self.pushButton_update_topic = QtGui.QPushButton(Dialog_process)
        self.pushButton_update_topic.setGeometry(QtCore.QRect(40, 550, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(10)
        self.pushButton_update_topic.setFont(font)
        self.pushButton_update_topic.setIcon(icon2)
        self.pushButton_update_topic.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_update_topic.setObjectName(_fromUtf8("pushButton_update_topic"))

        self.retranslateUi(Dialog_process)
        QtCore.QMetaObject.connectSlotsByName(Dialog_process)

    def retranslateUi(self, Dialog_process):
        Dialog_process.setWindowTitle(_translate("Dialog_process", "Dialog", None))
        self.lbl_select_subject.setText(_translate("Dialog_process", "SELECT  SUBJECT", None))
        self.btn_process.setText(_translate("Dialog_process", "PROCESS", None))
        self.lbl_process.setText(_translate("Dialog_process", "PROCESS", None))
        self.label_year.setText(_translate("Dialog_process", "YEAR", None))
        self.label_semester.setText(_translate("Dialog_process", "SEMESTER", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_process", "TOPIC", None))
        self.pushButton_delete.setText(_translate("Dialog_process", "DELETE", None))
        self.pushButton_update_content.setText(_translate("Dialog_process", "UPDATE CONTENT", None))
        self.label_question.setText(_translate("Dialog_process", "TOPIC", None))
        self.pushButton_update_topic.setText(_translate("Dialog_process", "UPDATE TOPIC", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_process = QtGui.QDialog()
    ui = Ui_Dialog_process()
    ui.setupUi(Dialog_process)
    Dialog_process.show()
    sys.exit(app.exec_())
