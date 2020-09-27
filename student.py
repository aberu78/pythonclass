import pickle
import re
import os


class Student:

    def __init__(self, num_id, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = num_id
        self.__grades = {}

    def add_grade(self, sub, score):
        if sub in self.__grades:
            self.__grades[sub].append(score)
        else:
            self.__grades[sub] = [grade]

    def grade_exist(self):
        if len(self.__grades.keys()) > 0:
            return True
        else:
            return False

    def print_student(self):
        print("ID: %s ; Name: %s %s " % (self.__id, self.__first_name, self.__last_name))

    def print_grades(self):
        if self.grade_exist():
            for sub in self.__grades:
                print("ID: %i Subject: %s grades: %s " % (self.__id, sub, self.__grades[sub]))
        else:
            print("No grades entered for this student ID")

    def print_avg(self):
        if self.grade_exist():
            avg = 0.0
            for sub in self.__grades:
                avg = sum(self.__grades[sub]) / len(self.__grades[sub])
                print("%s average is %.1f " % (sub, avg))
        else:
            print("No grades entered for this student ID")

    def __str__(self):
        return "ID: %i  %s %s %s" % (self.__id, self.__last_name, self.__first_name, self.__grades)

    def __repr__(self):
        return self.__str__()


def add_student(student_num, fname, lname):
    tmp_student = Student(student_num, fname, lname)
    return tmp_student


def load():
    info = {}
    if os.path.exists("student_test3.txt"):
        with open("student_test3.txt", "rb") as input_char:
            info = pickle.load(input_char)
            print("initial load ", info)
    return info


def save():
    with open("student_test3.txt", "wb") as output:
        pickle.dump(student_info, output)
        print("pickle success")


def is_valid_id(num):
    if num.isdigit():
        if int(num) in student_info:
            return True
    else:
        return False


student_info = load()  # load student information from a file
user_cond = True  # it will return false when q is selected

while user_cond:  # program will run until q is selected

    # print user choice to pick
    print("\nPlease enter \"a\" to ADD a student")
    print("Please enter \"d\" to remove a student")
    print("Please enter \"p\" to print student list")
    print("Please enter \"g\" to print student list, grades,or grades")
    print("Please enter \"q\" to exit\n")
    user_input = input(">>>")  # user input

    if user_input == "a":  # add student information
        isValid = True  # Return  False all inputs are valid

        while isValid:  # all the information entered is correct
            check_name = True
            check_id = True  # return false when id is entered correctly

            while check_name:
                first = input("First name :")
                last = input("Last name :")

                if not first.isnumeric() and not last.isnumeric():
                    first = re.sub(' +', ' ', first.strip())
                    last = re.sub(' +', ' ', last.strip())
                    student_first = first
                    student_last = last
                    check_name = False
                else:
                    print("invalid names,try again \n")

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
                        print("Student ID already exists, please choose another ID number\n")
                else:
                    print("Invalid id, try again \n")

            student_info[student_id] = add_student(student_id, student_first, student_last)  # save student information

    elif user_input == "g":
        isValid = True  # return false when information is deleted from dictionary

        while isValid:
            student_id = input("Please enter student ID :")
            if is_valid_id(student_id):
                subject = input("Class Name ?")
                grade = input("Grade ?")
                student_info[int(student_id)].add_grade(subject, int(grade))
                print("a grade is added")
                isValid = False
            else:
                print("Invalid ID, try again")

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
        isValid = True  # return false when information is deleted from dictionary
        while isValid:
            print("Please enter 1 to print all student Names")
            print("Please enter 2 to all grades by a student ID")
            print("Please enter 3 to print the average grade by a student ID\n")
            option = input("<<<<<<< ")

            if option == "1":  # print all student list
                for student_id in student_info:
                    student_info[student_id].print_student()
                    isValid = False
            elif option == "2":  # print grades by student ID
                student_id = input("Student ID ?")
                if is_valid_id(student_id):
                    student_info[int(student_id)].print_grades()
                    isValid = False
                else:
                    print("Invalid student ID, try again\n")
            elif option == "3":  # print grade average by student ID
                student_id = input("Student ID ?")
                if is_valid_id(student_id):
                    student_info[int(student_id)].print_avg()
                    isValid = False
                else:
                    print("Invalid student ID, try again\n")
            else:
                print("Invalid. Enter 1,2,or 3, try again\n")

    elif user_input == "q":
        user_cond = False
        save()
    else:
        print("Invalid option, try again\n")

print(student_info)
print("Good bye")
