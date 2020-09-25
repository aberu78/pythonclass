import pickle
import re
import os


class Student:
    def __init__(self, num_id, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = num_id
        self.grades = {}

    def add_grade(self, sub, score):
        if sub in self.grades:
            self.grades[sub].append(score)
        else:
            self.grades[sub] = [score]
        print("grade is added", self.grades)

    def print_student(self):
        print("print_student , ID: %s , Name: %s %s " % (self.id, self.first_name, self.last_name))

    def print_grade(self):
        for sub in self.grades:
            print("print_grade ", sub, self.grades[sub])

    def __str__(self):
        return self.last_name + ", " + self.first_name

    def __repr__(self):
        return self.__str__()


# check to see if the file exists, then load  the file, else return the empty dictionary
def load():
    """ load student information from file"""
    info = {}
    if os.path.exists("student_test.txt"):
        with open("student_test.txt", "rb") as input_char:
            info = pickle.load(input_char)
            print("initial load ", info)
    return info


def save():
    """ save all student info to file"""
    with open("student.txt", "wb") as output:
        pickle.dump(student_info, output)
        print("pickle success")


def add_student(student_num,fname, lname):
    tmp_student = Student(student_num, fname, lname)
    return tmp_student


student_info = load()  # load student information from a file
user_cond = True  # it will return false when q is selected

while user_cond:  # program will run until q is selected

    # print user choice to pick
    print("\nPlease enter \"a\" to ADD a student")
    print("Please enter \"d\" to remove a student")
    print("Please enter \"p\" to print student list")
    print("Please enter \"g\" to print student list")
    print("Please enter \"q\" to exit\n")
    user_input = input(">>>")  # user input

    if user_input == "a":  # add student information
        isValid = True  # Return  False all inputs are valid

        while isValid:  # all the information entered is correct
            check_name = True
            check_id = True  # return false when id is entered correctly

            while check_name:
                first = input("Please enter first name :")
                last = input("Please enter last name :")

                if not first.isnumeric() and not last.isnumeric():
                    first = re.sub(' +', ' ', first.strip())
                    last = re.sub(' +', ' ', last.strip())
                    student_first = first
                    student_last = last
                    check_name = False
                else:
                    print("invalid names, please try again \n")

            while check_id:
                tmp = input("Please enter student ID :")
                tmp = tmp.strip()  # remove any space
                if tmp.isnumeric():
                    tmp = int(tmp)  # save id as integer
                    # check to see if the student ID exist-NO DUPLICATE ID allows
                    if tmp not in student_info:
                        student_id = tmp
                        check_id = False
                        isValid = False
                    else:
                        print("Student ID you entered already exists, please choose another ID number\n")
                else:
                    print("Invalid id, please enter ID\n")

            student_info[student_id] = add_student(student_id, student_first, student_last)  # save student information

    elif user_input == "d":  # remove the student
        isValid = True  # return false when information is deleted from dictionary
        while isValid:
            remove_id = input("Please enter student ID :")

            if remove_id.isnumeric():
                remove_id = int(remove_id)
                if remove_id in student_info:
                    del student_info[remove_id]  # check to see the keyword exists and valid number
                    isValid = False
                    print("student removed\n")
                else:
                    print("student id you entered does not exists, please enter valid number\n")
            else:
                print("invalid id number, please enter student id\n")
    elif user_input == "g":
        isValid = True  # return false when information is deleted from dictionary

        while isValid:
            add_id = input("Please enter student ID :")
            if add_id.isnumeric():
                add_id = int(add_id)
                if add_id in student_info:
                    subject = input("Please enter a Class Name")
                    grade = input("please enter a grade")
                    student_info[add_id].add_grade(subject, grade)
                    isValid = False
                    print("end of adding grade")
            else:
                print("ID you entered is invalid, try again")

    elif user_input == "p":
        print("print function", student_info)  # print student information
    elif user_input == "q":
        user_cond = False
        save()
    else:
        print("Please enter a valid option\n")

print(student_info)
print("Good bye")
