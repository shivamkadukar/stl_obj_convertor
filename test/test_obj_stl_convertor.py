import unittest

from src.obj_to_stl.obj_reader import *
from src.obj_to_stl.obj_stl_convertor import *

vertexconvertor = ObjVertexConvertor()

class TestObjVertexConvertor(unittest.TestCase):
    def test_stores_vertex_index(self):
        face_data = [['1','2','3','4','5','6','7','8','9']]
        vertexconvertor.store_vertex_index(face_data)

        self.assertEqual(vertexconvertor.vertex_index, [0,3,6])


normalconvertor = ObjNormalConvertor()

class TestObjNormalConvertor(unittest.TestCase):
    def test_stores_normal_index(self):
        face_data = [['1','2','3','4','5','6','7','8','9']]
        normalconvertor.store_normal_index(face_data)

        self.assertEqual(normalconvertor.normal_index, [8])




