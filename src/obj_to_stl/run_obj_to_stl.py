from src.obj_to_stl.obj_reader import ObjReader
from src.obj_to_stl.obj_stl_convertor import ObjFaces, ObjNormalConvertor, ObjVertexConvertor
from src.obj_to_stl.stl_writer import StlWriter

from src.file import file_to_read, file_to_write

def main():
    write_file = open(file_to_write,'w')
    reader = ObjReader()
    stores_faces = ObjFaces()
    vertex_convertor = ObjVertexConvertor()
    normal_convertor = ObjNormalConvertor()
    writer = StlWriter()

    with open(file_to_read,'r') as file:
        for line in file:
            line = line.strip()
            reader.search_vertices(line)
            reader.search_normals(line)
            reader.search_faces(line)

    stores_faces.replace_space_with_slash(reader.searched_faces)
    stores_faces.faces_data()

    vertex_convertor.store_vertex_index(stores_faces.face_data)

    normal_convertor.store_normal_index(stores_faces.face_data)

    writer.write(write_file, 
                normal_convertor.normal_index,
                reader.searched_normals,
                vertex_convertor.vertex_index,
                reader.searched_vertices)


    




