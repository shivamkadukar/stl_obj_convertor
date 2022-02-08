import unittest

from src.obj_to_stl.obj_reader import *

reader = ObjReader()

class TestObjReader(unittest.TestCase):
    
    def test_is_instance(self):
        self.assertIsInstance(reader.searched_vertices, list)
        self.assertIsInstance(reader.searched_normals, list)
        self.assertIsInstance(reader.searched_faces, list)

    def test_search_vertices(self):
        reader.search_vertices('v 1 2 3') 
        self.assertEqual(reader.searched_vertices,['1 2 3'])

    def test_search_normals(self):
        reader.search_normals('vn 1 2 3')
        self.assertEqual(reader.searched_normals, ['1 2 3'])

    def test_search_faces(self):
        reader.search_faces('f 5/2/3 4/5/2 8/5/3')
        reader.search_faces('f 5//2//3 4/5/2 8/5/3')
        self.assertEqual(reader.searched_faces,['5/2/3 4/5/2 8/5/3', '5//2//3 4/5/2 8/5/3'])

