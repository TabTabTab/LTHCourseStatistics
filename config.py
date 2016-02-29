import os

PKL_STORAGE_FILE = 'courses_data.pkl'

FROM_SCHOOL_YEAR = 10
TO_SCHOOL_YEAR = 16

PROGRAM = 'D'

COURSE_BASE_URL = "http://kurser.lth.se/lot/?lasar={0}&sort1=lp&sort2=slut_lp&sort3=namn&prog={1}&forenk=t&val=program"

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

TEMO_FILE_BASENAME = os.path.join(BASE_DIR, "temp", "temp_pdf")

#do not write space here
REMOVABLE_CHARACTERS = '-'
