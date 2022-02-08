import unittest

from src.stl_to_obj.stl_reader import *

reader = StlReader()

class TestStlReader(unittest.TestCase):
    def test_is_instance(self):
        self.assertIsInstance(reader.searched_vertices, list)
        self.assertIsInstance(reader.searched_normals, list)

    def test_search_vertices(self):
        reader.search_vertices('vertex 1 2 3')
        reader.search_vertices('vertex 2.0 5.8 6.4')
        self.assertEqual(reader.searched_vertices, ['1 2 3', '2.0 5.8 6.4'])

    def test_search_normals(self):
        reader.search_normals('facet normal 1 2 3')
        self.assertEqual(reader.searched_normals, ['1 2 3'])


