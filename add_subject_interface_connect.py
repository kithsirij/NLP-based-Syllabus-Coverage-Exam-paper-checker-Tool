

__author__ = 'ASUS'
import sys
import MySQLdb
import numpy as np
from PyQt4.QtGui import *


from PyQt4 import QtCore
from PyQt4 import QtGui
from Interfaces import add_subject
from DB_Handling import DBHandler

db = MySQLdb.connect('localhost', 'root', '', 'new_pyproject')
cursor = db.cursor()

cursorNew = db.cursor(MySQLdb.cursors.DictCursor)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



class Addnewsubject(QDialog, add_subject.Ui_Dialog_add_subject):
    selectvalue = ""

    def __init__(self):
        super(Addnewsubject, self).__init__()

        self.setupUi(self)

        sql_student_year_retrival = "SELECT DISTINCT student_year FROM student_year_table"
        retriveYear = DBHandler().getData(sql_student_year_retrival)

        b = [str(text[0]) for text in retriveYear]

        for stu_year in b:
            self.comboBox_year.addItem(stu_year)

        self.comboBox_year.activated.connect(self.handleActivated_year)  # use to get combobox value
        self.comboBox_semester.activated.connect(self.handleActivated_semester)  # use to get combobox value
        self.pushButton_save.clicked.connect(self.saveSubject)
        self.tableWidget.cellClicked.connect(self.editsubject)
        self.pushButton_update.clicked.connect(self.updateQuestion)
        self.pushButton_delete.clicked.connect(self.deleteQuestion)

    def handleActivated_year(self, index):

        global com_text_year
        self.comboBox_semester.clear()
        self.tableWidget.clearContents()
        com_text_year = self.comboBox_year.itemText(index)
        print com_text_year
        sql_semester_retrival = "SELECT DISTINCT semester FROM student_year_table"
        retriveSemester = DBHandler().getData(sql_semester_retrival)

        b = [str(text[0]) for text in retriveSemester]

        for sem in b:
            self.comboBox_semester.addItem(sem)

    def addwidget(self,year,sem):
        select_Topic = "SELECT subject_name FROM add_subject where student_year='" + str(year) + "' and semester='" + str(sem) + "'"
        Max_Topic = DBHandler().getData(select_Topic)

        rows = len(Max_Topic)
        columns = len(Max_Topic[0])

        i = 0
        j = 0
        self.tableWidget.clearContents()
        for i in range(0, rows):
            for j in range(0, columns):
                item = QtGui.QTableWidgetItem((str(Max_Topic[i][j])))
                # print str(Max_Topic[i][1])
                self.tableWidget.setItem(i, j, item)


    def editsubject(self,row,column):
        try:
            print("Row %d and Column %d was clicked" % (row, column))
            item = self.tableWidget.itemAt(row, column)
            items = self.tableWidget.selectedItems()
            selectvalue = str(items[0].text())
            print(str(items[0].text()))

            self.textEdit.clear()
            self.textEdit.setText(str(items[0].text()))

        except IndexError:
            QtGui.QMessageBox.information(self, '', "You should have select a question")
            gotdata = 'null'

    def addwidgetFormSem(self,year,sem):
        select_Topic = "SELECT subject_name FROM add_subject where student_year='" + str(
            year) + "' and semester='" + str(sem) + "'"
        Max_Topic = DBHandler().getData(select_Topic)

        rows = len(Max_Topic)
        columns = len(Max_Topic[0])

        i = 0
        j = 0
        self.tableWidget.clearContents()
        for i in range(0, rows):
            for j in range(0, columns):
                item = QtGui.QTableWidgetItem((str(Max_Topic[i][j])))
                # print str(Max_Topic[i][1])
                self.tableWidget.setItem(i, j, item)

    def handleActivated_semester(self, index):
        self.tableWidget.clearContents()
        global com_text_sem
        com_text_sem = self.comboBox_semester.itemText(index)
        print com_text_sem
        self.addwidgetFormSem(com_text_year, com_text_sem)


    def saveSubject(self):
       print ""
       subject= self.lineEdit_subject_name.text()
       print(subject)
       print com_text_year
       print com_text_sem
       self.tableWidget.clearContents()
       self.lineEdit_subject_name.clear()

       insertsql = "insert into add_subject(subject_name,student_year,semester)values('" + str(
           subject) + "','" + str(com_text_year) + "','" + str(com_text_sem) + "')"

       DBHandler().setData(insertsql)
       self.addwidget(com_text_year, com_text_sem)

       QtGui.QMessageBox.question(None, 'Extract!', 'subject is inserted successfully..!!', QtGui.QMessageBox.Ok | QMessageBox.Cancel)

    def updateQuestion(self):

        update_question = self.textEdit.toPlainText()
        print 'UP >> ', update_question

        if update_question == "":
            print 'null'
            QtGui.QMessageBox.information(self, '', "You have to select a subject ")
        else:
            print 'has vaalue'


            quit_msg = "Are you sure you want to update ? "
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                items = self.tableWidget.selectedItems()
                print'>>>>>',(str(items[0].text()))

                update_subject = self.textEdit.toPlainText()
                print 'UP >> ',update_question

                delete_data_insert = "delete from add_subject where subject_name='" + str(items[0].text())+ "'"
                DBHandler().setData(delete_data_insert)

                insertsql = "insert into add_subject(subject_name,student_year,semester)values('" + str(
                    update_question) + "','" + str(com_text_year) + "','" + str(com_text_sem) + "')"
                DBHandler().setData(insertsql)

                select_Topic = "SELECT subject_name FROM add_subject where student_year='" + str(
                    com_text_year) + "' and semester='" + str(com_text_sem) + "'"
                Max_Topic=DBHandler().getData(select_Topic)

                rows = len(Max_Topic)
                columns = len(Max_Topic[0])

                i = 0
                j = 0
                self.tableWidget.clearContents()
                for i in range(0, rows):
                    for j in range(0, columns):
                        item = QtGui.QTableWidgetItem((str(Max_Topic[i][j])))
                        # print str(Max_Topic[i][1])
                        self.tableWidget.setItem(i, j, item)

    def deleteQuestion(self):

        try:
            items = self.tableWidget.selectedItems()
            selectvalue = str(items[0].text())
            # print(str(items[0].text()))

            quit_msg = "Are you sure you want to delete a question ? "
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:

                items = self.tableWidget.selectedItems()
                print'items>> del ', (str(items[0].text()))

                delete_data_insert = "delete from add_subject where subject_name='" + str(items[0].text()) + "'"
                DBHandler().setData(delete_data_insert)

                select_Topic = "SELECT subject_name FROM add_subject where student_year='" + str(
                    com_text_year) + "' and semester='" + str(com_text_sem) + "'"
                Max_Topic = DBHandler().getData(select_Topic)

                rows = len(Max_Topic)
                columns = len(Max_Topic[0])

                i = 0
                j = 0
                self.tableWidget.clearContents()
                for i in range(0, rows):
                    for j in range(0, columns):
                        item = QtGui.QTableWidgetItem((str(Max_Topic[i][j])))
                        # print str(Max_Topic[i][1])
                        self.tableWidget.setItem(i, j, item)

                self.lineEdit_subject_name.clear()
                QtGui.QMessageBox.information(self, '', "deleted succesfully")

            else:
                QtGui.QMessageBox.information(self, '', "Not delete")

        except IndexError:
            QtGui.QMessageBox.information(self, '', "You have to select a question")
            gotdata = 'null'


app = QtGui.QApplication(sys.argv)
ex = Addnewsubject()
# ex.show()
# ex.exec_()







