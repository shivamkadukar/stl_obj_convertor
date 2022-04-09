from utilis.progressbar import printprogreesbar

class StlWriter:
    def write(self, file, normal_strings, vertex_index, searched_vertices):
        start, end = 0, 3

        length = len(normal_strings)
        printprogreesbar(0, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
        
        file.write("solid\n")
        
        for i, normal_string in enumerate(normal_strings):
            file.write('\tfacet ')
            file.write('normal ')
            file.write(normal_string)
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

            printprogreesbar(i+1, length, prefix = 'Progress:', suffix = 'Complete', length = 50)
               
        file.write('endsolid')