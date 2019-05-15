#! python3
# -*- coding: UTF-8 -*-



tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = max(len(item) for item in tableData[i])
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if j == 0:
                print(tableData[j][i].rjust(colWidths[j])+"  ",end="")
            else:
                print(tableData[j][i].ljust(colWidths[j])+"  ",end="")
        print('\n')
    
printTable(tableData)


