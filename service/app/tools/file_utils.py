import os

def create_unique_filename(directory_path, filename):
    '''
    Creates a unique filename by appending an integer index to the file until
    no file with such a name exists.


    Args:
        directory_path: the directory path.
        filename: the intended name of the file.
    Returns:
        a unique filename which is not yet used in the directory specified
        by the directory_path.
    '''
    possible_abs_filename = os.path.join(directory_path, filename)
    if not os.path.isfile(possible_abs_filename):
        return filename
    else:
        filename_prefix, suffix = filename, ""
        if '.' in filename:
            filename_prefix, suffix = filename.rsplit('.', 1)
            suffix = ".{0}".format(suffix)
        return _create_unique_filename(directory_path, filename_prefix, suffix)


def _create_unique_filename(directory_path, filename_prefix, suffix, index=1):
    filename = "{0}({1}){2}".format(filename_prefix, str(index), suffix)
    possible_abs_filename = os.path.join(directory_path, filename)
    if not os.path.isfile(possible_abs_filename):
        return filename
    else:
        return _create_unique_filename(directory_path, filename_prefix, suffix,
                                       index + 1)
