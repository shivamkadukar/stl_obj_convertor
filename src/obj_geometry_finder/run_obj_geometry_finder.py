from src.obj_to_stl.obj_reader import ObjReader
from src.obj_to_stl.obj_stl_convertor import ObjFaces, ObjVertexConvertor
from src.obj_to_stl.normal_vertex import Vertex, Normal
from src.obj_geometry_finder.finder import VertexFinder, NormalFinder, EdgesFinder, FacesFinder
from src.file import file_to_read

reader = ObjReader()
stores_faces = ObjFaces()
vertices = Vertex()
normals = Normal()

print('''This is a geometry finder. It can find vertices, edges, normals, faces
in .obj or .stl file.
Input : Vertex --> Output: Normals, Edges, Faces
Input : Normal --> Output : Vertices, Edges, Face
''')

input_data = input('Enter a Vertex or a Normal: ')  # ('0.000000e+000','1.000000e+002','1.000000e+002') ('-1.000000e+000', '0.000000e+000', '0.000000e+000')
#('-1.3143', '15.0686', '-1.6458') ('-0.3819', '-0.2594', '-0.8871')
type_of_input = input("What is it? press 'v' for vertex and 'n' for normal: ")


def read():
    with open(file_to_read, 'r') as file:
        for line in file:
            reader.search_vertices(line)
            reader.search_normals(line)
            reader.search_faces(line)

    vertices.store_vertices(reader.searched_vertices)
    normals.store_vertex_normals(reader.searched_normals)

    reader.searched_vertices.clear()
    reader.searched_normals.clear()

    stores_faces.replace_space_with_slash(reader.searched_faces)

    reader.searched_faces.clear()

read()


def geometry_finder_vertex_as_input():
    normal_finder = NormalFinder()

    normal_finder.find_index_of_input_vertex(input_data,vertices.all_vertices)

    normal_finder.find_normal_index(stores_faces.face_list_with_texture,stores_faces.face_list_no_texture)

    normal_finder.find_normals(normals.vertex_normals)

    print(f'Normals: {normal_finder.normals_linked_with_vertex}')
    print('\n')

    edges_finder = EdgesFinder()

    vertex_convertor = ObjVertexConvertor()
    vertex_convertor.store_vertices(stores_faces.face_list_with_texture,stores_faces.face_list_no_texture)
    # print(vertex_convertor.all_vertex_index)

    edges_finder.find_index_of_input_vertex(input_data,vertices.all_vertices)

    edges_finder.find_edges_index(vertex_convertor.all_vertex_index)

    # print(edges_finder.edges_list)

    edges_finder.store_edges(vertices.all_vertices)
    print(f"Edges: {edges_finder.edges}")
    print('\n')

    faces_finder = FacesFinder()
    vertex_convertor.store_vertex_index()
    vertex_convertor.store_vertex_index_in_triangulated_form()
    faces_finder.find_index_of_input_vertex(input_data,vertices.all_vertices)

    faces_finder.store_face(vertex_convertor.triangulated_vertices,vertices.all_vertices)

    print(f"Faces: {faces_finder.faces}")


def geometry_finder_normal_as_input():
    vertex_finder = VertexFinder()

    vertex_finder.find_index_of_input_normal(input_data,normals.vertex_normals)

    vertex_finder.find_vertex_index(stores_faces.face_list_with_texture,stores_faces.face_list_no_texture)

    print(vertex_finder.vertex_index)
    vertex_finder.find_vertex(vertices.all_vertices)

    print(f'Vertices: {vertex_finder.vertices_linked_with_normals}')
    print('\n')
    edges_finder = EdgesFinder()

    vertex_convertor = ObjVertexConvertor()
    vertex_convertor.store_vertices(stores_faces.face_list_with_texture,stores_faces.face_list_no_texture)
    # print(vertex_convertor.all_vertex_index)

    for index in vertex_finder.vertex_index:
        edges_finder.find_index_of_input_vertex(index,vertices.all_vertices)

        edges_finder.find_edges_index(vertex_convertor.all_vertex_index)

        # print(edges_finder.edges_list)

        edges_finder.store_edges(vertices.all_vertices)

        print(f"Edges: {edges_finder.edges}")
        edges_finder.edges.clear()
        print('\n')

    faces_finder = FacesFinder()
    vertex_convertor.store_vertex_index()
    vertex_convertor.store_vertex_index_in_triangulated_form()
    faces_finder.find_index_of_input_vertex(input_data,vertices.all_vertices)
    faces_finder.store_face(vertex_convertor.triangulated_vertices,vertices.all_vertices)
    print(f"Faces: {faces_finder.faces}")
    faces_finder.faces.clear()
    print('\n')


def main():
    if type_of_input == 'v':
        geometry_finder_vertex_as_input()

    elif type_of_input == 'n':
        geometry_finder_normal_as_input()

