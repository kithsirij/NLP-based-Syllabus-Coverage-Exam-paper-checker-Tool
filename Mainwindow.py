# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui

import user_login_interface_connect
import add_subject_interface_connect
import add_topic_and_content_interface_connect
import process_interface_connect
import insert_question_interface_connect
import update_delete_interface_connect
import update_best_document_interface_connect
import best_document_all_question_interface_connect



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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1078, 600)
        MainWindow.setIconSize(QtCore.QSize(35, 25))

        # MainWindow.setStyleSheet(
        #     " background-image:url(SE_syllabus/videoblocks-two-feathers-down-moving-slowly-in-a-soft-light-decorative-blue-animation-for-background-or-illustration_rbxjcaiwz_thumbnail-full01.png)")

        # MainWindow.setStyleSheet(
        #     " background-image:url(SE_syllabus/jpgDARRGAXk0V.jpg)")



        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuLogin = QtGui.QMenu(self.menubar)
        self.menuLogin.setObjectName(_fromUtf8("menuLogin"))
        self.menuADD_SUBJECT = QtGui.QMenu(self.menubar)
        self.menuADD_SUBJECT.setObjectName(_fromUtf8("menuADD_SUBJECT"))
        self.menuADD_CONTENT = QtGui.QMenu(self.menubar)
        self.menuADD_CONTENT.setObjectName(_fromUtf8("menuADD_CONTENT"))
        self.menuPROCESS = QtGui.QMenu(self.menubar)
        self.menuPROCESS.setObjectName(_fromUtf8("menuPROCESS"))
        self.menuINSERT_QUESTION = QtGui.QMenu(self.menubar)
        self.menuINSERT_QUESTION.setObjectName(_fromUtf8("menuINSERT_QUESTION"))
        self.menuUPDATE_OR_DELETE_QUESTION = QtGui.QMenu(self.menubar)
        self.menuUPDATE_OR_DELETE_QUESTION.setObjectName(_fromUtf8("menuUPDATE_OR_DELETE_QUESTION"))
        self.menuBEST_DOCUMENT = QtGui.QMenu(self.menubar)
        self.menuBEST_DOCUMENT.setObjectName(_fromUtf8("menuBEST_DOCUMENT"))
        self.menuBEST_DOCUMENT_FOR_QUESTION_PAPER = QtGui.QMenu(self.menubar)
        self.menuBEST_DOCUMENT_FOR_QUESTION_PAPER.setObjectName(_fromUtf8("menuBEST_DOCUMENT_FOR_QUESTION_PAPER"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(60, 60))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionLogin = QtGui.QAction(MainWindow)

        self.actionLogin.triggered.connect(self.userLoging)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/Login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogin.setIcon(icon)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))

        self.actionAddsubject = QtGui.QAction(MainWindow)


        self.actionAddsubject.triggered.connect(self.addSubjects)
        self.actionAddsubject.setDisabled(True)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/books_add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddsubject.setIcon(icon1)
        self.actionAddsubject.setObjectName(_fromUtf8("actionAddsubject"))
        self.actionAddcontent = QtGui.QAction(MainWindow)

        self.actionAddcontent.triggered.connect(self.addContent)
        self.actionAddcontent.setDisabled(True)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/rodentia-icons_document-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddcontent.setIcon(icon2)
        self.actionAddcontent.setObjectName(_fromUtf8("actionAddcontent"))
        self.actionProcess = QtGui.QAction(MainWindow)

        self.actionProcess.triggered.connect(self.process)
        self.actionProcess.setDisabled(True)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/14d42564.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProcess.setIcon(icon3)
        self.actionProcess.setObjectName(_fromUtf8("actionProcess"))
        self.actionInsertquestion = QtGui.QAction(MainWindow)

        self.actionInsertquestion.triggered.connect(self.insertQuestion)
        self.actionInsertquestion.setDisabled(True)

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/003050-document-task-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsertquestion.setIcon(icon4)
        self.actionInsertquestion.setObjectName(_fromUtf8("actionInsertquestion"))
        self.actionUpdateordeletequestion = QtGui.QAction(MainWindow)

        self.actionUpdateordeletequestion.triggered.connect(self.questionUpdateDelete)
        self.actionUpdateordeletequestion.setDisabled(True)

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/magnifying-glass-97588_640.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdateordeletequestion.setIcon(icon5)
        self.actionUpdateordeletequestion.setObjectName(_fromUtf8("actionUpdateordeletequestion"))
        self.actionBestdocument = QtGui.QAction(MainWindow)

        self.actionBestdocument.triggered.connect(self.singleBestDoc)
        self.actionBestdocument.setDisabled(True)

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/report.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBestdocument.setIcon(icon6)
        self.actionBestdocument.setObjectName(_fromUtf8("actionBestdocument"))
        self.actionBsetdocumntsfod_questionpaper = QtGui.QAction(MainWindow)

        self.actionBsetdocumntsfod_questionpaper.triggered.connect(self.AllbestDoc)
        self.actionBsetdocumntsfod_questionpaper.setDisabled(True)

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("SE_syllabus/1600 (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBsetdocumntsfod_questionpaper.setIcon(icon7)
        self.actionBsetdocumntsfod_questionpaper.setObjectName(_fromUtf8("actionBsetdocumntsfod_questionpaper"))
        self.menuLogin.addSeparator()
        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuADD_SUBJECT.menuAction())
        self.menubar.addAction(self.menuADD_CONTENT.menuAction())
        self.menubar.addAction(self.menuPROCESS.menuAction())
        self.menubar.addAction(self.menuINSERT_QUESTION.menuAction())
        self.menubar.addAction(self.menuUPDATE_OR_DELETE_QUESTION.menuAction())
        self.menubar.addAction(self.menuBEST_DOCUMENT.menuAction())
        self.menubar.addAction(self.menuBEST_DOCUMENT_FOR_QUESTION_PAPER.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLogin)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAddsubject)
        self.toolBar.addAction(self.actionAddcontent)
        self.toolBar.addAction(self.actionProcess)
        self.toolBar.addAction(self.actionInsertquestion)
        self.toolBar.addAction(self.actionUpdateordeletequestion)
        self.toolBar.addAction(self.actionBestdocument)
        self.toolBar.addAction(self.actionBsetdocumntsfod_questionpaper)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuLogin.setTitle(_translate("MainWindow", "LOGIN", None))
        self.menuADD_SUBJECT.setTitle(_translate("MainWindow", "  ADD SUBJECT", None))
        self.menuADD_CONTENT.setTitle(_translate("MainWindow", "ADD CONTENT", None))
        self.menuPROCESS.setTitle(_translate("MainWindow", "PROCESS", None))
        self.menuINSERT_QUESTION.setTitle(_translate("MainWindow", "INSERT QUESTION", None))
        self.menuUPDATE_OR_DELETE_QUESTION.setTitle(_translate("MainWindow", "UPDATE OR DELETE QUESTION", None))
        self.menuBEST_DOCUMENT.setTitle(_translate("MainWindow", "BEST DOCUMENT FOR SINGLE QUESTION", None))
        self.menuBEST_DOCUMENT_FOR_QUESTION_PAPER.setTitle(_translate("MainWindow", "BEST DOCUMENT FOR QUESTION PAPER", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionLogin.setText(_translate("MainWindow", "login", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionAddsubject.setText(_translate("MainWindow", "addsubject", None))
        self.actionAddcontent.setText(_translate("MainWindow", "addcontent", None))
        self.actionProcess.setText(_translate("MainWindow", "process", None))
        self.actionInsertquestion.setText(_translate("MainWindow", "insertquestion", None))
        self.actionUpdateordeletequestion.setText(_translate("MainWindow", "updateordeletequestion", None))
        self.actionBestdocument.setText(_translate("MainWindow", "bestdocument", None))
        self.actionBsetdocumntsfod_questionpaper.setText(_translate("MainWindow", "bsetdocumntsfod questionpaper", None))

    def userLoging(self):
        ex = user_login_interface_connect.userLogin()

        ex.show()
        ex.exec_()


        tru = user_login_interface_connect.myTrueFalseVar
        print tru
        self.actionAddsubject.setEnabled(bool(tru))
        self.actionAddcontent.setEnabled(bool(tru))
        self.actionProcess.setEnabled(bool(tru))
        self.actionInsertquestion.setEnabled(bool(tru))
        self.actionUpdateordeletequestion.setEnabled(bool(tru))
        self.actionBestdocument.setEnabled(bool(tru))
        self.actionBsetdocumntsfod_questionpaper.setEnabled(bool(tru))




    def addSubjects(self):
        ex = add_subject_interface_connect.Addnewsubject()
        ex.show()
        ex.exec_()


    def addContent(self):
        ex = add_topic_and_content_interface_connect.AddNewTopicAndContent()
        ex.show()
        ex.exec_()

    def process(self):
        ex = process_interface_connect.Process_topics()
        ex.show()
        ex.exec_()

    def insertQuestion(self):
        ex = insert_question_interface_connect.InsertQuestion()
        ex.show()
        ex.exec_()

    def questionUpdateDelete(self):
        ex = update_delete_interface_connect.LoadQuestion()
        ex.show()
        ex.exec_()

    def singleBestDoc(self):
        ex = update_best_document_interface_connect.LoadQuestion()
        ex.show()
        ex.exec_()

    def AllbestDoc(self):
        ex = best_document_all_question_interface_connect.LoadQuestion2()
        ex.show()
        ex.exec_()

    def successLogin(self):
        print "suceess"
        self.actionAddcontent.setDisabled(False)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

