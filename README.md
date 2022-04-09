# .STL to .Obj and .Obj to .Stl convertor

:vulcan_salute: Hi, I am _Shivam Kadukar_. I am a self though programmer and this is my first project of making a python package.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [TechnologiesUsed](#technologies-used)
- [Contributors](#contributorscontributors)
- [Development](#development)
- [Version Info](#version-info)
- [FAQs](#faqs)

### Introduction

This python package converts .stl file to .obj file format and vice versa.

#### .stl File

The STL file format provides two different ways of storing information about the triangular facets that tile the object surface. These are called ASCII encoding and binary encoding. In both formats, the information of each triangle is stored as:

- The coordinates of the vertices.
- The components of the unit normal vector to the triangle. The normal vector should point outwards with respect to the 3D model.

#### .stl file format

An ASCII STL file begins with the line

> _solid name_

where name is an optional string (though if name is omitted there must still be a space after solid). The file continues with any number of triangles, each represented as follows:
```
facet normal ni nj nk
    outer loop
        vertex v1x v1y v1z
        vertex v2x v2y v2z
        vertex v3x v3y v3z
    endloop
endfacet
 ```

You can read more about .Stl files [here](https://en.wikipedia.org/wiki/STL_(file_format) ".stl file wikipedia")

#### .obj file

An OBJ file is a standard 3D image format that can be exported and opened by various 3D image editing programs. It contains a three-dimensional object, which includes 3D coordinates, texture maps, polygonal faces, and other object information

#### .obj file format

An OBJ file may contain vertex data, free-form curve/surface attributes, elements, free-form curve/surface body statements, connectivity between free-form surfaces, grouping and display/render attribute information. The most common elements are geometric vertices, texture coordinates, vertex normals and polygonal faces:

Anything following a hash character (#) is a comment.
\# this is a comment
```
\\# List of geometric vertices, with (x, y, z [,w]) coordinates, w is optional and defaults to 1.0.
v 0.123 0.234 0.345 1.0
v ...
...
\# List of texture coordinates, in (u, [,v ,w]) coordinates, these will vary between 0 and 1. v, w are optional and default to 0.
vt 0.500 1 [0]
vt ...
...
\# List of vertex normals in (x,y,z) form; normals might not be unit vectors.
vn 0.707 0.000 0.707
vn ...
...
\# Parameter space vertices in ( u [,v] [,w] ) form; free form geometry statement ( see below )
vp 0.310000 3.210000 2.100000
vp ...
...
\# Polygonal face element (see below)
f 1 2 3
f 3/1 4/2 5/3
f 6/4/1 3/5/3 7/6/5
f 7//1 8//2 9//3
f ...
...
\# Line element (see below)
l 5 8 1 2 4 9
```

You can read more about .obj files [here](https://en.wikipedia.org/wiki/Wavefront_.obj_file ".obj File Wikipedia")

### Installation

```
pip install -i https://test.pypi.org/simple/ stl-obj-convertor
```
### How to use this convertor?

To use this convertor, run the following command

``` python
from stl_obj_convertor import convertor
```

You can try out the package on this [file](https://drive.google.com/drive/folders/1HpkMrwUWt8scaL5o78qVAc-gynplM91g?usp=sharing) (more files will be added soon)

You will have to give to inputs, The file you want to convert.
(ex - E:\\cctech\\assignment 1 stl_obj_convertor\\data\\cube.stl)

And, the location and the name of the converted file
(ex - E:\\cctech\\assignment 1 stl_obj_convertor\\data\\new.obj)

The convertor will check the file type, if the file is .stl type then it will run .stl to .obj conversion and if the file is .obj type then it will run .obj to .stl conversion. 

Note - Make sure the file to read i.e. the first input is either a .stl file or a .obj file any other file type will result in an error.

You can view the converted file [here](https://www.creators3d.com/online-viewer)

To run the test suite, run the following command

```
python -m unittest
```

This command will run all the tests present in the test suite of this package.

### Technologies used

This package does not requires any third party python libraries and functionalites to work except which comes with
python 3.0 or greater.

This version of the package uses regular expressions (_regex_) python module to search for patterns which are explained in .stl and .obj file formats.

#### Development

[x] __Phase 1__: Created the converter using procedural code format and tested on simple geometries like a cube, etc.

[x] __Phase 2__: Recreated the convertor code in Oops format and tested on more complex geometries like a teapot, liver, ferrari, etc.

[x] __Phase 3__: Wrote Test Suite for the project and published as a python package. (version 1.0.0)

[] __Phase 4__: Level up your code to include a geometry finder which, for instance, returns the connected vertices from a given vertice. Various possible inputs & outputs are as follows:
  \- Input: vertice Output: vertices, edges, faces
  \- Input: edge Output: vertices, edges, faces
  \- Input: face Output: vertices, edges, faces

[] __Phase 5__: To conserve memory, use file streaming methods to convert from one format to another. Simultaneous read and write of the files.

#### Version Info

|  Version     |                                                                           |
|--------------|---------------------------------------------------------------------------|
|   0.1.0      | Converts .obj to .stl and vice versa                                      |
|   0.1.1      | Improved the Readme.md and added link to sample files to run the packages |
|   0.2.0      | Added progress bar to check progress of file conversion                   |
|   0.3.0      | .obj to .stl conversion of files with quadrilateral faces

### Contributors

| Name         | Contact             |
|--------------|---------------------|
|Shivam Kadukar|shivamk2802@gmail.com|

### FAQs

1) Does this convertor binary .stl file to .obj?
Ans - No, The current version of this convertor package can only converts ASCII .stl to .obj.
    But, the feature will be added in next version of the package.

2) Does this convertor converts .obj file with faces which are not in trainglur forms?
Ans - Package lower other than 0.3.0 can only convert .obj files with trianular faces. Version 0.3.0 can convert .obj file with quadrilateral faces(testing of faces with more than 4 vertices are yet to be tested.)



