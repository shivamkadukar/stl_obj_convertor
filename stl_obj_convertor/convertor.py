from src.obj_to_stl import run_obj_to_stl
from src.stl_to_obj import run_stl_to_obj

from src.file import file_to_read


def main():
    if file_to_read.endswith(".stl"):
        print("Running .stl to .obj conversion")
        run_stl_to_obj.main()
        print("conversion completed")

    elif file_to_read.endswith(".obj"):
        print("Running .obj to .stl conversion")
        run_obj_to_stl.main()
        print("Conversion completed")
        
    else:
        print("Invalid File Address")

main()

