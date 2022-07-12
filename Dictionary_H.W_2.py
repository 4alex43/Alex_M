import collections


def ex1():
    print("Ex1\n")
    # Ex1.1
    str1 = "rnklwefngjrehnpiregmwekrmwqpemqwklfnwepiorkqwenworiwed"
    list_key_value = collections.Counter(str1)

    list_key_value = dict(sorted(list_key_value.items()))

    for k, v in list_key_value.items():
        print(k, ":", v)

    # Ex1.2
    value_turn_to_key = {}
    for key, value in list_key_value.items():
        if value not in value_turn_to_key:
            value_turn_to_key[value] = [key]
        else:
            value_turn_to_key[value].append(key)
    print("The final dictionary", value_turn_to_key)


def ex2():
    print("Ex2\n")
    # Ex2.a
    list1 = [1, 1, 1, 2, 3, 4, 5, 1, 7, 3, 8, 9]
    list2 = [5, 8, 9]
    list3 = [1, 2, 3, 4, 7, 5, 8]
    list = {"list1": list1, "list2": list2, "list3": list3}

    def show_num_return(list):
        list_set = set(list)
        check_duplicates = len(list) != len(list_set)
        result = "In the list:" + str(list) + " values return more than once: "

        if check_duplicates:  # if have numbers returns
            list_key_value = collections.Counter(list)
            for k, v in list_key_value.items():
                if v > 1:
                    result += str(k) + " "
            return True, result
        else:
            return False

    # Ex2.b
    def check_common_values(all_list):
        lwnr = {}  # listWithNotReturn
        check_in_left_lists = []
        for key, value in all_list.items():
            if not show_num_return(value):
                lwnr[key] = value  # to save the numbers of lists and the lists
                check_in_left_lists += value  # add list to one list to check number returns
            else:
                print(show_num_return(value)[1])

        result = show_num_return(check_in_left_lists)

        if result:
            print(result[1].replace(str(check_in_left_lists), str(lwnr)))
        else:
            print([])

    check_common_values(list)


"""
Ex3
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


def ex3():
    print("Ex3\n")

    def check_num_str(list):

        order_by = input('What is order(asc/desc)? ')
        if order_by == "asc" or order_by == "ASC" or order_by == "desc" or order_by == "DESC":
            s = ''.join(str(x) for x in list)
            res_list = []
            res_list[:0] = s
            set_res = set(res_list)
            if order_by == "asc" or order_by == "ASC":
                result = sorted(set_res)
            if order_by == "desc" or order_by == "DESC":
                result = sorted(set_res, reverse=True)
            print(result)
        else:
            print("Error use only asc or desc!!!")
            checkNumStr(list)

    # For check
    list = [31, 99, 3, 1943]
    check_num_str(list)


def main():
    ex1()
    ex2()
    ex3()


if __name__ == "__main__":
    main()
