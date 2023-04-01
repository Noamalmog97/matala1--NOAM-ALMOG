#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:21:21 2023

@author: noam
"""

#Q1
def my_func(x1,x2,x3):
    try:
        if x1+x2+x3 == 0:
            print("not a number-denominator equals zero")
        if type(x1)!=float or type(x2)!=float or type(x3) != float:
            print("Error:parameters should be float") 
        else:
            return float(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))
    except:
        return ("None")
#my_func("noam",2.5,6.4) 

#Q2
textfile =open('/Users/noam/Desktop/לימודים/שנה ג/סמסטר ב/פייתון/מטלות להגשה/text.txt')

dic=dict()
def revword(str1:str):
    str1=str1[::-1]
    return str1.lower()

def countword(textfile):
    for i in textfile:
        line=i.split(" ")
        if len(line)==1:
            word=line[0].lower().strip()
            dic[word]=1
        else:
            for n in line:
                word1=revword(i).strip()
                if word1==word:
                    dic[word]=dic.get(word,0)+1
    print (dic[word])
            

countword(textfile)       
        

