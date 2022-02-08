import unittest

from src.stl_to_obj.stl_reader import *
from src.stl_to_obj.stl_obj_convertor import *
from src.stl_to_obj.obj_writer import *

test_read = 'E:\\cctech\\stl_obj_convertor\\test\\test_data\\test_cube.stl'
test_write = 'E:\\cctech\\stl_obj_convertor\\test\\test_data\\result.obj'

write_file = open(test_write,'r+')
    
reader = StlReader()
vertex_convertor = StlVertexConvertor()
normal_convertor = StlNormalConvertor()
writer = ObjWriter()

def main():
    with open(test_read, 'r') as file:
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

main()

written_file_content = open(test_write,'r').read()

expected_written_content = open('E:\\cctech\\stl_obj_convertor\\test\\test_data\\expected.obj', 'r').read()

class TestObjWriter(unittest.TestCase):
    def test_the_written_file_is_not_empty(self):
        self.assertNotEqual(len(written_file_content),0)

    def test_the_writer_writes_the_file_correctly(self):
        self.assertEqual(written_file_content, expected_written_content)

