import unittest

from src.obj_to_stl.obj_reader import ObjReader
from src.obj_to_stl.obj_stl_convertor import ObjFaces, ObjVertexConvertor
from src.obj_to_stl.normal_vertex import Vertex 
from src.obj_to_stl.normal_vertex import Normal
from src.obj_to_stl.stl_writer import StlWriter

test_read = 'test\\test_data\\cube.obj'
test_write = 'test\\test_data\\result.stl'


write_file = open(test_write, 'r+')

def main():
    reader = ObjReader()
    stores_faces = ObjFaces()
    vertex_convertor = ObjVertexConvertor()
    writer = StlWriter()
    vertices = Vertex()
    normals = Normal()

    with open(test_read,'r') as file:
        for line in file:
            line = line.strip()
            reader.search_vertices(line)
            reader.search_faces(line)

    vertices.store_vertices(reader.searched_vertices)

    stores_faces.replace_space_with_slash(reader.searched_faces)

    vertex_convertor.store_vertices(stores_faces.face_list_with_texture,stores_faces.face_list_no_texture)
    vertex_convertor.store_vertex_index()

    normals.calculate_normals(vertices.all_vertices,vertex_convertor.vertex_index)

    normals.convert_calculated_normals_to_string()

    writer.write(write_file,normals.normal_strings,vertex_convertor.vertex_index,reader.searched_vertices)

main()

written_file_content = open(test_write,'r').read()

expected_written_content = open('test\\test_data\\expected.stl', 'r').read()


class TestStlWriter(unittest.TestCase):
    def test_the_written_file_is_not_empty(self):
        self.assertNotEqual(len(written_file_content),0)

    def test_the_writer_writes_the_file_correctly(self):
        self.assertEqual(written_file_content, expected_written_content)
