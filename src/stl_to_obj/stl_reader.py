import re

class StlReader():
    def __init__(self):
        self.searched_vertices = []
        self.searched_normals = []

    def search_vertices(self, line):
        """
        StlReader.search_vertices :
        Check if the line is a vertex line.

        Parameters
        ----------
        line : line from the file to read.

        Returns
        -------
        returns None. Stores the vertices in searched_vertices list.
        """
        vertices = re.compile(r"vertex .+")
        if re.search(vertices, line):
            line = line.replace('vertex', ' ')
            line = line.strip()
            self.searched_vertices.append(line)
    
    def search_normals(self, line):
        """
        StlReader.search_normals :
        Check if the line is a normal line.

        Parameters
        ----------
        line : A line from file to read.

        Returns
        -------
        returns None. Stores the normals in searched_normals list.
        """
        normals = re.compile(r"facet normal .+")
        if re.search(normals, line):
            line = line.replace('facet normal', ' ')
            line = line.strip()
            self.searched_normals.append(line)
        

#print(StlReader.search_normals.__doc__, StlReader.search_vertices.__doc__)

