import sys

def handle_error(error_msg="An error occured", exit=True):
    print(error_msg)
    if exit:
        sys.exit(1)
