#!/usr/bin/python2

from course_scraper import scrape_courses_data
from config import FROM_SCHOOL_YEAR, TO_SCHOOL_YEAR, PROGRAM, PKL_STORAGE_FILE

import pickle
import time
import multiprocessing

class CoursesData(object):
    '''
    Container for storing saved courses
    '''
    def __init__(self, from_pkl=False, from_scrape=False,
        from_year=FROM_SCHOOL_YEAR, to_year=TO_SCHOOL_YEAR, program=PROGRAM):
        self.courses_data = None
        self.last_update = None
        self.from_year = from_year
        self.to_year = to_year
        self.program = program
        self.available_specialisations = set()
        if from_pkl:
            self.load_from_pkl()
        elif from_scrape:
            self.scrape()

    def update_all_course_types(self):
        specialisation_sets = [course.specialisations for course in self.get_courses()]
        self.available_specialisations = self.specialisations.union(other_course.specialisations)

    def get_available_specialisations(self):
        return self.available_specialisations

    def get_courses(self):
        return self.courses_data

    def scrape(self):
        courses_data = scrape_courses_data(self.from_year, self.to_year, self.program)
        self.courses_data = courses_data
        self.last_update = time.time()

    def load_from_pkl(self):
        try:
            with open(PKL_STORAGE_FILE, 'rb') as pkl_file:
                stored_course_data = pickle.load(pkl_file)
                self.courses_data = stored_course_data.courses_data
                self.from_year = stored_course_data.from_year
                self.to_year = stored_course_data.to_year
                self.last_update = stored_course_data.last_update
                return self
        except IOError:
            handle_error("Could not access or find stored data in: '{0}'"
                .format(PKL_STORAGE_FILE))

    def save(self):
        with open(PKL_STORAGE_FILE, 'wb') as pkl_file:
            # Pickle dictionary using protocol 0.
            pickle.dump(self, pkl_file)

    def __str__(self):
        return "from year: {0}, to year: {1}, last update {2}, {3} courses:\
            \n{4}".format(
            self.from_year, self.to_year, self.last_update, len(self.courses_data),
                self.courses_data)

if __name__ == '__main__':
    courses_data = CoursesData(from_pkl=True, from_scrape=True,
        from_year=FROM_SCHOOL_YEAR, to_year=TO_SCHOOL_YEAR)
    courses_data.save()
    print(courses_data)
