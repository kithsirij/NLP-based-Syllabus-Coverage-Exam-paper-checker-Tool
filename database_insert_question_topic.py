import MySQLdb
import nltk
import string
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import *
from PyQt4 import QtGui
from PyQt4.QtGui import *
import math
import operator


db = MySQLdb.connect('localhost', 'root', '', 'new_pyproject')
cursor = db.cursor()

cursorNew = db.cursor(MySQLdb.cursors.DictCursor)

input_arr = {}
# input_count = 0

max_tf_idf = 0
max_topic = ''
tfidf_count = 0
tfidf_count1 = 0
tfidf_count2 = 0


class GenerateBestDocument:
    def get_tokens(self, word):
        # print 'word --',word
        input_count=0

        newv = str(word)
        # remove nonalpha numeric words
        regex = re.compile('[^a-zA-Z,\.!?]')
        nonalpha = regex.sub(' ', newv)

        lowers = nonalpha.lower()
        # remove the punctuation using the character deletion step of translate
        no_punctuation = lowers.translate(None, string.punctuation)
        # tokenize the words
        tokens = nltk.word_tokenize(no_punctuation)
        # filtered the words
        filtered = [w for w in tokens if not w in stopwords.words('english')];

        No_words_in_doc = len(filtered)

        print 'Number of words in a document: ', No_words_in_doc
        # input_arr[input_count]=filtered
        # print input_count,'-->',input_arr[input_count]
        print '------', filtered
        input_arr.clear()
        for w in filtered:

            input_arr[input_count] = w
            print input_count,'-->',input_arr[input_count]
            input_count = input_count + 1

    def get_tfidf(self, subject,question,stu_year,semester,yearss):

        cursorNew.execute("""SELECT topic FROM subject_topic_with_content where subject_name=%s and student_year=%s and semester=%s""", (subject,stu_year,semester,))
        topics = cursorNew.fetchall()

        for singleTopic in topics:
            tfidf_count = 0
            tfidf_count1= 0
            tfidf_count2 = 0

            print '>>', singleTopic["topic"]
            print ''

            for arr in input_arr:
                print arr,'word////',input_arr[arr]
                cursorNew.execute("""SELECT word,tfidf,tf_idf_with_log,tf_idf_with_half FROM process_word_tfidf WHERE word=%s AND topic=%s""",(input_arr[arr], singleTopic["topic"]))
                data = cursorNew.fetchall()
                for freq in data:
                    print 'fr--', freq
                    print ''
                    print freq["word"]
                    tfidf = freq["tfidf"]
                    tfidf_log = freq["tf_idf_with_log"]
                    tfidf_half = freq["tf_idf_with_half"]
                    tfidf_count = tfidf_count + tfidf;
                    tfidf_count1 = tfidf_count1 + tfidf_log;
                    tfidf_count2 = tfidf_count2 + tfidf_half;
                    print freq["word"], '-->', tfidf_count, 'log-->', tfidf_count1, 'half-->', tfidf_count2
            print ">>>",tfidf_count,"log>>>",tfidf_count1,"half>>>",tfidf_count2


            cursorNew.execute("Insert into insert_question(years,student_year,semester,subject_name,topic,question,tfidf,tfidf_with_log,tfidf_with_half) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (yearss,stu_year,semester,subject,singleTopic["topic"],question,tfidf_count,tfidf_count1,tfidf_count2,))
            db.commit()
            ##########################2017-10-24##########################################

    def get_max_tfidf(self, subject,question,stu_year,semester,yearss):


        cursorNew.execute( """SELECT topic FROM subject_topic_with_content where subject_name=%s and student_year=%s and semester=%s""",(subject, stu_year, semester,))
        topics = cursorNew.fetchall()

        global max_tf_idf
        global max_topic
        max_topic = ''
        max_tf_idf = 0

        for singleTopic in topics:
            tfidf_count = 0



            print '>>', singleTopic["topic"]
            for arr in input_arr:

                cursorNew.execute("""SELECT word,tfidf FROM process_word_tfidf WHERE  word=%s AND topic=%s""",(input_arr[arr], singleTopic["topic"]))
                data = cursorNew.fetchall()
                for freq in data:
                    tfidf = freq["tfidf"]
                    tfidf_count = tfidf_count + tfidf;
                    print freq["word"], '-->', tfidf_count

                if max_tf_idf < tfidf_count:
                    max_tf_idf = tfidf_count
                    max_topic = singleTopic["topic"]

        print '\n\n'
        print question, '--', max_topic,max_tf_idf

        cursorNew.execute( "Insert into question_max_tfidf(years,subject_name,question,max_tfidf,student_year,semester,topic) values(%s,%s,%s,%s,%s,%s,%s)",
            (yearss,subject,question,max_tf_idf, stu_year, semester,max_topic,))
        db.commit()


    def subject_and_question(self, getsubject, getquestion,stu_year,semester,yearss):
        self.get_tokens(getquestion)
        self.get_tfidf(getsubject,getquestion,stu_year,semester,yearss)
        self.get_max_tfidf(getsubject, getquestion, stu_year, semester, yearss)



ex = GenerateBestDocument()










