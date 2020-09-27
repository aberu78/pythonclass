import pickle
import re
import os


class Student:

    def __init__(self, num_id, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = num_id
        self.__grades = {}

    def add_grade(self, subject, grade):
        if subject in self.__grades:
            self.__grades[subject].append(grade)
        else:
            self.__grades[subject] = [grade]
        print("a grade is added")

    def grade_exist(self):
        if len(self.__grades.keys()) > 0:
            return True
        else:
            return False

    def print_student(self):
        print("ID: %s ; Name: %s %s " % (self.__id, self.__first_name, self.__last_name))

    def print_grades(self):
        print("Entering print_grades()")
        if self.grade_exist():
            for sub in self.__grades:
                    print("ID: %i Subject: %s grades: %s " % (self.__id, sub, self.__grades[sub]))
        else:
            print("No grades entered for this student")

    def print_avg(self):
        print("Entering print_avg() ")
        if self.grade_exist():
            avg = 0.0
            for subject in self.__grades:
                    avg = sum(self.__grades[subject]) / len(self.__grades[subject])
                    print("%s average is %i" % (subject, avg))
        else:
            print("No grades entered for this student ID")


    def __str__(self):
        return "ID: %i  %s %s " % (self.__id, self.__last_name, self.__first_name)

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
            add_id = input("Please enter student ID :")
            if add_id.isnumeric():
                add_id = int(add_id)
                print("inside loop")
                if add_id in student_info:
                    subject = input("Class Name ?")
                    grade = input("Grade ?")
                    student_info[add_id].add_grade(subject, int(grade))
                    isValid = False
            else:
                print("Invalid ID, try again")

    elif user_input == "p":

        print("Please enter 1 to print all student Names")
        print("Please enter 2 to all grades and average\n")
        option = input("<<<<<<< ")
        option = option.strip()

        if int(option) == 1:
            for student_id in student_info:
                student_info[student_id].print_student()  # print student information
        elif int(option) == 2:
            student_id = input("Student ID ?")
            if int(student_id) in student_info:
                student_info[int(student_id)].print_grades()
                student_info[int(student_id)].print_avg()
            else:
                print("invalid student id, try again")
        else:
            print("Invalid option error")

    elif user_input == "q":
        user_cond = False
        save()
    else:
        print("Invalid option, try again\n")

print(student_info)
print("Good bye")
