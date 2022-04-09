import re


class ObjFaces:
    def __init__(self):
        self.face_list_with_texture = []
        self.face_list_no_texture = []

    def replace_space_with_slash(self, faces):

        pattern1 = re.compile(r'\d+[\\+|\/+]+\d+[\\+|\/+]+\d+')
        pattern2 = re.compile(r'\d+[\\+|\/+]+\d+')

        for face in faces:
            slash_pattern = re.compile(r'\\+|\/+')
            slash = (re.search(slash_pattern, face)).group()
            if re.search(pattern1, face):
                face = face.replace(' ',slash)
                face = face.split(slash)
                self.face_list_with_texture.append(face)

            elif re.search(pattern2,face):
                face = face.replace(' ',slash)
                face = face.split(slash)
                self.face_list_no_texture.append(face)


class ObjVertexConvertor:
    def __init__(self):
        self.all_vertex_index = []
        self.vertex_index = []
        self.triangulated_vertices = []

    def store_vertices(self, face_list_with_texture, face_list_no_texture):
        for face_list in face_list_with_texture:
            temp_list = []
            for i in range(0,len(face_list),3):
                vertex = int(face_list[i]) - 1
                temp_list.append(vertex)
            self.all_vertex_index.append(temp_list)

        for face_list in face_list_no_texture:
            temp_list = []
            for i in range(0,len(face_list),2):
                vertex = int(face_list[i]) - 1
                temp_list.append(vertex)
            self.all_vertex_index.append(temp_list)

        face_list_with_texture.clear()
        face_list_no_texture.clear()

    def store_vertex_index(self):
        for vertex_list in self.all_vertex_index:
            for i in range(1,len(vertex_list)):
                if len(vertex_list) - i < 2:
                    break
                self.vertex_index.append(vertex_list[0])
                self.vertex_index.append(vertex_list[i])
                self.vertex_index.append(vertex_list[i + 1])

        self.all_vertex_index.clear()

    def store_vertex_index_in_triangulated_form(self):
        '''Only required for geometry finder has no use in obj to stl conversion'''
        for i in range(0, len(self.vertex_index),3):
            temp_list = []
            temp_list.append(self.vertex_index[i])
            temp_list.append(self.vertex_index[i + 1])
            temp_list.append(self.vertex_index[i + 2])
            self.triangulated_vertices.append(temp_list)

