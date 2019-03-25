
__author__ = 'ASUS'
import sys
import MySQLdb
import numpy as np
from PyQt4.QtGui import *


from PyQt4 import QtCore
from PyQt4 import QtGui
import best_document_for_all_questions
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
class LoadQuestion2(QDialog, best_document_for_all_questions.Ui_Dialog_best_document):
    selectvalue = ""

    def __init__(self):
        super(LoadQuestion2, self).__init__()

        self.setupUi(self)

        sql_year_retrival = "SELECT DISTINCT years FROM insert_question"
        retriveYear = DBHandler().getData(sql_year_retrival)

        b1 = [str(text[0]) for text in retriveYear]

        for yearss in b1:
            self.comboBox_year_2.addItem(yearss)

        self.comboBox_year_2.activated.connect(self.handleActivated_yearss)  # use to get combobox value


        sql_student_year_retrival="SELECT DISTINCT student_year FROM student_year_table"
        retriveYear = DBHandler().getData(sql_student_year_retrival)

        b = [str(text[0]) for text in retriveYear]

        for stu_year in b:
            self.comboBox_year.addItem(stu_year)

        self.comboBox_year.activated.connect(self.handleActivated_year)  # use to get combobox value
        self.comboBox_semester.activated.connect(self.handleActivated_semester)  # use to get combobox value
        self.cmb_select_process.activated.connect(self.handleActivated_subject)  # use to get combobox value
        # self.pushButton_load.clicked.connect(self.loadData)

    def handleActivated_yearss(self,index):
        global yearss
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
        self.tableWidget.clearContents()
        self.tableWidget_2.clearContents()

        yearss=self.comboBox_year_2.itemText(index)


    def handleActivated_year(self, index):
        global com_text_year
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
        self.tableWidget_2.clearContents()
        self.tableWidget.clearContents()
        com_text_year = self.comboBox_year.itemText(index)
        print com_text_year

        sql_semester_retrival = "SELECT DISTINCT semester FROM student_year_table"
        retriveSemester = DBHandler().getData(sql_semester_retrival)

        b = [str(text[0]) for text in retriveSemester]

        for sem in b:
            self.comboBox_semester.addItem(sem)

    def handleActivated_semester(self, index):
        global com_text_sem
        com_text_sem = self.comboBox_semester.itemText(index)
        print com_text_sem
        self.cmb_select_process.clear()

        sql_subject_retrival = "SELECT DISTINCT subject_name FROM insert_question WHERE student_year='"+str(com_text_year)+"' and semester='"+str(com_text_sem)+"' and years='" + str(yearss) + "'"
        retriveSubject = DBHandler().getData(sql_subject_retrival)

        b_sub = [str(text[0]) for text in retriveSubject]

        for subject in b_sub:
            # print subject["subject_name"]
            self.cmb_select_process.addItem(subject)


    def handleActivated_subject(self,index):
        global com_text_sub
        self.tableWidget.clearContents()
        self.tableWidget_2.clearContents()

        com_text_sub=self.cmb_select_process.itemText(index)
        print yearss
        print com_text_year
        print com_text_sem
        print com_text_sub

        selectData = "SELECT question,max_tfidf,topic FROM question_max_tfidf WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and years='" + str(yearss) + "' and subject_name='" + str(com_text_sub) + "' "

        wup_list = DBHandler().getData(selectData)
        print 'wup List: ',wup_list

        # print wup_list[0]
        print '>>>>>', wup_list
        ########################################################
        # print wup_list[0]     means topic and tfidf
        # print wup_list[0][0]     means topic only
        # print wup_list[0][1]     means idf only
        #########################################################


        rows = len(wup_list)
        columns = len(wup_list[0])

        i = 0
        j = 0
        self.tableWidget_2.clearContents()
        for i in range(0, rows):
            for j in range(0, columns):
                item = QtGui.QTableWidgetItem((str(wup_list[i][j])))
                print str(wup_list[i][1])
                self.tableWidget_2.setItem(i, j, item)

        print '>>>', wup_list[0][1]


        delete_max_Topic = "delete from topic_with_question_count"
        DBHandler().setData(delete_max_Topic)

        select_count = "SELECT count(*) FROM question_max_tfidf WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and subject_name='" + str(
            com_text_sub) + "'and years='" + str(yearss) + "'"

        ques_count = DBHandler().getData(select_count)
        question_count = [str(text[0]) for text in ques_count]

        percentge=0
        for q_count in question_count:
            print 'ques_count',float(q_count)



            selectTopic = "SELECT topic FROM subject_topic_with_content WHERE student_year='" + str(
                com_text_year) + "' and semester='" + str(com_text_sem) + "' and subject_name='" + str(com_text_sub) + "' "

            wup_Topic = DBHandler().getData(selectTopic)
            # print 'Topic--> ',wup_Topic

            b_Topic = [str(text[0]) for text in wup_Topic]



            for topy in b_Topic:
                print 'topy',topy

                select_max_Topic = "SELECT topic FROM question_max_tfidf WHERE student_year='" + str(
                    com_text_year) + "' and semester='" + str(com_text_sem) + "' and subject_name='" + str(
                    com_text_sub) + "'and years='" + str(yearss) + "'"

                wup_Max_Topic = DBHandler().getData(select_max_Topic)
                # print 'Topic--> ', wup_Max_Topic

                b_max_Topic = [str(text[0]) for text in wup_Max_Topic]
                topy_count=0
                for topyc in b_max_Topic:
                    # print 'max topy', topyc
                    if(topy==topyc):
                        topy_count=topy_count+1


                print  '  -->count  ', topy_count
                percentge=(topy_count/float(q_count))*100
                print  '  -->percentage ', (topy_count/float(q_count))*100


                insertsql="insert into topic_with_question_count(topic,question_count,percentage)values('" + str(topy) + "','" + str(topy_count) + "','" + str(percentge) + "')"

                DBHandler().setData(insertsql)

            select_Topic = "SELECT topic,question_count,percentage FROM topic_with_question_count"
            Max_Topic = DBHandler().getData(select_Topic)
            print '>>', Max_Topic

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

            print '>>>', Max_Topic[0][1]


app = QtGui.QApplication(sys.argv)
ex = LoadQuestion2()
ex.show()
ex.exec_()







