from src.stl_to_obj.stl_reader import StlReader
from src.stl_to_obj.stl_obj_convertor import StlVertexConvertor, StlNormalConvertor
from src.stl_to_obj.obj_writer import ObjWriter

from src.file import file_to_read, file_to_write

def main():

    write_file = open(file_to_write,'w')
    
    reader = StlReader()
    vertex_convertor = StlVertexConvertor()
    normal_convertor = StlNormalConvertor()
    writer = ObjWriter()

    with open(file_to_read, 'r') as file:
        for line in file:
            reader.search_vertices(line)
            reader.search_normals(line)

    vertex_convertor.vertex_index(reader.searched_vertices)
    vertex_convertor.unique_vertex_index(reader.searched_vertices)

    normal_convertor.normal_index(reader.searched_normals)
    normal_convertor.unique_normal_index(reader.searched_normals)

    writer.write(
                write_file, 
                vertex_convertor.v_list, 
                normal_convertor.vn_list, 
                vertex_convertor.v_index, 
                normal_convertor.vn_index
                )

    write_file.close()








