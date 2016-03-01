class Course(object):
    '''
    Represents a course
    '''
    def __init__(self, code, points, level, initial_specialisation=None):
        self.course_code = code
        self.points = points
        self.level = level
        self.specialisations = set([initial_specialisation]) if initial_specialisation else set()

    def __str__(self):
        return "course code: {0}, points: {1}, level {2}, types: {3}".format(
            self.course_code, self.points, self.level, self.get_specialisations())

    def __repr__(self):
        return "{0}\n".format(self.__str__())

    def get_course_code(self):
        return self.course_code

    def get_points(self):
        return self.points

    def get_level(self):
        return self.level

    def get_specialisations(self):
        return self.specialisations

    def merge_course_info(self, other_course):
        '''
        Merges the information from the other course too the current course
        This currently only concerns the course types
        '''
        self.specialisations = self.specialisations.union(other_course.specialisations)
