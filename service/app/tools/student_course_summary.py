#!/usr/bin/python3

from config import WEIGHTED_GRADES

from collections import defaultdict

class SpecialisationProgress(object):
    '''
    Represents the progress for a specialisation
    '''
    def __init__(self, specialisation_name):
        self.specialisation_name = specialisation_name
        self.total_points = 0
        self.A_points = 0
        self.A_courses = []
        self.regular_courses = []

    def add_course(self, course):
        self.total_points += course.get_points()
        if course.get_level() == 'A':
            self.A_points += course.get_points()
            self.A_courses.append(course)
        else:
            self.regular_courses.append(course)

    def get_regular_courses(self):
        return self.regular_courses

    def get_A_courses(self):
        return self.A_courses

    def get_total_points(self):
        return self.total_points

    def get_A_points(self):
        return self.A_points

    def __eq__(self, other):
        return self.specialisation_name == other.specialisation_name

    def __hash__(self):
        return hash(self.specialisation_name)

    def __str__(self):
        specialisation_summary_str = "{0}\n\nPOINTS:{1}\nA POINTS:{2}\nRegular COURSES:{3}\n\nA COURSES:{4}".format(self.specialisation_name, self.total_points, self.A_points, self.regular_courses, self.A_courses)
        return specialisation_summary_str

class StudentCourseSummary(object):
    '''
    Student course summary
    '''

    def __init__(self, finished_courses=[], unfinished_courses=[],
        grade_list=[], courses_data=None):
        self.finished_courses = finished_courses
        self.unfinished_courses = unfinished_courses
        self.grade_list = grade_list
        self.courses_data = courses_data
        self.finished_points = self.calc_finished_points()
        self.finished_A_points = self.calc_finished_A_points()
        self.unfinished_points = self.calc_unfinished_points()
        self.average_grade = self.calc_average_grade()
        self.specialisation_progress = self.calc_specialisation_progress()


    def __str__(self):
        header_str = "\n\n\n******COURSE SUMMARY******\n\n"
        average_grade_str = "AVERAGE GRADE: {0:.3f}\n".format(self.average_grade)
        general_summary_str = "_____FINISHED_____\nPOINTS:{0}\nA POINTS:{1}\n courses: {2} --- \n_____UNFINISHED_____\nPOINTS:{3}\n courses: {4} ---\n".format(
            self.finished_points,self.finished_A_points, self.finished_courses, self.unfinished_points, self.unfinished_courses)
        #specialisation_summary_str = "____SPECIALISATIONS____\n{0}".format(
        #    "\n".join([self.specialisation_progress.items()]))
        return "\n".join([header_str, average_grade_str, general_summary_str]) #, specialisation_summary_str])

    def calc_finished_points(self):
        return sum([course.get_points() for course in self.finished_courses])

    def calc_finished_A_points(self):
        return sum([course.get_points() for course in self.finished_courses if course.is_level('A')])

    def calc_unfinished_points(self):
        return sum([course.get_points() for course in self.unfinished_courses])

    def calc_average_grade(self):
        weighted_points = 0
        grade_sum = 0
        for (grade, points) in self.grade_list:
            if grade in WEIGHTED_GRADES:
                weighted_points += points
                grade_sum += points * WEIGHTED_GRADES[grade]
        if weighted_points:
            return grade_sum / weighted_points
        else:
            return 0
    def calc_specialisation_progress(self):
        #specialisation_progress = defaultdict(lambda: [0, 0, list(), list()])
        specialisation_progress = defaultdict(lambda : SpecialisationProgress("hii"))
        for course in self.finished_courses:
            for specialisation in course.get_specialisations():
                if specialisation not in specialisation_progress:
                    specialisation_progress[specialisation] = SpecialisationProgress(specialisation)
                specialisation_progress[specialisation].add_course(course)
        return specialisation_progress
