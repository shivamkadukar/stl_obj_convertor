import re


class ObjReader:
    def __init__(self):
        self.searched_vertices = []
        self.searched_normals = []
        self.searched_faces = []

    def search_vertices(self, line):
        v = re.compile(r'v .+')
        if re.search(v, line):
            line = line.replace('v', ' ')
            line = line.strip()
            self.searched_vertices.append(line)

    def search_normals(self,line):
        vn = re.compile(r'vn .+')
        if re.search(vn, line):
            line = line.replace('vn',' ')
            line = line.strip()
            self.searched_normals.append(line)

    def search_faces(self,line):
        f = re.compile(r'f \d+[\\+|\/+]+\d+')
        if re.search(f, line):
            line = line.replace('f', ' ')
            line = line.strip()
            self.searched_faces.append(line)


class Vertex:
    def __init__(self):
        self.all_vertices = []

    def store_vertices(self,searched_vertices):
        for line in searched_vertices:
            vertices = line.split()
            vertex = tuple((i for i in vertices))
            self.all_vertices.append(vertex)


class Normal:
    def __init__(self):
        self.all_normals = []
        self.normal_strings = []

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
