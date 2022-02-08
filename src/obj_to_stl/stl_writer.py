from re import search


class StlWriter():
    def write(self, file, normal_index, searched_normals, vertex_index, searched_vertices):
        start, end = 0, 3
        
        file.write("solid\n")

        for normal in normal_index:
            file.write('\tfacet ')
            file.write('normal ')
            file.write(searched_normals[normal])
            file.write('\n')

            file.write('\t\touter loop\n')

            for vertex in vertex_index[start:end]:
                file.write('\t\t')
                file.write('vertex ')
                file.write(searched_vertices[vertex])
                file.write('\n')
            start += 3
            end += 3

            file.write('\t\tendloop\n')

            file.write('\tendfacet\n')
            
        file.write('endsolid')