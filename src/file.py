file_to_convert = input("Enter file address: ")  #E:\cctech\data\new.obj
file_to_save = input("Save converted file as: ") #E:\cctech\data\new_cube.stl

def python_readable_file_address(file_location):
    '''
    Replaces the back slash in file location with a forward slash

    Parameters
    ----------
    file_location -> location of a file(file_to_convert, file_to_save)

    Returns
    -------
    py_readable_location -> location of file with slash replaced.
    '''
    py_readable_location =  file_location.replace('\\','/')
    return py_readable_location

file_to_read = python_readable_file_address(file_to_convert)
file_to_write = python_readable_file_address(file_to_save)


