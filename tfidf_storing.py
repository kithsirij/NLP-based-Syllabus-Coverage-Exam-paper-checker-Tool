import MySQLdb
import nltk
import string
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import *
import math
from PyQt4.QtGui import *
from PyQt4 import QtGui

db = MySQLdb.connect('localhost', 'root', '', 'new_pyproject')
cursor = db.cursor()

cursorNew = db.cursor(MySQLdb.cursors.DictCursor)


one_array = {}
top_arr={}
tf_arr={}
words_array={}
lst = 0
tfcount = 0
tfcount1=0
tfcount2=0

idf_count=0
word_arr={}
idf_arr={}
subject_arr={}
stu_year_arr={}
semester_arr={}
no_of_document=0

top_arr1={}
tf_arr1={}
subject_arr1={}
words_array1={}
stu_year_arr1={}
semester_arr1={}


top_arr2={}
tf_arr2={}
subject_arr2={}
words_array2={}
stu_year_arr2={}
semester_arr2={}


class GnerateTfIDF:



    def termfrequency(self,filtered, No_words_in_doc, topic,subject,stu_year,semester):
        # print 'set word: ', set(filtered)
        global tfcount
        for word in set(filtered):
            # print 'word >>',word
            frequency = float(filtered.count(word)) / No_words_in_doc
            top_arr[tfcount] = topic
            tf_arr[tfcount] = frequency
            subject_arr[tfcount]=subject
            stu_year_arr[tfcount]=stu_year
            semester_arr[tfcount]=semester
            words_array[tfcount]=word
            # print 'count: ', tfcount
            # print stu_year,'>>',semester,'>>',subject,'-->',topic,'--->',word,'--->',frequency
            tfcount = tfcount +1
        # print '-------------------------------------------------------------'

    ##################2017-10-24##########################################

    def termfrequency_variation1(self,filtered, No_words_in_doc, topic,subject,stu_year,semester):
        # print 'set word: ', set(filtered)
        global tfcount1
        for word in set(filtered):
            # print 'word >>',word
            frequency =1+(math.log(float(filtered.count(word)) / No_words_in_doc))
            top_arr1[tfcount1] = topic
            tf_arr1[tfcount1] = frequency
            subject_arr1[tfcount1]=subject
            stu_year_arr1[tfcount] = stu_year
            semester_arr1[tfcount] = semester
            words_array1[tfcount1]=word
            # print 'count: ', tfcount1
            # print stu_year,'-->',semester,'>>',subject,'-->',topic,'--->',word,'--->',frequency
            tfcount1 = tfcount1 +1
        # print '-------------------------------------------------------------'

    def termfrequency_variation2(self, filtered, No_words_in_doc, topic, subject,stu_year,semester):
        # print 'set word: ', set(filtered)
        global tfcount2
        for word in set(filtered):
            # print 'word >>', word
            frequency = 0.5 +0.5 * (math.log(float(filtered.count(word)) / No_words_in_doc))
            top_arr2[tfcount2] = topic
            tf_arr2[tfcount2] = frequency
            subject_arr2[tfcount2] = subject
            stu_year_arr2[tfcount] = stu_year
            semester_arr2[tfcount] = semester
            words_array2[tfcount2] = word
            # print 'count: ', tfcount2
            # print stu_year,'>>',semester,'>>',subject, '-->', topic, '--->', word, '--->', frequency
            tfcount2= tfcount2 + 1
        # print '-------------------------------------------------------------'

    ######################################################################


    def get_tokens(self,word, topic,subject,stu_year,semester):
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
        # print 'fil>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.',filtered    #sampurna content eka tokens walata kadala array ekaka thiyan innwa
        one_array[lst] = filtered
        No_words_in_doc = len(filtered)

        # print 'Number of words in a document: ', No_words_in_doc
        self.termfrequency(filtered, No_words_in_doc,topic,subject,stu_year,semester)
        ##################2017-10-24##########################################

        self.termfrequency_variation1(filtered, No_words_in_doc,topic,subject,stu_year,semester)
        self.termfrequency_variation2(filtered, No_words_in_doc, topic, subject,stu_year,semester)

        ######################################################################


    def proceddDataAccordingTosubject(self,getsubject,stu_year,semester):

        cursorNew.execute("SELECT content FROM subject_topic_with_content where subject_name=%s and student_year=%s and semester=%s ", (getsubject,stu_year,semester,))
        retriveContent = cursorNew.fetchall()

        # cursorNew.execute("SELECT content FROM topic_content_last where subject_name=%s ", (getsubject,))
        # retriveContent = cursorNew.fetchall()

        all_row_content = [row for row in retriveContent]
        global no_of_document
        # print '.......',all_row_content, '\n'
        no_of_document=len(all_row_content)
        # print 'Number of documents: ', no_of_document, '\n'



        cursorNew.execute("SELECT topic FROM subject_topic_with_content where subject_name=%s and student_year=%s and semester=%s ", (getsubject,stu_year,semester,))
        retrivalTopic = cursorNew.fetchall()

        arr = {}

        i = 0
        for topyc in retrivalTopic:
            arr[i] = topyc["topic"]
            # print arr[i]
            # print  i,'>>',arr[i]       #topics display wenwa
            i += 1

        for row in all_row_content:
            global lst
            # print lst

            if lst < len(all_row_content):  # pawichchi karanwa , print x[0],print x[1],print x[2],print x[3] me code eka wenuwata
                row1 = all_row_content[lst]
                # print row1
                self.get_tokens(row1,arr[lst],getsubject,stu_year,semester)
                lst=lst+1

        self.idf(one_array, len(all_row_content))

        for cnt in idf_arr:
            # print stu_year_arr[cnt],semester_arr[cnt],'----->',subject_arr[cnt],'----->', top_arr[cnt], '---->', word_arr[cnt], '---->', tf_arr[cnt], '---->', idf_arr[cnt]
            # print stu_year_arr[cnt],semester_arr[cnt],'----->',subject_arr1[cnt],'----->',top_arr1[cnt],'---->',word_arr[cnt],'---->',tf_arr1[cnt],'---->', idf_arr[cnt]
            # print stu_year_arr[cnt],semester_arr[cnt],'----->',subject_arr2[cnt],'----->',top_arr2[cnt],'---->',word_arr[cnt],'---->',tf_arr2[cnt],'---->',idf_arr[cnt]
            tf_idf = tf_arr[cnt] * idf_arr[cnt]
            tf_idf1=tf_arr1[cnt] * idf_arr[cnt]
            tf_idf2 = tf_arr2[cnt] * idf_arr[cnt]
            print 'tf_idf  -->', tf_idf
            print 'tf_idf1  -->', tf_idf1
            print 'tf_idf2  -->', tf_idf2
            # print("--------------")
            # print top_arr[cnt]
            #cursor.execute("""Insert into try_table_tfidf(subject_name,topic,word,tf,idf,tfidf) values(%s,%s,%s,%s,%s,%s)""",(subject_arr[cnt],top_arr[cnt], word_arr[cnt], tf_arr[cnt], idf_arr[cnt], tf_idf))
            cursor.execute("""Insert into process_word_tfidf(subject_name,student_year,semester,topic,word,idf,tf,tfidf,tf_with_log,tf_idf_with_log,tf_with_half,tf_idf_with_half) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (subject_arr[cnt],stu_year_arr[cnt],semester_arr[cnt] ,top_arr[cnt], word_arr[cnt],idf_arr[cnt], tf_arr[cnt], tf_idf, tf_arr1[cnt], tf_idf1,tf_arr2[cnt],tf_idf2))
            db.commit()



    def go_idf(self,x,inverse_doc_freq):
        global idf_count
        word_arr[idf_count]=x
        idf_arr[idf_count]=inverse_doc_freq
        # print idf_count,' -->', word_arr[idf_count],idf_arr[idf_count]
        idf_count=idf_count+1


    def idf(self,one_array, No_of_doc):
        count = 0
        for key in one_array:

            # print 'key',key
            all = set(one_array[key])
            # print "all:",len(all)
            for x in all:
                # print "x:",x
                for index in one_array:

                    # print 'index ',index
                    word = set(one_array[index])
                    # print 'word',len(word)
                    for keyword in word:

                        if x == keyword:

                            # print "Matched>>\tx:", x, "\tkeyword:", keyword
                            count = count + 1
                            break
                        else:
                            # print "Mismatched>>\tx:", x, "\tkeyword:", keyword
                            continue



                inverseTermFrequency =1+(math.log(float(No_of_doc) / (count)))
                self.go_idf(x,inverseTermFrequency)
                count = 0




