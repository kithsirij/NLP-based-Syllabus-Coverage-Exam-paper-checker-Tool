
__author__ = 'ASUS'
import sys
import MySQLdb
import numpy as np
from PyQt4.QtGui import *


from PyQt4 import QtCore
from PyQt4 import QtGui
import update_delete
import database_insert_question_topic
from DB_Handling import DBHandler


# db = MySQLdb.connect('localhost', 'root', '', 'pyproject')
# cursor = db.cursor()
#
# cursorNew = db.cursor(MySQLdb.cursors.DictCursor)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

com_text=''
question=''
count_question=0
class LoadQuestion(QDialog, update_delete.Ui_Dialog_update_or_delete_question):
    selectvalue = ""

    def __init__(self):
        super(LoadQuestion, self).__init__()

        self.setupUi(self)

        sql_year_retrival = "SELECT DISTINCT years FROM insert_question"
        retriveYear = DBHandler().getData(sql_year_retrival)

        b1 = [str(text[0]) for text in retriveYear]

        for yearss in b1:
            self.comboBox_year.addItem(yearss)

        self.comboBox_year.activated.connect(self.handleActivated_yearss)  # use to get combobox value


        sql_student_year_retrival="SELECT DISTINCT student_year FROM student_year_table"
        retriveYear = DBHandler().getData(sql_student_year_retrival)

        b = [str(text[0]) for text in retriveYear]

        for stu_year in b:
            self.comboBox_student_year.addItem(stu_year)

        self.comboBox_student_year.activated.connect(self.handleActivated_year)  # use to get combobox value
        self.comboBox_semester.activated.connect(self.handleActivated_semester)  # use to get combobox value
        self.cmb_select_process.activated.connect(self.handleActivated_subject)  # use to get combobox value
        self.tableWidget.cellClicked.connect(self.editsubject)
        self.pushButton_update.clicked.connect(self.updateQuestion)
        self.pushButton_delete.clicked.connect(self.deleteQuestion)

    def handleActivated_yearss(self,index):
        global yearss
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
        self.tableWidget.clearContents()

        yearss=self.comboBox_year.itemText(index)


    def handleActivated_year(self, index):
        global com_text_year
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
        self.tableWidget.clearContents()
        com_text_year = self.comboBox_student_year.itemText(index)
        # print com_text_year

        sql_semester_retrival = "SELECT DISTINCT semester FROM student_year_table"
        retriveSemester = DBHandler().getData(sql_semester_retrival)

        b = [str(text[0]) for text in retriveSemester]

        for sem in b:
            self.comboBox_semester.addItem(sem)

    def handleActivated_semester(self, index):
        global com_text_sem
        com_text_sem = self.comboBox_semester.itemText(index)
        # print com_text_sem
        # print com_text_year
        self.cmb_select_process.clear()
        self.tableWidget.clearContents()

        sql_subject_retrival = "SELECT DISTINCT subject_name FROM insert_question WHERE student_year='"+str(com_text_year)+"' and semester='"+str(com_text_sem)+"' and years='"+str(yearss)+"'"
        retriveSubject = DBHandler().getData(sql_subject_retrival)

        b_sub = [str(text[0]) for text in retriveSubject]

        for subject in b_sub:
            # print subject
            # print subject["subject_name"]
            self.cmb_select_process.addItem(subject)


    def handleActivated_subject(self,index):
        global com_text_sub
        self.tableWidget.clearContents()

        com_text_sub=self.cmb_select_process.itemText(index)
        print yearss
        print com_text_year
        print com_text_sem
        print com_text_sub

        selectData = "SELECT DISTINCT question FROM insert_question WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and years='" + str(
            yearss) + "' and subject_name='" + str(com_text_sub) + "' "

        wup_list = DBHandler().getData(selectData)

        print '>>>>>', wup_list
        ########################################################
        # print wup_list[0]     means topic and tfidf
        # print wup_list[0][0]     means topic only
        # print wup_list[0][1]     means idf only
        #########################################################


        rows = len(wup_list)
        columns = len(wup_list[0])

        print 'rows and columns ',rows,columns

        i = 0
        j = 0
        self.tableWidget.clearContents()
        for i in range(0, rows):
            for j in range(0, columns):
                item = QtGui.QTableWidgetItem((str(wup_list[i][j])))
                # print str(wup_list[i][1])
                self.tableWidget.setItem(i, j, item)

        # print '>>>', wup_list[0][1]

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


    def updateQuestion(self):

        update_question = self.textEdit.toPlainText()
        print 'UP >> ', update_question

        if update_question == "":
            print 'null'
            QtGui.QMessageBox.information(self, '', "You have to select a question ")
        else:
            print 'has vaalue'


            quit_msg = "Are you sure you want to update ? "
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                items = self.tableWidget.selectedItems()
                print'>>>>>',(str(items[0].text()))

                update_question = self.textEdit.toPlainText()
                print 'UP >> ',update_question

                delete_data_insert = "delete from insert_question where question='" + str(items[0].text())+ "'"
                DBHandler().setData(delete_data_insert)

                delete_data_max = "delete from question_max_tfidf where question='" + str(items[0].text()) + "'"
                DBHandler().setData(delete_data_max)

                database_insert_question_topic.GenerateBestDocument().subject_and_question(com_text_sub,update_question,com_text_year, com_text_sem, yearss)

                selectData = "SELECT DISTINCT question FROM insert_question WHERE student_year='" + str(
                    com_text_year) + "' and semester='" + str(com_text_sem) + "' and years='" + str(
                    yearss) + "' and subject_name='" + str(com_text_sub) + "' "

                wup_list = DBHandler().getData(selectData)

                print '>>>>>', wup_list
                ########################################################
                # print wup_list[0]     means topic and tfidf
                # print wup_list[0][0]     means topic only
                # print wup_list[0][1]     means idf only
                #########################################################


                rows = len(wup_list)
                columns = len(wup_list[0])

                print 'rows and columns ', rows, columns

                i = 0
                j = 0
                self.tableWidget.clearContents()
                for i in range(0, rows):
                    for j in range(0, columns):
                        item = QtGui.QTableWidgetItem((str(wup_list[i][j])))
                        # print str(wup_list[i][1])
                        self.tableWidget.setItem(i, j, item)
                QtGui.QMessageBox.information(self, '', "Update successfully")

            else:
                QtGui.QMessageBox.information(self, '', "Nothing Changed")

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

                delete_data_insert = "delete from insert_question where question='" + str(items[0].text()) + "'"
                DBHandler().setData(delete_data_insert)

                delete_data_max = "delete from question_max_tfidf where question='" + str(items[0].text()) + "'"
                DBHandler().setData(delete_data_max)

                selectData = "SELECT DISTINCT question FROM insert_question WHERE student_year='" + str(
                    com_text_year) + "' and semester='" + str(com_text_sem) + "' and years='" + str(
                    yearss) + "' and subject_name='" + str(com_text_sub) + "' "

                wup_list = DBHandler().getData(selectData)

                print '>>>>>', wup_list
                ########################################################
                # print wup_list[0]     means topic and tfidf
                # print wup_list[0][0]     means topic only
                # print wup_list[0][1]     means idf only
                #########################################################


                rows = len(wup_list)
                columns = len(wup_list[0])

                print 'rows and columns ', rows, columns

                i = 0
                j = 0
                self.tableWidget.clearContents()
                for i in range(0, rows):
                    for j in range(0, columns):
                        item = QtGui.QTableWidgetItem((str(wup_list[i][j])))
                        # print str(wup_list[i][1])
                        self.tableWidget.setItem(i, j, item)
                QtGui.QMessageBox.information(self, '', "deleted succesfully")

            else:
                QtGui.QMessageBox.information(self, '', "Not delete")

        except IndexError:
            QtGui.QMessageBox.information(self, '', "You have to select a question")
            gotdata = 'null'






app = QtGui.QApplication(sys.argv)
ex = LoadQuestion()
# ex.show()
# ex.exec_()