import tfidf_storing

__author__ = 'ASUS'
import sys
import MySQLdb
from PyQt4.QtGui import *



from PyQt4 import QtCore
from PyQt4 import QtGui
from DB_Handling import DBHandler
import Mainwindow
import user_login

db = MySQLdb.connect('localhost', 'root', '', 'new_pyproject')
cursor = db.cursor()

cursorNew = db.cursor(MySQLdb.cursors.DictCursor)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

myTrueFalseVar = ''

com_text=''
class userLogin(QDialog, user_login.Ui_Dialog_login):
    selectvalue = ""

    def __init__(self):
        super(userLogin, self).__init__()

        self.setupUi(self)

        self.pushButton_login.clicked.connect(self.loginWithPassword)




    def loginWithPassword(self):
        username = self.lineEdit_user_name.text()
        # print username

        pw = self.lineEdit_password.text()
        # print password


        user=cursorNew.execute("""SELECT user_name,password FROM userlogin where user_name=%s and password=%s""",(username,pw,))
        # user = cursorNew.fetchall()

        print 'user>>> ',user

        if(user==1):
            QtGui.QMessageBox.information(self, '', "Login success...!!")
            global myTrueFalseVar
            myTrueFalseVar=True
            QDialog.setVisible(self, False)



        elif(user==0):
            QtGui.QMessageBox.information(self, '', "Can't Login ...!!")





app = QtGui.QApplication(sys.argv)
ex = userLogin()

# ex.show()
# ex.exec_()
