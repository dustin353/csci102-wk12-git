#
# Dustin Choat
# CSCI 102 - Section B
# Week 11 - Part B

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







