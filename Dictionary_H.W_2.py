import collections
#Ex1.1

str = "rnklwefngjrehnpiregmwekrmwqpemqwklfnwepiorkqwenworiwed"
strSort=sorted(str)
listKeyValue = collections.Counter(str)

listKeyValue = dict(sorted(listKeyValue.items()))

for k, v in  listKeyValue.items():
    print(k, ":" ,v)

#Ex1.2
valueTurnToKey = {}
for key, value in listKeyValue.items():
    if value not in valueTurnToKey:
        valueTurnToKey[value] = [key]
    else:
        valueTurnToKey[value].append(key)
print("The final dictionary", valueTurnToKey)


#Ex2.a
list1 = [1,1,1,2,3,4,5,1,7,3,8,9]
list2 = [5,8,9]
list3 = [1,2,3,4,7,5,8]
list = {"list1" : list1,"list2" : list2, "list3" : list3}



def showNumReturn(list):
    listSet = set(list)
    checkDuplicates = len(list) != len(listSet)
    result = "In the list:" + str(list) + " values return more than once: "

    if checkDuplicates :# if have numbers returns
        listKeyValue = collections.Counter(list)
        for k, v in listKeyValue.items():
            if v > 1:
                result += str(k) + " "
        return True, result
    else:
        return False

def checkCommonValues(allList):
    lwnr = {} #listWithNotReturn
    checkInLeftLists = []
    for key, value in allList.items():
        if not showNumReturn(value):
            lwnr[key] = value #to save the numbers of lists and the lists
            checkInLeftLists += value#add list to one list to check number returns
        else:
            print(showNumReturn(value)[1])

    result = showNumReturn(checkInLeftLists)

    if result:
        print(result[1].replace(str(checkInLeftLists), str(lwnr)))
    else:
        print([])

checkCommonValues(list)

"""
Ex2.b
@author  Alex Mircea
@version 1.0
@since   26/06/22

get a list of numbers
Ask user asc or desc chack if user type only one of the options if not print error and try again
change list to string
change string to list each number in index
use set for remove duplicates numbers
print the answer
"""
def checkNumStr(list):

    orderBy = input('What is order(asc/desc)? ')
    if orderBy == "asc" or orderBy == "ASC" or orderBy == "desc" or orderBy == "DESC":
        s = ''.join(str(x) for x in list)
        resList = []
        resList[:0] = s
        setRes = set(resList)
        if orderBy =="asc" or orderBy == "ASC" :
            result = sorted(setRes)
        if orderBy =="desc" or orderBy == "DESC":
            result = sorted(setRes,reverse=True)
        print(result)
    else:
        print("Error use only asc or desc!!!")
        checkNumStr(list)

#For check
list=[31,99,3,1943]
checkNumStr(list)
