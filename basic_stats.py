# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/2/2024
# Description: Write a class called Student that has two private data members - the student's name and grade.
import statistics

class Student:
        """
        A class to represent the object of a Student with a private name and grade.

        Attributes:
            __name (str): The student's name
            __grade (float): The student's grade (assigned as a float to allow for places after decimal)
        """

        def __init__(self, name: str, grade: float):
            """
            Initializes a Student object with the provided name and grade.

            :param name: Student name
                   grade: Student grade
            """
            self.__name = name  # Private data member for name of student
            self.__grade = grade  # Private data member for grade of student

        def get_grade(self) -> float:  # Defines a function to retrieve the student's grade
            """
            Returns the grade of the student
            :return: grade (float)
            """
            return self.__grade

def basic_stats(students: list) -> tuple:
        """
        Returns the mean, median and mode of the grades of the list of students as basic_stats
        :param students:
        :return: mean, median and mode of grades from listed students as a tuple
        """
        grades = [student.get_grade() for student in
                  students]  # Retrieves the grade from each student in students[] and creates a list called grades[]

        # Calc the mean, median & mode
        mean = statistics.mean(grades)
        median = statistics.median(grades)
        mode = statistics.mode(grades)

        return mean, median, mode  # Returns as a tuple

# # Sample list of students & grades to run statistics
# s1 = Student("Mason", 84)
# s2 = Student("Ashton", 100)
# s3 = Student("Taylor", 78)
# s4 = Student("Tabitha", 90)
#
# student_list = [s1, s2, s3, s4]  # Assembles the student objects into a list, student_list[]
# print(basic_stats(student_list))  # Processes student_list[] thru basic_stats() function and prints the tuple result