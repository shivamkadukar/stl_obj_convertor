class IndexFinder:
    def __init__(self):
        self.index_of_vertex = 0
        self.index_of_normal = 0

    def find_index_of_input_vertex(self, vertex, all_vertices):
        for v in all_vertices:
            if vertex == v:
                self.index_of_vertex = all_vertices.index(vertex)
                break

    def find_index_of_input_normal(self, normal, vertex_normals):
        for vn in vertex_normals:
            if vn == normal:
                self.index_of_normal = vertex_normals.index(normal)
                break


class VertexFinder(IndexFinder):
    def __init__(self):
        super().__init__()
        self.vertex_index = []
        self.vertices_linked_with_normals = []
    
    def find_vertex_index(self, face_list_with_texture, face_list_no_texture):
        normal = str(self.index_of_normal + 1)
        for face_list in face_list_with_texture:
            face_list = face_list[::-1]
            for i in range(0,len(face_list),3):
                if face_list[i] == normal:
                    self.vertex_index.append(int(face_list[i + 2])-1)

        for face_list in face_list_no_texture:
            face_list = face_list[::-1]
            for i in range(0,len(face_list),2):
                if face_list[i] == normal:
                    self.vertex_index.append(int(face_list[i + 1])-1)

    def find_vertex(self, searched_normals):
        for i in self.vertex_index:
            self.vertices_linked_with_normals.append(searched_normals[i])


class NormalFinder(IndexFinder):
    def __init__(self):
        super().__init__()
        self.normal_index = []
        self.normals_linked_with_vertex = []

    def find_normal_index(self, face_list_with_texture, face_list_no_texture):
        vertex = str(self.index_of_vertex + 1)
        for face_list in face_list_with_texture:
            for i in range(0,len(face_list),3):
                if face_list[i] == vertex:
                    self.normal_index.append(face_list[face_list.index(vertex) + 2])

        for face_list in face_list_no_texture:
            for i in range(0,len(face_list),2):
                if face_list[i] == vertex:
                    self.normal_index.append(face_list[face_list.index(vertex) + 1])

    def find_normals(self, searched_normals):
        for i in self.normal_index:
            index = int(i) - 1
            self.normals_linked_with_vertex.append(searched_normals[index])


class EdgesFinder(IndexFinder):
    def __init__(self):
        super().__init__()
        self.edges_list = []
        self.edges = []

    def find_edges_index(self, all_vertex_index):
        for index_list in all_vertex_index:
            for index,element in enumerate(index_list):
                if element == self.index_of_vertex:
                    temp_tuple = [index_list[index],index_list[index - 1]]
                    if temp_tuple not in self.edges_list:
                        self.edges_list.append(temp_tuple)

                    temp_tuple = [index_list[index],index_list[index - 2]]
                    if temp_tuple not in self.edges_list:
                        self.edges_list.append(temp_tuple)

    def store_edges(self, all_vertices):
        for index_list in self.edges_list:
            temp = []
            for i in index_list:
                temp.append(all_vertices[i])
            temp = tuple(temp)
            self.edges.append(temp)


class FacesFinder(IndexFinder):
    def __init__(self):
        super().__init__()
        self.faces = []

    def store_face(self, triangulated_vertices, all_vertices):
        for triangle_list in triangulated_vertices:
            vertex_list = []
            if self.index_of_vertex in triangle_list:
                vertex_list.append(all_vertices[triangle_list[0]])
                vertex_list.append(all_vertices[triangle_list[1]])
                vertex_list.append(all_vertices[triangle_list[2]])

                [px1,py1,pz1] = vertex_list[0]
                [px2,py2,pz2] = vertex_list[1]
                [px3,py3,pz3] = vertex_list[2]

                ux = float(px2) - float(px1)
                uy = float(py2) - float(py1)
                uz = float(pz2) - float(pz1)

                vx = float(px3) - float(px1)
                vy = float(py3) - float(py1)
                vz = float(pz3) - float(pz1)

                nx = (uy * vz) - (uz * vy)
                ny = (ux * vz) - (uz * vz)
                nz = (ux * uy) - (vx * uy)

                normal = (nx, ny, nz)

                face = dict()

                face['vertex'] = vertex_list
                face['normal'] = normal

                self.faces.append(face)














