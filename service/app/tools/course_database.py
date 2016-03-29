#!/usr/bin/python3

from app.tools.course_scraper import scrape_courses
from config import FROM_SCHOOL_YEAR, TO_SCHOOL_YEAR, PROGRAM, PKL_STORAGE_FILE
from app.tools.errors import handle_error

import pickle
import time
import multiprocessing

class CourseDatabase(object):
    '''
    Container for storing saved courses
    '''
    def factory(from_pkl=False, from_scrape=False, from_year=FROM_SCHOOL_YEAR,
                to_year=TO_SCHOOL_YEAR, program=PROGRAM):
        if from_pkl:
            return CourseDatabase.load_from_pkl()
        elif from_scrape:
            return self.scrape(from_year=FROM_SCHOOL_YEAR,
                               to_year=TO_SCHOOL_YEAR, program=PROGRAM)
        return None

    def __init__(self, all_courses, last_update, from_year=FROM_SCHOOL_YEAR,
                 to_year=TO_SCHOOL_YEAR, program=PROGRAM):
        self.all_courses = all_courses
        self.last_update = last_update
        self.from_year = from_year
        self.to_year = to_year
        self.program = program
        self.available_specialisations = set()


    #def update_all_course_types(self):
    #    specialisation_sets = [course.specialisations for course in self.get_all_courses()]
    #    self.available_specialisations = self.specialisations.union(other_course.specialisations)

    def get_available_specialisations(self):
        return self.available_specialisations

    def get_all_courses(self):
        return self.all_courses

    def scrape(self, from_year=FROM_SCHOOL_YEAR,
               to_year=TO_SCHOOL_YEAR, program=PROGRAM):
        self.all_courses = scrape_courses(from_year, to_year, program)
        self.last_update = time.time()

    def load_from_pkl():
        try:
            with open(PKL_STORAGE_FILE, 'rb') as pkl_file:
                return pickle.load(pkl_file)
        except IOError:
            handle_error("Could not access or find stored data in: '{0}'"
                .format(PKL_STORAGE_FILE))
            return None

    def save(self):
        with open(PKL_STORAGE_FILE, 'wb') as pkl_file:
            # Pickle dictionary using protocol 0.
            pickle.dump(self, pkl_file)

    def __str__(self):
        return "from year: {0}, to year: {1}, last update {2}, {3} courses:\
            \n{4}".format(
            self.from_year, self.to_year, self.last_update, len(self.all_courses),
                self.all_courses)

if __name__ == '__main__':
    course_database = CourseDatabase.factory(from_pkl=True, from_scrape=True,
        from_year=FROM_SCHOOL_YEAR, to_year=TO_SCHOOL_YEAR)
    print(course_database)
