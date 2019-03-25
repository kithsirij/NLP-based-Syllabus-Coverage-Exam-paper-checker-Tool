
from nltk.corpus import wordnet


# A=['design','thing']
# B=['box','quality']
# cont=0
# cont1 = 0
# for A1 in A:
#     for B1 in B:
#         wordFromList1 = wordnet.synsets(A1,'n')
#         wordFromList2 = wordnet.synsets(B1,'n')
#         print 'wordFromList1',wordFromList1
#         print 'wordFromList2',wordFromList2
#
#         for listA in wordFromList1:
#             cont=cont+1
#             # print 'cont',cont
#
#             # list1_name = listA.name().partition('.')[0]
#             if(cont==1):
#                 print listA
#
#                 # continue
#                 for listB in wordFromList2:
#
#                     cont1=cont1+1
#                     print 'cont1',cont1
#                     if(cont1==1):
#                         print listB

# A=['design']
# B=['box']
#
# print wordFromList1

# for listA in A:
#     concatA= "Synsets('"+listA+".n.01')"
#     for listB in B:
#         concatB= "Synsets('" + listA + ".n.01')"
#         # print concatB
#         s = concatA.wup_similarity(concatB)
#         print s

# listA = wordFromList1[0].name().partition('.')[0]
############################ important ####################################
# x=wordnet.synsets('coupling')
# one_arr=[]
# for one_list in x:
#     if(one_list.name().partition('.')[0]=='coupling'):
#         # print one_list.name().partition('.')[0]
#         one_arr.append(one_list.name().partition('.')[0])
# print one_arr[0 ]
#################################################################

wordFromList1=wordnet.synsets('cohension')
wordFromList2=wordnet.synsets('coupling')

print 'list1 --> ',wordFromList1
print 'list2 --> ',wordFromList2

# listA=wordFromList1[0].name().partition('.')[0]
# print 'listA >>   ', listA
if wordFromList2 == [] or wordFromList1==[]:
    print 'empty'
else:
    listB = wordFromList2[0].name().partition('.')[0]
    print 'listB >>   ', listB
    s = wordFromList1[0].wup_similarity(wordFromList2[0])
    print s

# for list1 in x:
#     print 'list1 --> ', list1
#
# for list2 in y:
#         print 'list2 --> ',list2