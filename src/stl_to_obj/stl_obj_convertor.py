class StlVertexConvertor:
    def __init__(self):
        self.v_list = []
        self.v_index = []
        self.all_vertices = list()
        self.all_vertices_index = []
        self.triangle_vertex_index = []

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

    def store_vertices(self, searched_vertices):
        """
        StlVertexConvertor.store_vertices:
        Stores the vertices in tuple by separating its co-ordinate as (x,y,z)
        This function is only used for geometry finder. It has no use in stl to obj conversion

        Parameters
        ----------
        searched_vertices : A list of all the vertices searched by stl_reader.

        Returns
        -------
        None. Converts string vertices to a tuple of floats of co-ordinates.
        """
        for vertex in searched_vertices:
            vertex = vertex.split()
            vertex_list = tuple([float(i) for i in vertex])
            self.all_vertices.append(vertex_list)

    def store_all_vertex_index(self,searched_vertices):
        """
        StlVertexConvertor.store_all_vertex_index:
        Stores the index of  all vertices
        This function is only used for geometry finder. It has no use in stl to obj conversion

        Parameters
        ----------
        searched_vertices : A list of all the vertices searched by stl_reader.
        self.v_list : A list of unique/non-duplicate vertices

        Returns
        -------
        None. Stores the index of vertices from searched_vertices by searching them in self.v_list
        """
        for vertex in searched_vertices:
            self.all_vertices_index.append(self.v_list.index(vertex))

    def store_vertex_index_in_triangulated_form(self):
        """
        StlVertexConvertor.store_vertex_index_in_triangulated_form:
        Stores the index of vertices in form of list of 3 vertices.
        This function is only used for geometry finder. It has no use in stl to obj conversion

        Parameters
        ----------
        self.all_vertex_index : A list of indexes of all vertices

        Returns
        -------
        None. Stores the index of vertices in form of list of list where each sub list is of length = 3
        """
        for i in range(0, len(self.all_vertices_index),3):
            temp = list()
            temp.append(i)
            temp.append(i + 1)
            temp.append(i + 2)
            self.triangle_vertex_index.append(temp)


class StlNormalConvertor:
    def __init__(self):
        self.vn_list = []
        self.vn_index = []
        self.all_normals = list()
        self.all_normal_index = list()
    
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

    def store_normals(self,searched_normals):
        for normal in searched_normals:
            normal = normal.split()
            normal_list = tuple([float(i) for i in normal])
            self.all_normals.append(normal_list)

    def store_all_normal_index(self,searched_normals):
        """
        StlVertexConvertor.store_all_normal_index:
        Stores the index of  all normal
        This function is only used for geometry finder. It has no use in stl to obj conversion

        Parameters
        ----------
        searched_normals : A list of all the normals searched by stl_reader.
        self.vn_list : A list of unique/non-duplicate normals

        Returns
        -------
        None. Stores the index of vertices from searched_vertices by searching them in self.v_list
        """
        for normal in searched_normals:
            self.all_normal_index.append(self.vn_list.index(normal))


   


