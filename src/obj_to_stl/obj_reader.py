import re
class ObjReader():
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
        #print(self.searched_vertices)
    
    def search_normals(self, line):
        vn = re.compile(r'vn .+')
        if re.search(vn, line):
            line = line.replace('vn', ' ')
            line = line.strip()
            self.searched_normals.append(line)
        #print(self.searched_normals)
    
    def search_faces(self,line):
        f = re.compile(r'f \d+[\\+|\/+]+\d+')
        if re.search(f, line):
            line = line.replace('f', ' ')
            line = line.strip()
            self.searched_faces.append(line)
        #print(self.searched_faces)