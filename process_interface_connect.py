import tfidf_storing

__author__ = 'ASUS'
import sys
import MySQLdb
from PyQt4.QtGui import *

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

from PyQt4 import QtCore
from PyQt4 import QtGui
from DB_Handling import DBHandler
import process_subject_content

db = MySQLdb.connect('localhost', 'root', '', 'new_pyproject')
cursor = db.cursor()

cursorNew = db.cursor(MySQLdb.cursors.DictCursor)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

com_text=''
class Process_topics(QDialog, process_subject_content.Ui_Dialog_process):
    selectvalue = ""

    def __init__(self):
        super(Process_topics, self).__init__()

        self.setupUi(self)

        sql_student_year_retrival = "SELECT DISTINCT student_year FROM student_year_table"
        retriveYear = DBHandler().getData(sql_student_year_retrival)

        b = [str(text[0]) for text in retriveYear]

        for stu_year in b:
            self.comboBox_year.addItem(stu_year)

        self.comboBox_year.activated.connect(self.handleActivated_year)  # use to get combobox value
        self.comboBox_semester.activated.connect(self.handleActivated_semester)  # use to get combobox value
        self.cmb_select_process.activated.connect(self.handleActivated_subject)  # use to get combobox value
        self.tableWidget.cellClicked.connect(self.editTopic)
        self.pushButton_update_topic.clicked.connect(self.updateTopic)
        self.pushButton_update_content.clicked.connect(self.convert_pdf_and_updateContent)
        self.pushButton_delete.clicked.connect(self.deleteTopicWithContent)
        self.btn_process.clicked.connect(self.saveProcess)

    def handleActivated_year(self, index):

        global com_text_year
        self.comboBox_semester.clear()
        self.cmb_select_process.clear()
        com_text_year = self.comboBox_year.itemText(index)
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

        # sql_subject_retrival = "SELECT subject_name FROM add_subject WHERE student_year='" + str(
        #     com_text_year) + "' and semester='" + str(com_text_sem) + "'"
        # retriveSubject = DBHandler().getData(sql_subject_retrival)

        sql_subject_retrival = "SELECT DISTINCT subject_name FROM subject_topic_with_content WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "'"
        retriveSubject = DBHandler().getData(sql_subject_retrival)

        b_sub = [str(text[0]) for text in retriveSubject]

        for subject in b_sub:
            # print subject["subject_name"]
            self.cmb_select_process.addItem(subject)

    def handleActivated_subject(self, index):
        global com_text_sub
        com_text_sub = self.cmb_select_process.itemText(index)
        print com_text_sub
        self.tableWidget.clearContents()

        selectData = "SELECT topic FROM subject_topic_with_content WHERE student_year='" + str(
            com_text_year) + "' and semester='" + str(com_text_sem) + "' and subject_name='" + str(com_text_sub) + "' "

        wup_list = DBHandler().getData(selectData)
        print 'wup List: ', wup_list

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
        self.tableWidget.clearContents()
        for i in range(0, rows):
            for j in range(0, columns):
                item = QtGui.QTableWidgetItem((str(wup_list[i][j])))

                self.tableWidget.setItem(i, j, item)

    def editTopic(self,row,column):
        try:
            print("Row %d and Column %d was clicked" % (row, column))
            item = self.tableWidget.itemAt(row, column)
            items = self.tableWidget.selectedItems()
            selectvalue = str(items[0].text())
            print(str(items[0].text()))

            self.lineEdit_topic.clear()
            self.lineEdit_topic.setText(str(items[0].text()))

        except IndexError:
            self.lineEdit_topic.clear()
            QtGui.QMessageBox.information(self, '', "You should have select a topic")

            gotdata = 'null'

    def updateTopic(self):
        update_question = self.lineEdit_topic.text()
        print 'UP >> ', update_question

        if update_question == "":
            print 'null'
            QtGui.QMessageBox.information(self, '', "You have to select a topic")
        else:
            print 'has vaalue'

            quit_msg = "Are you sure you want to update ? "
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                try:
                    items = self.tableWidget.selectedItems()
                    print'>>>>>', (str(items[0].text()))

                    update_question = self.lineEdit_topic.text()
                    print 'UP >> ', update_question

                    updateData = "update subject_topic_with_content set topic='" + str(update_question) + "' where topic='" + str(items[0].text()) + "'"
                    DBHandler().setData(updateData)

                    self.tableWidget.clearContents()

                    selectData = "SELECT topic FROM subject_topic_with_content WHERE student_year='" + str(
                        com_text_year) + "' and semester='" + str(com_text_sem) + "' and subject_name='" + str(
                        com_text_sub) + "' "

                    wup_list = DBHandler().getData(selectData)
                    print 'wup List: ', wup_list

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
                    self.tableWidget.clearContents()
                    for i in range(0, rows):
                        for j in range(0, columns):
                            item = QtGui.QTableWidgetItem((str(wup_list[i][j])))

                            self.tableWidget.setItem(i, j, item)


                    QtGui.QMessageBox.information(self, '', "Topic updated successfully")

                except IndexError:
                    QtGui.QMessageBox.information(self, '', "You have to select a topic")
                    gotdata = 'null'

    def convert_pdf_and_updateContent(self):
        update_question = self.lineEdit_topic.text()
        print 'UP >> ', update_question

        if update_question == "":
            print 'null'
            QtGui.QMessageBox.information(self, '', "You have to select a topic")
        else:
            print 'has vaalue'

            items = self.tableWidget.selectedItems()
            print'>>>>>', (str(items[0].text()))

            update_topic = self.lineEdit_topic.text()
            print 'UP >> ', update_topic

            if (update_topic == (str(items[0].text()))):

                quit_msg = "Are you sure you want to update ? "
                reply = QtGui.QMessageBox.question(self, 'Message',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:

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
                    # contnt = [text]
                    # print contnt
                    # print text
                    output.close()

                    updateData = "update subject_topic_with_content set content='" + str(text) + "' where topic='" + str(items[0].text()) + "'"

                    DBHandler().setData(updateData)

                    QtGui.QMessageBox.information(self, '', "Content updated successfully..!!")

            else:
                    QtGui.QMessageBox.information(self, '', "There is no content for this topic..!!")


    def deleteTopicWithContent(self):
        try:
            items = self.tableWidget.selectedItems()
            selectvalue = str(items[0].text())
            # print(str(items[0].text()))

            quit_msg = "Are you sure you want to delete topic with content ? "
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                items = self.tableWidget.selectedItems()
                print'items>> del ', (str(items[0].text()))

                delete_data_insert = "delete from subject_topic_with_content where topic='" + str(items[0].text()) + "'"
                DBHandler().setData(delete_data_insert)

                self.tableWidget.clearContents()

                selectData = "SELECT topic FROM subject_topic_with_content WHERE student_year='" + str(
                    com_text_year) + "' and semester='" + str(com_text_sem) + "' and subject_name='" + str(
                    com_text_sub) + "' "

                wup_list = DBHandler().getData(selectData)
                print 'wup List: ', wup_list

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
                self.tableWidget.clearContents()
                for i in range(0, rows):
                    for j in range(0, columns):
                        item = QtGui.QTableWidgetItem((str(wup_list[i][j])))

                        self.tableWidget.setItem(i, j, item)

                self.lineEdit_topic.clear()
                QtGui.QMessageBox.information(self, '', "Topic with content deleted successfully")

        except IndexError:
            QtGui.QMessageBox.information(self, '', "You have to select a topic")
            gotdata = 'null'

    def saveProcess(self):
        # print com_text_year,'>>'
        # print com_text_sem, '>>'
        # print com_text_sub, '>>'

        delete_data_insert = "delete from process_word_tfidf where subject_name='" + str(
            com_text_sub) + "' and student_year='" + str(com_text_year) + "' and semester='" + str(com_text_sem) + "'"

        DBHandler().setData(delete_data_insert)
        # QtGui.QMessageBox.information(self, '', "deleted successfully")

        tfidf_storing.GnerateTfIDF().proceddDataAccordingTosubject(com_text_sub,com_text_year,com_text_sem)
        QtGui.QMessageBox.information(self, '', "inserted successfully")




app = QtGui.QApplication(sys.argv)
ex = Process_topics()
# ex.show()
# ex.exec_()







