from src.obj_geometry_finder import run_obj_geometry_finder

from src.file import file_to_read 


def main():
    if file_to_read.endswith('.obj'):
        run_obj_geometry_finder.main()

    elif file_to_read.endswith('.stl'):
        pass
        #run_stl_geometry_finder.main()

    else:
        print("Invalid file type")

main()