from src.obj_to_stl.obj_reader import ObjReader
from src.obj_to_stl.normal_vertex import Vertex, Normal
from src.obj_to_stl.obj_stl_convertor import ObjFaces, ObjVertexConvertor
from src.obj_to_stl.stl_writer import StlWriter

from src.file import file_to_read, file_to_write


def main():
    write_file = open(file_to_write,'w')
    reader = ObjReader()
    stores_faces = ObjFaces()
    vertex_convertor = ObjVertexConvertor()
    writer = StlWriter()
    vertices = Vertex()
    normals = Normal()

    with open(file_to_read,'r') as file:
        for line in file:
            line = line.strip()
            reader.search_vertices(line)
            reader.search_faces(line)

    vertices.store_vertices(reader.searched_vertices)

    stores_faces.replace_space_with_slash(reader.searched_faces)

    vertex_convertor.store_vertices(stores_faces.face_list_with_texture, stores_faces.face_list_no_texture)
    vertex_convertor.store_vertex_index()

    normals.calculate_normals(vertices.all_vertices, vertex_convertor.vertex_index)

    normals.convert_calculated_normals_to_string()

    writer.write(write_file,
                normals.normal_strings,
                vertex_convertor.vertex_index,
                reader.searched_vertices)


