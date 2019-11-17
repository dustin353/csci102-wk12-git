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
    
