"""
@author  Alex Mircea
@version 1.0
@since   17/06/22

Ex1
Create histogram list for list numbers (use a repetition (*) operator)
ToDoList
1.Create func with name histogramList that receives an array
2.build try&except for check the list with only a numbers
3.Create new list and fill it out with String included num of '*' same in index from list you got
"""
#for check
#mylist = [1,2,3,4,"g"]
#mylist = ["g"]

def histogramList(list):
    histo = []
    for value in list:
        try:
            histo.append(('*') * int(value))
        except ValueError:
            print("Find a variable is not int in the list")
            break

    return histo

#print(histogramList(mylist))

