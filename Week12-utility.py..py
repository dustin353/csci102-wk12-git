# https://github.com/dustin353/csci102-wk12-git
# Dustin Choat
# CSCI 102 - Section B
# Week 11 - Part B

import string

#1. PrintOutput
def PrintOutput(put):
    print('OUTPUT', put)

#2. LoadFile
def LoadFile(filename):
    file = open(filename)
    contents = file.read()
    list1 = contents.split('\n')
    ''' Attempt to put list elements between double quotation marks
    x = 0
    string1 = ''
    for x in range(len(list1)):
        string1 = string1 + '"' + list1[x] + '"' + '-'
        x += 1
    print(string1)
    list2 = string1.split('-')
    print(list2)
    '''
    return list1

#3. UpdateString
def UpdateString(string1, string2, index):
    string3 = string1[:index] + string2 + string1[index+1:]
    PrintOutput(string3)

#4. FindWordCount
def FindWordCount(list1, string1):
    occurances = 0
    x = 0
    while x < len(list1):
        y = 0
        while y < len(list1[x]):
            string2 = list1[x]
            if string2[y:y+len(string1)] == string1:
                occurances += 1
            y += 1
        x += 1
    ''' Check if string only matches list element not in list element
    #for x in list1:
        #if x == string1:
            #occurances += 1
    '''
    return occurances

#5. ScoreFinder
def ScoreFinder(list1, list2, string1):
    x = 0
    spot = False
    while x < len(list1):
        if list1[x] == string1.title():
            spot = True
            player = list1[x]
            score = list2[x]
        elif list1[x] == string1.lower():
            spot = True
            player = list1[x]
            score = list2[x]
        x += 1
    if spot:
        output = player + ' got a score of ' + str(score)
        PrintOutput(output)
    else:
        PrintOutput('player not found')

#6. Union
def Union(list1, list2):
    x = 0
    list3 = []
    while x < len(list1):
        if list1[x] in list2:
            pass
        else:
            list3.append(list1[x])
        x += 1
    x = 0
    while x < len(list2):
        if list2[x] in list1:
            pass
        else:
            list3.append(list2[x])
        x += 1
    return list3

#7. Intersection
def Intersection(list1, list2):
    x = 0
    intersect = False
    list3 = []
    while x < len(list1):
        if list1[x] in list2:
            list3.append(list1[x])
            intersect = True
        x += 1
    if intersect:
        return list3
    else:
        return 'no intersection'

#8. NotIn
def NotIn(list1, list2):
    x = 0
    no_values = True
    list3 = []
    while x < len(list1):
        if list1[x] in list2:
            pass
        else:
            list3.append(list1[x])
            no_values = False
        x += 1
    if no_values:
        return 'no values'
    else:
        return list3
