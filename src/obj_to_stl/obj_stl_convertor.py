import re

class ObjFaces():
    def __init__(self):
        self.face_list = []
        self.face_data = []

    def replace_space_with_slash(self, faces):
        pattern = re.compile(r'\\+|\/+')
        for face in faces:
            slash = (re.search(pattern, face)).group()
            face = face.replace(' ', slash)
            self.face_list.append(face)

    def faces_data(self):
        pattern = re.compile(r'\\+|\/+')
        for face in self.face_list:
            slash = (re.search(pattern, face)).group()
            list = face.split(slash)
            self.face_data.append(list)

class ObjVertexConvertor():
    def __init__(self):
        self.vertex_index = []

    def store_vertex_index(self, face_data):
        """
        Store the index vertex data from the face line from the obj file.

        Parameters
        ----------
        face_data: A list of list containing face info from obj file.


        Returns 
        -------
        returns none. Appends vertex_index list.
        """
        for list in face_data:
            if len(list) == 9:
                self.vertex_index.append(int(list[0])-1)
                self.vertex_index.append(int(list[3])-1)
                self.vertex_index.append(int(list[6])-1)
                
            if len(list) == 6:
                self.vertex_index.append(int(list[0])-1)
                self.vertex_index.append(int(list[2])-1)
                self.vertex_index.append(int(list[4])-1) 

class ObjNormalConvertor():
    def __init__(self):
        self.normal_index = []
    
    def store_normal_index(self, face_data): 
        """
        Store the index normal data from the face line from the obj file.

        Parameters
        ----------
        face_data: A list of list containing face info from obj file.


        Returns 
        -------
        returns none. Appends normal_index list.
        """   
        for list in face_data:
            self.normal_index.append(int(list[-1])-1)

