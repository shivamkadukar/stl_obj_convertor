class ObjWriter():
    def write(self, file_to_write, unique_vertices_list, unique_normals_list, v_index, vn_index):
        
        for vertex in unique_vertices_list:
            file_to_write.write("v ")
            file_to_write.write(vertex)
            file_to_write.write("\n")

        for normal in unique_normals_list:
            file_to_write.write("vn ")
            file_to_write.write(normal)
            file_to_write.write("\n")

        start, end = 0, 3
        for vn in vn_index:
            file_to_write.write('f ')
            for v in v_index[start: end]:
                file_to_write.write(f'{v}/{vn} ')
            file_to_write.write('\n')
            start += 3
            end += 3

        