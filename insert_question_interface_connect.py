
__author__ = 'ASUS'
import sys
import MySQLdb
import numpy as np
from PyQt4.QtGui import *


from PyQt4 import QtCore
from PyQt4 import QtGui
import insert_question
import database_insert_question_topic

db = MySQLdb.connect('localhost', 'root', '', 'new_pyproject')
cursor = db.cursor()

cursorNew = db.cursor(MySQLdb.cursors.DictCursor)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

com_text=''
question=''
class InsertQuestion(QDialog, insert_question.Ui_Dialog_insert_question):
    selectvalue = ""

    def __init__(self):
        super(InsertQuestion, self).__init__()

        self.setupUi(self)

        cursorNew.execute("""SELECT year_name FROM years""")
        yearname = cursorNew.fetchall()

        for years in yearname:
            self.comboBox_year_2.addItem(years["year_name"])

        cursorNew.execute("""SELECT DISTINCT student_year FROM student_year_table""")
        stu_year = cursorNew.fetchall()

        self.comboBox_year_2.activated.connect(self.handleActivated_yearsss)  # use to get combobox value

        for years in stu_year:
            self.comboBox_year.addItem(years["student_year"])

        self.comboBox_year.activated.connect(self.handleActivated_year)  # use to get combobox value
        self.comboBox_semester.activated.connect(self.handleActivated_semester)  # use to get combobox value
        self.cmb_select_process.activated.connect(self.handleActivated_subject)  # use to get combobox value
        self.btn_save.clicked.connect(self.save_questions)


    def handleActivated_yearsss(self,index):
        global yearss
        yearss=self.comboBox_year_2.itemText(index)

    def handleActivated_year(self, index):
        global com_text_year
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
        com_text_year = self.comboBox_year.itemText(index)
        # print com_text_year

        cursorNew.execute("""SELECT DISTINCT semester FROM student_year_table""")
        stu_semester = cursorNew.fetchall()

        for sem in stu_semester:
            self.comboBox_semester.addItem(sem["semester"])


    def handleActivated_semester(self, index):
        global com_text_sem
        com_text_sem = self.comboBox_semester.itemText(index)
        # print com_text_sem
        self.cmb_select_process.clear()

        # cursorNew.execute("""SELECT subject_name FROM add_subject where student_year=%s and semester=%s """,(com_text_year, com_text_sem))
        # sub_name = cursorNew.fetchall()

        cursorNew.execute("""SELECT DISTINCT subject_name FROM process_word_tfidf where student_year=%s and semester=%s """,(com_text_year, com_text_sem))
        sub_name = cursorNew.fetchall()

        for subject in sub_name:
            # print subject["subject_name"]
            self.cmb_select_process.addItem(subject["subject_name"])

    def handleActivated_subject(self, index):
        global com_text_sub
        com_text_sub = self.cmb_select_process.itemText(index)
        # print com_text_sub



    def save_questions(self):
        global question

        question=self.textEdit_question.toPlainText()

        print question
        print com_text_sub
        print com_text_year
        print com_text_sem
        print yearss


        database_insert_question_topic.GenerateBestDocument().subject_and_question(com_text_sub, question,com_text_year,com_text_sem,yearss)

        QtGui.QMessageBox.question(None, 'Extract!', 'question is inserted successfully..!!',
                                   QtGui.QMessageBox.Ok | QMessageBox.Cancel)


app = QtGui.QApplication(sys.argv)
ex = InsertQuestion()
# ex.show()
# ex.exec_()







