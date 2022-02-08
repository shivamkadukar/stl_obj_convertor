import unittest

from src.obj_to_stl.obj_reader import ObjReader
from src.obj_to_stl.obj_stl_convertor import ObjFaces, ObjNormalConvertor, ObjVertexConvertor
from src.obj_to_stl.stl_writer import StlWriter

test_read = 'E:\\cctech\\stl_obj_convertor\\test\\test_data\\cube.obj'
test_write = 'E:\\cctech\\stl_obj_convertor\\test\\test_data\\result.stl'


write_file = open(test_write, 'r+')

def main():
    
    reader = ObjReader()
    stores_faces = ObjFaces()
    vertex_convertor = ObjVertexConvertor()
    normal_convertor = ObjNormalConvertor()
    writer = StlWriter()

    with open(test_read,'r') as file:
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

main()

written_file_content = open(test_write,'r').read()

expected_written_content = open('E:\\cctech\\stl_obj_convertor\\test\\test_data\\expected.stl', 'r').read()

class TestStlWriter(unittest.TestCase):
    def test_the_written_file_is_not_empty(self):
        self.assertNotEqual(len(written_file_content),0)

    def test_the_writer_writes_the_file_correctly(self):
        self.assertEqual(written_file_content, expected_written_content)
