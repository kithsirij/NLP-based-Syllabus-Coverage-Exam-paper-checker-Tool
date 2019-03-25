
__author__ = 'ASUS'
import sys
import MySQLdb
import numpy as np
from PyQt4.QtGui import *


from PyQt4 import QtCore
from PyQt4 import QtGui
import nltk
import tagging
from nltk.corpus import wordnet
import string
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import *
import math
import tagging_noun_content

from nltk.stem import WordNetLemmatizer


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

question_arr = []
topic_arr=[]
content_arr=[]
class LoadQuestionTagging(QDialog, tagging.Ui_Dialog):
    selectvalue = ""

    def __init__(self):
        super(LoadQuestionTagging, self).__init__()

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
        self.cmb_select_process.activated.connect(self.handleActivated_question)  # use to get combobox value
        self.pushButton_similarity.clicked.connect(self.similarity)

    def handleActivated_yearss(self, index):
        global yearss
        yearss = self.comboBox_year.itemText(index)

    def handleActivated_year(self, index):
        global com_text_year
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
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

        sql_subject_retrival = "SELECT distinct subject_name FROM insert_question WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and years='" + str(yearss) + "'"
        retriveSubject = DBHandler().getData(sql_subject_retrival)

        b_sub = [str(text[0]) for text in retriveSubject]

        for subject in b_sub:
            # print subject["subject_name"]
            self.cmb_select_process.addItem(subject)


    def handleActivated_question(self, index):

        global com_text
        com_text = self.cmb_select_process.itemText(index)
        print yearss, com_text_year, com_text_sem,com_text

        # print com_text
        sql_question_retrival = "SELECT DISTINCT question FROM insert_question WHERE subject_name='" + str(
            com_text) + " ' and student_year='" + str(com_text_year) + "' and semester='" + str(com_text_sem) + "' and years='" + str(yearss) + "'"
        retriveQuestion = DBHandler().getData(sql_question_retrival)

        b = [str(text[0]) for text in retriveQuestion]
        for q_sion in b:
            question_arr.append(q_sion.lower())

        print 'question array',question_arr

        # tagging_noun_content.QuestionNounContent().subject_and_question(question_arr,com_text,yearss,com_text_year,com_text_sem)


        QtGui.QMessageBox.information(self, '', "topic inserted successfully")
        QtGui.QMessageBox.information(self, '', "wait for content..........")

        print '-----------------------------------------------------------------------------------------------------------------------'

        selectTopic = "SELECT topic FROM subject_topic_with_content WHERE subject_name='" + str(
            com_text) + "' and student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' "
        retriveTopic = DBHandler().getData(selectTopic)

        b_top = [str(text[0]) for text in retriveTopic]

        for topc in b_top:
            sql_content_retrival = "SELECT content FROM subject_topic_with_content WHERE subject_name='" + str(
                com_text) + " ' and student_year='" + str(
                com_text_year) + "' and semester='" + str(com_text_sem) + "' and topic='"+str(topc)+"'"
            retriveContent = DBHandler().getData(sql_content_retrival)
            b_content = [str(text[0]) for text in retriveContent]

            # tagging_noun_content.QuestionNounContent().extract_content_nouns(b_content, topc,com_text)

        QtGui.QMessageBox.information(self, '', "content inserted successfully")



    def similarity(self):

        # tagging_noun_content.QuestionNounContent().wordSynsetSimilarity(com_text)
        tagging_noun_content.QuestionNounContent().maxSimilarityTen(com_text)






app = QtGui.QApplication(sys.argv)
ex = LoadQuestionTagging()
ex.show()
ex.exec_()


