class Course(object):
    '''
    Represents a course
    '''
    def __init__(self, code, points, level, initial_course_type=None):
        self.course_code = code
        self.points = points
        self.level = level
        self.course_types = set([initial_course_type]) if initial_course_type else set()

    def __str__(self):
        return "course code: {0}, points: {1}, level {2}, types: {3}".format(
            self.course_code, self.points, self.level, self.course_types)

    def __repr__(self):
        return "{0}\n".format(self.__str__())

    def get_course_code(self):
        return self.course_code

    def merge_course_info(self, other_course):
        '''
        Merges the information from the other course too the current course
        This currently only concerns the course types
        '''
        self.course_types = self.course_types.union(other_course.course_types)
