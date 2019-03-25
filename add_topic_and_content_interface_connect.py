

__author__ = 'ASUS'


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


import sys
import MySQLdb
import numpy as np
from PyQt4.QtGui import *


from PyQt4 import QtCore
from PyQt4 import QtGui
import add_topic_with_content
from DB_Handling import DBHandler

# db = MySQLdb.connect('localhost', 'root', '', 'new_pyproject')
# cursor = db.cursor()
#
# cursorNew = db.cursor(MySQLdb.cursors.DictCursor)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s



com_text_sem=''
com_text_year=''
com_text_sub=''
class AddNewTopicAndContent(QDialog, add_topic_with_content.Ui_Dialog_add_topic_content):
    selectvalue = ""

    def __init__(self):
        super(AddNewTopicAndContent, self).__init__()

        self.setupUi(self)

        sql_student_year_retrival = "SELECT DISTINCT student_year FROM student_year_table"
        retriveYear = DBHandler().getData(sql_student_year_retrival)

        b = [str(text[0]) for text in retriveYear]

        for stu_year in b:
            self.comboBox_year.addItem(stu_year)

        self.comboBox_year.activated.connect(self.handleActivated_year)  # use to get combobox value
        self.comboBox_semester.activated.connect(self.handleActivated_semester)  # use to get combobox value
        self.cmb_select_subject.activated.connect(self.handleActivated_subject)  # use to get combobox value
        self.btn_add_content.clicked.connect(self.convert_pdf_and_save)


    def handleActivated_year(self, index):

        global com_text_year
        self.comboBox_semester.clear()

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
        self.cmb_select_subject.clear()

        sql_subject_retrival = "SELECT subject_name FROM add_subject WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "'"
        retriveSubject = DBHandler().getData(sql_subject_retrival)

        b_sub = [str(text[0]) for text in retriveSubject]

        for subject in b_sub:
            self.cmb_select_subject.addItem(subject)

    def handleActivated_subject(self,index):
        global com_text_sub
        com_text_sub = self.cmb_select_subject.itemText(index)
        print ""
        print ""
        print com_text_year
        print com_text_sem
        print com_text_sub

        sql_topic_retrival = "SELECT topic FROM subject_topic_with_content WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and subject_name='" + str(com_text_sub) + "'"
        retriveTopic = DBHandler().getData(sql_topic_retrival)

        b_top = [str(text[0]) for text in retriveTopic]

        for topic in b_top:
            self.listWidget.addItem(topic)


    def convert_pdf_and_save(self):
        print com_text_year,'>>'
        print com_text_sem, '>>'
        print com_text_sub, '>>'

        topic = self.lineEdit_add_topic.text()
        print topic

        fname = QtGui.QFileDialog.getOpenFileName(None, 'Open file',
                                                  'c:\\', "Image files (*.pdf )", )

        pages = None
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)

        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        infile = file(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        contnt= text.replace("'", " ")
        contnt1=contnt.replace("\n"," ")
        contnt2=contnt1.replace(","," ")
        print contnt2
        # print text
        output.close()

        insertsql = "insert into subject_topic_with_content(student_year,semester,subject_name,topic,content)values('" + str(
            com_text_year) + "','" + str(com_text_sem) + "','" + str(com_text_sub) + "','" + str(topic) + "','" + str(contnt2) + "')"

        DBHandler().setData(insertsql)

        self.listWidget.clear()

        sql_topic_retrival = "SELECT topic FROM subject_topic_with_content WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and subject_name='"+str(com_text_sub)+"'"
        retriveTopic = DBHandler().getData(sql_topic_retrival)

        b_top = [str(text[0]) for text in retriveTopic]

        for topic in b_top:
            self.listWidget.addItem(topic)


        QtGui.QMessageBox.question(None, 'Extract!', 'Topic, subject and content are inserted successfully.!!',
                                   QtGui.QMessageBox.Ok | QMessageBox.Cancel)


        # cursorNew.execute("SELECT content FROM subject_topic_with_content WHERE content=%s", (contnt,))
        #
        # results = cursorNew.fetchone()
        # print results

        # if (results == None):
        #     cursorNew.execute("insert into subject_topic_with_content(student_year,semester,subject_name,topic,content) values(%s,%s,%s,%s,%s)",(com_text_year,com_text_sem,com_text_sub,topic,text,))
        #     db.commit()
        #     print text
        #
        #     self.listWidget.addItem(topic)
        #     QtGui.QMessageBox.question(None, 'Extract!', 'Topic, subject and content are inserted successfully.!!',
        #                                QtGui.QMessageBox.Ok | QMessageBox.Cancel)
        # else:
        #     QtGui.QMessageBox.question(None, 'Extract!', 'Content is already inserted...!!',
        #                                QtGui.QMessageBox.Ok | QMessageBox.Cancel)


app = QtGui.QApplication(sys.argv)
ex = AddNewTopicAndContent()
# ex.show()
# ex.exec_()







