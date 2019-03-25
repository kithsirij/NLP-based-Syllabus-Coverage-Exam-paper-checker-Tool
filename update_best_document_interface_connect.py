
__author__ = 'ASUS'
import sys
import MySQLdb
import numpy as np
from PyQt4.QtGui import *


from PyQt4 import QtCore
from PyQt4 import QtGui
import best_document
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
class LoadQuestion(QDialog, best_document.Ui_Dialog_best_document):
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

        sql_student_year_retrival = "SELECT DISTINCT student_year FROM student_year_table"
        retriveYear = DBHandler().getData(sql_student_year_retrival)

        b = [str(text[0]) for text in retriveYear]

        for stu_year in b:
            self.comboBox_student_year.addItem(stu_year)

        self.comboBox_student_year.activated.connect(self.handleActivated_year)  # use to get combobox value
        self.comboBox_semester.activated.connect(self.handleActivated_semester)  # use to get combobox value
        self.cmb_select_process.activated.connect(self.handleActivated_subject)  # use to get combobox value
        self.cmb_select_topic.activated.connect(self.load_questions)  # use to get combobox value


    def handleActivated_yearss(self, index):
        global yearss
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
        self.cmb_select_topic.clear()
        self.tableWidget.clearContents()

        yearss = self.comboBox_year.itemText(index)

    def handleActivated_year(self, index):
        global com_text_year
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
        self.tableWidget.clearContents()
        self.cmb_select_topic.clear()
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
        self.cmb_select_process.clear()

        sql_subject_retrival = "SELECT DISTINCT subject_name FROM insert_question WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and years='" + str(yearss) + "'"
        retriveSubject = DBHandler().getData(sql_subject_retrival)

        b_sub = [str(text[0]) for text in retriveSubject]

        for subject in b_sub:
            # print subject["subject_name"]
            self.cmb_select_process.addItem(subject)


    def handleActivated_subject(self,index):
        global com_text
        self.cmb_select_topic.clear()
        com_text = self.cmb_select_process.itemText(index)
        print com_text

        sql_question_retrival = "SELECT DISTINCT question FROM insert_question WHERE subject_name='" + str(com_text) + " ' and student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and years='" + str(yearss) + "' "
        retriveQuestion = DBHandler().getData(sql_question_retrival)

        b = [str(text[0]) for text in retriveQuestion]
        for q_sion in b:
            print q_sion

            self.cmb_select_topic.addItem(q_sion)


    def load_questions(self,index):


        table_question = self.cmb_select_topic.itemText(index)
        table_subject=self.cmb_select_process.itemText(index)

        print table_question,'>>'

        # cursorNew.execute("""SELECT topic,question,tfidf FROM insert_question_topic WHERE question=%s""", (table_question,))

        # selectData = "SELECT topic,tfidf FROM insert_question_topic WHERE question= '" + str(table_question) + "'"
        # getHighest="select max(tfidf) FROM insert_question_topic WHERE question= '" + str(table_question) + "' "

        selectData = "SELECT topic,tfidf,tfidf_with_log FROM insert_question WHERE question= '" + str(table_question) + "'"
        getHighest = "select max(tfidf) FROM insert_question WHERE question= '" + str(table_question) + "' "

        ###########################2017-11-25################################
        # getHighestLog = "select max(tfidf_with_log) FROM insert_question WHERE question= '" + str(table_question) + "' and tfidf_with_log < 0 "
        getHigestLog="SELECT DISTINCT tfidf_with_log FROM insert_question where question= '" + str(table_question) + "' order by tfidf_with_log limit 1;"
        getMaxLog = DBHandler().getData(getHigestLog)
        print getMaxLog

        b_Log = [str(text[0]) for text in getMaxLog]
        print '-->',b_Log
        print 'b_log', b_Log[0]


        ###########################2017-11-25################################

        getMax = DBHandler().getData(getHighest)
        print getMax

        b = [str(text[0]) for text in getMax]
        print '-->',b
        print '>>', b[0]


        print selectData
        wup_list = DBHandler().getData(selectData)

        print wup_list[0]

        ########################################################
        # print wup_list[0]     means topic and tfidf
        #print wup_list[0][0]     means topic only
        # print wup_list[0][1]     means idf only
        #########################################################


        rows = len(wup_list)
        columns = len(wup_list[0])
        i = 0
        j = 0
        self.tableWidget.clearContents()
        for i in range(0, rows):
            for j in range(0, columns):
                item = QtGui.QTableWidgetItem((str(wup_list[i][j])))
                print str(wup_list[i][1])
                if(str(wup_list[i][1])==str(b[0])):
                    brush=QtGui.QBrush(QtGui.QColor(154,232,80))
                    brush.setStyle(QtCore.Qt.SolidPattern)
                    item.setBackground(brush)

                # if (str(wup_list[i][2]) == str(b_Log[0])):
                #     if(b_Log[0]==0):
                #         break
                #     else:
                #         brush = QtGui.QBrush(QtGui.QColor(255, 153, 153))
                #         brush.setStyle(QtCore.Qt.SolidPattern)
                #         item.setBackground(brush)

                self.tableWidget.setItem(i, j, item)

        print '>>>',wup_list[0][1]
        print 'b_log',b_Log[0]



app = QtGui.QApplication(sys.argv)
ex = LoadQuestion()
# ex.show()
# ex.exec_()







