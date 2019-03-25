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


from nltk.stem import WordNetLemmatizer

from nltk.corpus import wordnet
from DB_Handling import DBHandler
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




class QuestionNounContent:

    def searchVerbs11(self, getSentenses,getQuestion,com_text, yearss, com_text_year, com_text_sem):
        verbList = []
        isVB = False
        isNNP = False
        isWH = False

        for tagList in getSentenses:
            print 'question',getQuestion
            # print 'tag list: ', tagList
            for oneList in tagList:
                # print 'one list: ',[oneList][0][0],[oneList][0][1]

                if ([oneList][0][1].startswith('NNP') or [oneList][0][1].startswith('NN')):
                    # verbList.append([oneList][0][0].lower())
                    print 'verb list', [oneList][0][0]
                    Lemmatizer=WordNetLemmatizer()
                    noun_lemmatize=Lemmatizer.lemmatize([oneList][0][0])
                    print 'lemmatize ',noun_lemmatize

                    # insertsql = "insert into question_nouns(subject_name,years,student_year,semester,question,word_noun)values('" + str(com_text) + "','" + str(yearss)+ "','" + str(com_text_year) + "','" + str(com_text_sem)+ "','" + str(getQuestion)+ "','" + str(noun_lemmatize)+ "')"
                    # DBHandler().setData(insertsql)


    def extract_nouns(self,arr_question,com_text, yearss, com_text_year, com_text_sem):
        print 'arr question',arr_question
        for question in arr_question:

            sentenses = nltk.sent_tokenize(question)
            # print 'sentence',sentenses
            sentences = [nltk.word_tokenize(sent) for sent in sentenses]
            print 'word', sentences
            sentences = [nltk.pos_tag(sent) for sent in sentences]
            print 'POS',sentences
            verbList =self.searchVerbs11(sentences,question,com_text, yearss, com_text_year, com_text_sem)

    def subject_and_question(self, question_arr,com_text,yearss,com_text_year,com_text_sem):
         self.extract_nouns(question_arr,com_text,yearss,com_text_year,com_text_sem)

    def search_content_nouns11(self, contnt_sentence, topic, com_text):
        print '###############################', topic, '##########################################################'
        print '>>>>>>> ', contnt_sentence, '>>>>>>>>>>>>>>>>>'

        for oneList in contnt_sentence:
            if ([oneList][0][1].startswith('NNP') or [oneList][0][1].startswith('NN')):
                if (len([oneList][0][0]) == 3 and [oneList][0][0].startswith('x')):
                    continue;
                else:
                    if ([oneList][0][0].startswith('[') or [oneList][0][0].startswith(']') or len(
                            [oneList][0][0]) == 1):
                        continue;
                    else:
                        # print '>>', [oneList][0][0]
                        Lemmatizer = WordNetLemmatizer()
                        noun_lemmatize = Lemmatizer.lemmatize([oneList][0][0])

                        print [oneList][0][0], ' >> lemmatize >> ', noun_lemmatize

                        # insertsqlContent = "insert into content_noun(subject_name,topic,word_noun)values('" + str(
                        #     com_text) + "','" + str(topic) + "','" + str(noun_lemmatize) + "')"
                        # DBHandler().setData(insertsqlContent)


    def extract_content_nouns(self, content, b_topic, com_text):
        # print 'topic ', b_topic
        # print 'content ',content

        sentenses = nltk.sent_tokenize(str(content))

        sentences = [nltk.word_tokenize(sent) for sent in sentenses]
        print 'content sentence', sentences

        for one_list in sentences:
            print 'one sentence list', one_list
            list2 = []
            list3 = []
            list4 = []
            list2 = [el.replace('\\n', ' ') for el in one_list]
            # print 'list2',list2
            list3 = [el.replace('\\', ' ') for el in list2]
            list4 = [el.replace("'", " ") for el in list3]

            split_sentence = [words for segments in list4 for words in segments.split()]
            print '>> ', split_sentence
            sentences1 = nltk.pos_tag(split_sentence)
            print 'content POS', sentences1
            verbList = self.search_content_nouns11(sentences1,b_topic,com_text)

    def wordSynsetSimilarity(self,com_text):
        selectQuestion = "SELECT distinct question FROM question_nouns where subject_name='" + str(com_text) + "'"
        retriveQuestion = DBHandler().getData(selectQuestion)

        b_question = [str(text[0]) for text in retriveQuestion]
        print b_question
        for question in b_question:
            print question
            selectQuestionNoun = "select word_noun from question_nouns where subject_name='" + str(
                com_text) + "' and question='" + str(question) + "' "
            retriveQuestionNoun = DBHandler().getData(selectQuestionNoun)

            b_question_noun = [str(text[0]) for text in retriveQuestionNoun]
            print b_question_noun

            for q_noun in b_question_noun:

                selectTopic = "select distinct topic from content_noun where subject_name='" + str(com_text) + "'"
                retriveTopic = DBHandler().getData(selectTopic)

                b_topic = [str(text[0]) for text in retriveTopic]
                # print b_topic

                for Topic in b_topic:
                    selectContentNoun = "select word_noun from content_noun where subject_name='" + str(com_text) + "' and topic='" + str(Topic) + "'"
                    retriveContentNoun = DBHandler().getData(selectContentNoun)

                    b_content_noun = [str(text[0]) for text in retriveContentNoun]
                    set_content_noun = set(b_content_noun)
                    print 'set content /// > ', set_content_noun

                    for q_content in set_content_noun:

                        wordFromList1 = wordnet.synsets(q_noun)
                        wordFromList2 = wordnet.synsets(q_content)

                        if wordFromList2 == [] or wordFromList1 == []:
                            print wordFromList1
                            print wordFromList2
                            print 'empty'
                        else:
                            listA = wordFromList1[0].name().partition('.')[0]
                            # print 'listA >>   ', listA
                            listB = wordFromList2[0].name().partition('.')[0]
                            # print 'listB >>   ',listB
                            s = wordFromList1[0].wup_similarity(wordFromList2[0])
                            if s != None:
                                print listA, ' >> ', listB, ' >> ', s
                                # insertsqlSimilarity = "insert into synset_similarity_between_question_content(subject_name,question,topic,question_noun,content_noun,similarity)values('" + str(
                                #             com_text) + "','" + str(question) + "','" + str(Topic) + "','" + str(listA) + "','" + str(listB) + "','" + str(s) + "')"
                                # DBHandler().setData(insertsqlSimilarity)

    def maxSimilarityTen(self,com_text):
        selectTopic = "SELECT distinct topic FROM synset_similarity_between_question_content where subject_name='" + str(com_text) + "'"
        retriveTopic = DBHandler().getData(selectTopic)

        b_topic = [str(text[0]) for text in retriveTopic]
        print '>>',b_topic

        for topic in b_topic:
            print 'topic>> ',topic
            selectQuestion = "SELECT distinct question FROM synset_similarity_between_question_content where subject_name='" + str(com_text) + "'"
            retriveQuestion = DBHandler().getData(selectQuestion)

            b_question = [str(text[0]) for text in retriveQuestion]
            print '>>', b_question
            for question in b_question:
                print 'question .. >',question

                selectMaxSimilarity = "SELECT similarity FROM synset_similarity_between_question_content where subject_name='" + str(
                    com_text) + "' and topic='" + str(topic) + "' and question='" + str(question) + "' order by similarity  desc limit 15"
                retriveMaxSimilarity = DBHandler().getData(selectMaxSimilarity)

                b_maxSimilarity = [str(text[0]) for text in retriveMaxSimilarity]
                count_simialrity = 0
                for max_similarity in b_maxSimilarity:
                    print 'max similarity >>',max_similarity
                    count_simialrity=count_simialrity+float(max_similarity)
                    print 'count similarity  >>   ',count_simialrity
                print 'count similarity                                      >>   ', count_simialrity
                insertsqlMaxSimilarity = "insert into max_similarity_table(subject_name,topic,question,max_similarity)values('" + str(
                            com_text) + "','" + str(topic) + "','" + str(question) + "','" + str(count_simialrity) + "')"
                DBHandler().setData(insertsqlMaxSimilarity)


ex = QuestionNounContent()