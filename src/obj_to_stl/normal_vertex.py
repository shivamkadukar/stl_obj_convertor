class Vertex:
    def __init__(self):
        self.all_vertices = []

    def store_vertices(self,searched_vertices):
        for line in searched_vertices:
            vertices = line.split(' ')
            vertex = tuple((i for i in vertices))
            self.all_vertices.append(vertex)


class Normal:
    def __init__(self):
        self.all_normals = []
        self.normal_strings = []
        self.vertex_normals = []

    def store_vertex_normals(self, searched_normals):
        for line in searched_normals:
            normals = line.split()
            normal = tuple((i for i in normals ))
            self.vertex_normals.append(normal)

    def calculate_normals(self, all_vertices, vertex_index):
        start = 0
        for i in range(0, int(len(vertex_index)/3)):
            v1 = all_vertices[vertex_index[start]]
            v2 = all_vertices[vertex_index[start + 1]]
            v3 = all_vertices[vertex_index[start + 2]]

            [px1, py1, pz1] = v1
            [px2,py2,pz2] = v2
            [px3,py3,pz3] = v3

            ux = float(px2) - float(px1)
            uy = float(py2) - float(py1)
            uz = float(pz2) - float(pz1)

            vx = float(px3) - float(px1)
            vy = float(py3) - float(py1)
            vz = float(pz3) - float(pz1)

            nx = (uy * vz) - (uz * vy)
            ny = (ux * vz) - (uz * vz)
            nz = (ux * uy) - (vx * uy)

            start += 3

            self.all_normals.append([nx, ny, nz])

    def convert_calculated_normals_to_string(self):
        for normal in self.all_normals:
            normal_string = ' '.join([str(point) for point in normal])
            self.normal_strings.append(normal_string)
