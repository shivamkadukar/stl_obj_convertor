import unittest

from src.obj_to_stl.obj_stl_convertor import *
from src.obj_to_stl.normal_vertex import *

facesconvertor = ObjFaces()


class TestObjFaces(unittest.TestCase):
    def test_stores_faces_as_list(self):
        facesconvertor.faces = ['2/1/1 3/2/1 4/3/1 1/2/3']
        expected_list = [['2', '1', '1', '3', '2', '1', '4', '3', '1','1','2','3']]
        facesconvertor.replace_space_with_slash(facesconvertor.faces)
        self.assertEqual(facesconvertor.face_list_with_texture, expected_list)

vertex = Vertex()
vertexconvertor = ObjVertexConvertor()


class TestObjVertexConvertor(unittest.TestCase):
    def test_stores_vertex_as_tuple(self):
        test_list = ['1 2 3']
        expected_tuple = [('1','2','3')]

        vertex.store_vertices(test_list)
        self.assertEqual(vertex.all_vertices, expected_tuple)

    def test_stores_vertex_index_from_face_list(self):
        test_list_1 = [['2', '1', '1', '3', '2', '1', '4', '3', '1','1','2','3']]
        test_list_2 = [['2', '1', '1', '3']]
        expected_list = [[1, 2, 3, 0], [1, 0]]

        vertexconvertor.store_vertices(test_list_1, test_list_2)
        self.assertEqual(vertexconvertor.all_vertex_index,expected_list)

    def test_converts_polygon_faces_to_triangular_faces(self):
        vertexconvertor.all_vertex_index = [['1','2','3','0']]
        expected_list = ['1','2','3','1','3','0']

        vertexconvertor.store_vertex_index()
        self.assertEqual(vertexconvertor.vertex_index, expected_list)


















