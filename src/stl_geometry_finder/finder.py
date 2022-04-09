from src.stl_to_obj.stl_obj_convertor import StlNormalConvertor, StlVertexConvertor


class IndexFinder(StlNormalConvertor, StlVertexConvertor):
    """
    StlNormalConvertor
    -----------------
    Methods - store_normals()
    Attribute - self.all_normals

    StlVertexConvertor
    ----------------
    Methods - store_vertices()
    Attribute - self.all_vertices
    """
    def __init__(self):
        super().__init__()
        self.index_of_vertex = int()
        self.index_of_normal = int()

    def find_index_of_input_vertex(self, vertex):
        for v in self.all_vertices:
            if vertex == v:
                self.index_of_vertex = self.all_vertices.index(vertex)
                break

    def find_index_of_input_normal(self, normal):
        for vn in self.all_normals:
            if normal == vn:
                self.index_of_normal = self.all_normals.index(normal)


class NormalFinder(IndexFinder, StlNormalConvertor):
    def __init__(self):
        super().__init__()
        self.normal_index = list()
        self.normals_linked_with_vertex = list()

    def find_normal_index(self,vertex, all_vertices):
        for v in all_vertices:
            if v == vertex:
                self.normal_index.append(all_vertices)

