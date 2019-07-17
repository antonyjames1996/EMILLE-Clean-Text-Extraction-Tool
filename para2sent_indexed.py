#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from array import * 
import sys,os

arr1 = [line.rstrip('\n').split() for line in open(sys.argv[1])]
#print(arr1) #testing

para_count = 1
sent_count = 0
sent_list = []
final_sent = []


for i in range(0,len(arr1)):
    if arr1[i][len(arr1[i])-1] != '।' and arr1[i][len(arr1[i])-1] != '?' :
        arr1[i].append('।')

for i in range(0,len(arr1)):
    for j in range(0,len(arr1[i])):
        if arr1[i][j] != '।' and arr1[i][j] != '?' :
            s1 = str(arr1[i][j])
            sent_list.append(s1)
            #print(arr1[i][j], end =" ")
        if arr1[i][j] == '।' or arr1[i][j] == '?' :
            sent_count+=1
            sent_list.append(str(arr1[i][j]))
            final_sent = sent_list
            sent_list = []
        if arr1[i][j-1] == '।' or arr1[i][j-1] == '?' :
            if (len(final_sent)!= 0):
                print(os.path.basename(sys.argv[1]).strip(".txt") + "-" + "p" + str(para_count) + "-" + "s" + str(sent_count) + "\t", end = "")
                print(*final_sent, sep = " ")
    print(os.path.basename(sys.argv[1]).strip(".txt") + "-" + "p" + str(para_count) + "-" + "s" + str(sent_count)+ "\t", end = "")
    print(*final_sent, sep = " ")
    final_sent=[]
    #print(sent_count)
    sent_count = 0
    para_count+=1
    print("")

#print (para_count) 

