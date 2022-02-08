class StlVertexConvertor:
    def __init__(self):
        self.v_list = []
        self.v_index = []

    def vertex_index(self, searched_vertices):
        """
        StlVertexConvertor.vertex_index:
        Stores unique vertices.

        Parameters
        ----------
        searched_vertices: A list of all the vertices searched by stl_reader

        Returns
        -------
        None. Appends unique vertices to v_list list.
        """
        for v in searched_vertices:
            if v not in self.v_list:
                self.v_list.append(v)
    
    def unique_vertex_index(self, searched_vertices):
        """
        StlVertexConvertor.unique_vertex_index:
        Stores index of searched_vertices by searching it in v_list
        
        Parameters
        ----------
        searched_vertices: A list of all the vertices searched by stl_reader.
        self.v_list : A list containing only unique/non duplicate vertices

        Returns
        -------
        None. Appends the index of vertices to v_index
        """
        for vertex in searched_vertices:
            index = self.v_list.index(vertex) + 1
            self.v_index.append(index)

class StlNormalConvertor:
    def __init__(self):
        self.vn_list = []
        self.vn_index = []
    
    def normal_index(self, searched_normals):
        """
        StlNormalConvertor.normal_index:
        Stores unique normal.

        Parameters
        ----------
        searched_normals: A list of all the normals searched by stl_reader

        Returns
        -------
        None. Appends unique normals to vn_list list.
        """
        for vn in searched_normals:               
            if vn not in self.vn_list:
                self.vn_list.append(vn)
    
    def unique_normal_index(self, searched_normals):
        """
        StlNormalConvertor.unique_normal_index:
        Stores index of searched_normals by searching it in vn_list
        
        Parameters
        ----------
        searched_normals: A list of all the  searched by stl_reader.
        self.vn_list : A list containing only unique/non duplicate normals

        Returns
        -------
        None. Appends the index of normals to vn_index
        """
        for normal in searched_normals:
            vn = self.vn_list.index(normal) + 1
            self.vn_index.append(vn)


'''def replace_vertices(self, searched_vertices):
        
        StlVertexConvertor.replace_vertices:
        replaces 'vertex' with 'v' to convert vertices to .obj format

        Parameters
        ----------
        searched_vertices : A list containing vertices in .stl format

        Returns 
        -------
        returns None. Appends converted vertices to all_vertices list.
        for vertex in searched_vertices:
            vertex = vertex.strip()
            vertex = vertex.replace('vertex', 'v')
            self.all_vertices.append(vertex)'''    


