import unittest

from src.stl_to_obj.stl_reader import *
from src.stl_to_obj.stl_obj_convertor import *

Vertex = StlVertexConvertor()
Normal = StlNormalConvertor()


class TestVertexConvertor(unittest.TestCase):
    
    def test_is_instance(self):
        self.assertIsInstance(Vertex.v_list, list)
        self.assertIsInstance(Vertex.v_index, list)

    def test_vlist_stores_non_duplicate_vertices(self):
        reader = StlReader()
        reader.searched_vertices = ['1 2 3', '2.0 5.8 6.4', '1 2 3', '2.0 5.8 6.4']
        Vertex.vertex_index(reader.searched_vertices)

        self.assertEqual(Vertex.v_list, ['1 2 3', '2.0 5.8 6.4'])


class TestNormalConvertor(unittest.TestCase):

    def test_is_instance(self):
        self.assertIsInstance(Normal.vn_list, list)
        self.assertIsInstance(Normal.vn_index, list)

    def test_vnlist_stores_non_duplicate_vertices(self):
        reader = StlReader()
        reader.searched_normals = ['1 2 3', '2.0 5.8 6.4', '1 2 3', '2.0 5.8 6.4']
        Normal.normal_index(reader.searched_normals)

        self.assertEqual(Normal.vn_list, ['1 2 3', '2.0 5.8 6.4'])

    
    