import os
import pickle
import re


# check to see if the file exists, then load  the file, else return the empty dictionary
def load():
    """ load student information from file"""
    info = {}
    if os.path.exists("student.txt"):
        with open("student.txt", "rb") as input_char:
            info = pickle.load(input_char)
            print("initial load ",info)

    return info


def save():
    """ save all student info to file"""
    with open("student.txt", "wb") as output:
        pickle.dump(student_info, output)
        print("picke success")


student_info = load() # load student infomations from a file
#print("student info is ",student_info)
user_cond = True  # it will return false when q is selected

while user_cond:  # program will run until q is selected

    student_first = ""
    student_last = ""
    student_id = 0

    # print user choice to pick
    print("\nPlease enter \"a\" to ADD a student")
    print("Please enter \"d\" to remove a student")
    print("Please enter \"p\" to print student list")
    print("Please enter \"q\" to exit\n")
    user_input = input(">>>")  # user input

    if user_input == "a":  # add student information
        isValid = True  # Return  False all inputs are valid

        while isValid:  # all the information entered is correct
            check_first = True  # return false when first name is entered correctly
            check_last = True  # return false when last name is entered correctly
            check_id = True  # return false when id is entered correctly

            while check_first:
                first = input("Please enter first name :")
                # strip while splace and call RE and strip multiple whitesace if any
                first = re.sub(' +', ' ', first.strip())

                if not first.isnumeric():# this check the string contains number - allow to have space btw two name
                    student_first = first
                    check_first = False
                else:
                    print("invalid first name \n")

            while check_last:
                last = input("Please enter last name :")

                # strip whitesplace and call RE and strip multiple whitesace if any
                last = re.sub(' +', ' ', last.strip())
                if not last.isnumeric():
                    student_last = last
                    check_last = False
                else:
                    print("invalid last name\n")

            while check_id:
                tmp = input("Please enter student ID :")
                tmp = tmp.strip()  # remove any space
                if tmp.isnumeric():
                    tmp=int(tmp) #save id as integer
                    #print(tmp)
                    # check to see if the student ID exist-NO DUPLICATE ID allows
                    if tmp not in student_info:
                        student_id = tmp
                        check_id = False
                        isValid = False
                    else:
                        print("Student ID you entered already exists, please choose another ID number\n")
                else:
                    print("Invalid id, please enter ID\n")

            student_info[student_id] = (student_first, student_last)  # save student information

    elif user_input == "d":  # remove the student
        isValid = True  # return false when information is deleted from dictionary
        while isValid:
            remove_id = input("Please enter student ID :")

            if remove_id.isnumeric():
                remove_id = int(remove_id)
                if remove_id in student_info:
                    del student_info[remove_id]      # check to see the keyword exists and valid number
                    isValid = False
                    print("student removed\n")
                else:
                    print("student id you entered does not exists, please enter valid number\n")
            else:
                print("invalid id number, please enter student id\n")

    elif user_input == "p":
        print("print function",student_info)  # print student information
    elif user_input == "q":
        user_cond = False
        save()
    else:
        print("Please enter a valid option\n")

print(student_info)
print("Good bye")
