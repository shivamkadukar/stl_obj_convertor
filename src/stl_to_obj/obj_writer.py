from utilis.progressbar import printprogreesbar


class ObjWriter:
    def write(self, file_to_write, unique_vertices_list, unique_normals_list, v_index, vn_index):
        
        lv = len(unique_vertices_list)
        printprogreesbar(0, lv, prefix = 'Converting Vertices:', suffix = 'Complete', length = 50)

        for i, vertex in enumerate(unique_vertices_list):
            file_to_write.write("v ")
            file_to_write.write(vertex)
            file_to_write.write("\n")
            
            printprogreesbar(i + 1, lv, prefix = 'Converting Vertices:', suffix = 'Complete', length = 50)

        lvn = len(unique_normals_list)
        printprogreesbar(0, lvn, prefix = 'Converting Normals:', suffix = 'Complete', length = 50)

        for i, normal in enumerate(unique_normals_list):
            file_to_write.write("vn ")
            file_to_write.write(normal)
            file_to_write.write("\n")

            printprogreesbar(i + 1, lvn, prefix = 'Converting Normals:', suffix = 'Complete', length = 50)

        start, end = 0, 3
        lf = len(vn_index)
        printprogreesbar(0, lf, prefix = 'Converting Faces:', suffix = 'Complete', length = 50)

        for i, vn in enumerate(vn_index):
            file_to_write.write('f ')
            for v in v_index[start: end]:
                file_to_write.write(f'{v}/{vn} ')
            file_to_write.write('\n')
            start += 3
            end += 3

            printprogreesbar(i+1, lf, prefix = 'Converting Faces:', suffix = 'Complete', length = 50)


        