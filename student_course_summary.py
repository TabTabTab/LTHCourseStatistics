#!/usr/bin/python2

from collections import defaultdict

class StudentCourseSummary(object):
    '''
    Student course summary
    '''
    def __init__(self, finished_courses=[], unfinished_courses=[],
        courses_data=None):
        self.finished_courses = finished_courses
        self.unfinished_courses = unfinished_courses
        self.courses_data = courses_data
        self.specialisation_progress = defaultdict(lambda: [0, 0, list(), list()])
        self.calc_specialisation_progress()

    def __str__(self):
        general_summary_str = "_____FINISHED_____\nPOINTS:{0}\nA POINTS:{1}\n courses: {2} --- \n_____UNFINISHED_____\nPOINTS:{3}\n courses: {4} ---\n".format(
            self.calc_finished_points(),self.calc_finished_A_points(), self.finished_courses, self.calc_unfinished_points(), self.unfinished_courses)
        specialisation_summary_str = "____SPECIALISATIONS____\n{0}".format(
            "\n".join(["--{0}--\nPOINTS:{1}\nA POINTS:{2}\nRegular COURSES:{3}\nA COURSES:{4}".
            format(s, p, ap, rc, ac) for s, [p, ap, rc, ac] in self.specialisation_progress.iteritems()]))
        return "\n".join([general_summary_str, specialisation_summary_str])

    def calc_finished_points(self):
        return sum([course.get_points() for course in self.finished_courses])

    def calc_finished_A_points(self):
        return sum([course.get_points() for course in self.finished_courses if course.get_level() == 'A'])

    def calc_unfinished_points(self):
        return sum([course.get_points() for course in self.unfinished_courses])

    def calc_specialisation_progress(self):
        for course in self.finished_courses:
            for specialisation in course.get_specialisations():
                self.specialisation_progress[specialisation][0] += course.get_points()
                if course.get_level() == 'A':
                    self.specialisation_progress[specialisation][1] += course.get_points()
                    self.specialisation_progress[specialisation][3].append(course)
                else:
                    self.specialisation_progress[specialisation][2].append(course)
