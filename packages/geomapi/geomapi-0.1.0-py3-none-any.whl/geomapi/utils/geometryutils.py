"""
Geometryutils - a Python library for processing mesh and point cloud data.
"""

from ast import Raise
from logging import warning
from operator import ge
from re import X
from xmlrpc.client import Boolean
import numpy as np 
import open3d as o3d 
import copy
import pye57 
pye57.e57.SUPPORTED_POINT_FIELDS.update({'nor:normalX' : 'd',
                                         'nor:normalY': 'd',
                                         'nor:normalZ': 'd',
                                         'sphericalRange': 'd',
                                         'sphericalAzimuth' : 'd',
                                         'sphericalElevation' : 'd',
                                         'class:classification':'d'})
from PIL import Image

import xml.etree.ElementTree as ET 
import math
from typing import List,Tuple
import matplotlib
import os
import cv2

import ifcopenshell
import ifcopenshell.geom as geom
import ifcopenshell.util
from scipy.spatial.transform import Rotation as R
import concurrent.futures

import trimesh
import fcl

#IMPORT MODULES
import geomapi.utils as ut

#### COORDINATE CONVERTERS ####

def cap_mesh(test):
    """UNTESTED CODE
    """
      # the plane we're using
    normal = trimesh.unitize([1,1,1])
    origin = m.center_mass

    # get a section as a Path3D object
    s = m.section(plane_origin=origin,
                  plane_normal=normal)

    # transform the Path3D onto the XY plane so we can triangulate
    on_plane, to_3D = s.to_planar()

    # triangulate each closed region of the 2D cap
    v, f = [], []
    for polygon in on_plane.polygons_full:
        tri = trimesh.creation.triangulate_polygon(polygon)
        v.append(tri[0])
        f.append(tri[1])
        
    # append the regions and re- index
    vf, ff = trimesh.util.append_faces(v, f)
    # three dimensionalize polygon vertices
    vf = np.column_stack((vf, np.zeros(len(vf))))
    # transform points back to original mesh frame
    vf = trimesh.transform_points(vf, to_3D)
    # flip winding of faces for cap
    ff = np.fliplr(ff)

    # the mesh for the planar cap
    cap = trimesh.Trimesh(vf, ff)

    # get the uncapped slice
    sliced = m.slice_plane(plane_origin=origin,
                           plane_normal=normal)

    # append the cap to the sliced mesh
    capped = sliced + cap

def mesh_to_trimesh(geometry: o3d.geometry) -> trimesh.Trimesh:
    """Convert open3D.geometry.TriangleMesh to [trimesh.Trimesh](https://trimsh.org/trimesh.html). \n
    
    **NOTE**: Only vertex_colors are implemented instead of face_colors with textures.\n

    Args:
        geometry (Open3D.geometry): OrientedBoundingBox, AxisAlignedBoundingBox or TriangleMesh
    
    Raises:
        ValueError('Incorrect geometry input. Only input o3d.geometry.TriangleMesh,o3d.geometry.AxisAlignedBoundingBox or o3d.geometry.OrientedBoundingBox or type(geometry)  ')

    Returns:
        trimesh.Trimesh
    """
    if type(geometry) is o3d.geometry.OrientedBoundingBox or type(geometry) is o3d.geometry.AxisAlignedBoundingBox:
        geometry=box_to_mesh(geometry)
    
    if type(geometry) is o3d.geometry.TriangleMesh and len(geometry.vertices) !=0:
        vertices= geometry.vertices
        faces= geometry.triangles
        face_normals=None
        vertex_normals=None
        # face_colors=None
        vertex_colors=None
        # color_visuals=None
        # texture_visuals=None
        # uv=None

        if geometry.has_triangle_normals():
            face_normals=geometry.triangle_normals
        if geometry.has_vertex_normals():
            vertex_normals=geometry.vertex_normals
        if geometry.has_triangle_uvs():
            uv=np.asarray(geometry.triangle_uvs)
        # if geometry.textures[1] is not None:
        #     pass
            # myarray=np.asarray(geometry.textures[1])
            # PIL_image = Image.fromarray(np.uint8(myarray)).convert('RGB')
            # material = trimesh.visual.texture.SimpleMaterial(image=PIL_image)
            # texture_visuals=trimesh.visual.TextureVisuals(uv=uv, material=material, image=PIL_image)
            # color_visuals=trimesh.visual.ColorVisuals(mesh=)
            # color_visuals = trimesh.visual.TextureVisuals(uv=uv, image=PIL_image, material=material)            
        if geometry.has_vertex_colors():
            colors=np.asarray(geometry.vertex_colors)*255
            vertex_colors=vertex_colors=colors.astype(int)
        try:
            triMesh= trimesh.Trimesh(vertices, faces, face_normals=face_normals, vertex_normals=vertex_normals, vertex_colors=vertex_colors) #, visual=texture_visuals
            
            return triMesh
        except:
            print('Open3D to Trimesh failed')
            return None
    else:
        raise ValueError('Incorrect geometry input. Only input o3d.geometry.TriangleMesh,o3d.geometry.AxisAlignedBoundingBox or o3d.geometry.OrientedBoundingBox or type(geometry)  ')

def crop_geometry_by_convex_hull(source:trimesh.Trimesh, cutters: List[trimesh.Trimesh], inside : Boolean = True ) -> trimesh.Trimesh:
    """Cut a portion of a mesh that lies within the convex hull of another mesh.
    
    .. image:: ../../../docs/pics/crop_by_convex_hull.PNG

    Args:
        1. source (trimesh.Trimesh):   mesh that will be cut \n
        2. cutter (trimesh.Trimesh):   mesh of which the faces are used for the cuts. Face normals should point outwards (positive side) \n
        3. strict (Boolean):           True if source faces can only be part of a single submesh\n
        4. inside (Boolean):           True if retain the inside of the intersection\n
        
    Returns:
        mesh (trimesh.Trimesh) or None 
    """
    #validate list
    cutters=ut.item_to_list(cutters)

    submeshes=[]
    for cutter in cutters:
        submesh=None
        #compute faces and centers
        convexhull=cutter.convex_hull
        plane_normals=convexhull.face_normals
        plane_origins=convexhull.triangles_center

        if inside: # retain inside
            submesh=source.slice_plane(plane_origins, -1*plane_normals)
            if len(submesh.vertices)!=0:
                submeshes.append(submesh)
        else:# retain outside
            #cut source mesh for every slicing plane on the box
            meshes=[]
            for n, o in zip(plane_normals, plane_origins):
                tempMesh= source.slice_plane(o, n)
                if not tempMesh.is_empty:
                    meshes.append(tempMesh)
            if len(meshes) !=0: # gather pieces
                combined = trimesh.util.concatenate( [ meshes ] )
                combined.merge_vertices(merge_tex =True,merge_norm =True )
                combined.remove_duplicate_faces()
                submesh=combined
                submeshes.append(submesh)

        # if strict and len(submesh.vertices)!=0:
        #     pcdSource=o3d.geometry.PointCloud()
        #     pcdSource.points=o3d.utility.Vector3dVector(source.vertices)           
        #     pcdSubMesh=o3d.geometry.PointCloud()
        #     pcdSubMesh.points=o3d.utility.Vector3dVector(submesh.vertices)
        #     dists=np.asarray(pcdSource.compute_point_cloud_distance(pcdSubMesh))
        #     mask= dists>=0.01  
        #     source.update_vertices(mask)
        #     source.remove_degenerate_faces()
    if submeshes:
        return submeshes
    else:
        return None

def get_mesh_representation(geometry)->o3d.geometry.TriangleMesh:
    """Returns the mesh representation of a o3d.geometry.TriangleMesh or o3d.geometry.PointCloud.\n
    Returns the convex hull if point cloud.

    Args:
        geometry (o3d.geometry.TriangleMesh or o3d.geometry.PointCloud)

    Raises:
        ValueError: 'No valid input: o3d.geometry.TriangleMesh or o3d.geometry.PointCloud'

    Returns:
        o3d.geometry.TriangleMesh 
    """
    if 'PointCloud' in str(type(geometry)):
        hull, _ =geometry.compute_convex_hull()
        return hull
    elif 'TriangleMesh' in str(type(geometry)):
        return geometry
    else:
        raise ValueError('No valid input: o3d.geometry.TriangleMesh or o3d.geometry.PointCloud')

def get_mesh_collisions_trimesh(sourceMesh: o3d.geometry.TriangleMesh, geometries: List[o3d.geometry.TriangleMesh]) -> List[int]:
    """Return indices of geometries that collide with the source.

    .. image:: ../../../docs/pics/collision_4.PNG

    Args:
        sourceMesh (o3d.geometry.TriangleMesh)\n
        geometries (List[o3d.geometry.TriangleMesh])

    Returns:
        List[int]: indices of inliers
    """
    # geometries=ut.item_to_list(geometries)
    if (type(sourceMesh) is o3d.cpu.pybind.geometry.TriangleMesh and len(sourceMesh.triangles) >0):
        myTrimesh=mesh_to_trimesh(sourceMesh)
        geometries=ut.item_to_list(geometries)
        # add all geometries to the collision manager
        collisionManager=trimesh.collision.CollisionManager()
        for idx,geometry in enumerate(geometries):
            if type(geometry) is o3d.geometry.TriangleMesh and len(geometry.triangles) >1:
                referenceTrimesh=mesh_to_trimesh(geometry)
                collisionManager.add_object(idx,referenceTrimesh)

        # report the collisions with the sourceMesh
        (is_collision, names ) = collisionManager.in_collision_single(myTrimesh, transform=None, return_names=True, return_data=False)    
        if is_collision:
            list=[int(name) for name in names]
            return list
    else:
        raise ValueError('condition not met: type(sourceMesh) is o3d.geometry.TriangleMesh and len(sourceMesh.triangles) >0')

def get_pcd_collisions(sourcePcd: o3d.geometry.PointCloud, geometries: List[o3d.geometry.PointCloud]) -> List[int]:
    """Return indices of geometries that collide with the source. This detection is based on the convex hull of the geometries and the sourcePcd.

    Args:
        1. sourceMesh (o3d.geometry.TriangleMesh)\n
        2. geometries (List[o3d.geometry.TriangleMesh])\n

    Returns:
        List[int]: indices
    """
    geometries=ut.item_to_list(geometries)
    if (len(sourcePcd.points) >0):
        sourceHull, _ = sourcePcd.compute_convex_hull()
        hulls=[]
        for geometry in geometries:
            hull, _ = geometry.compute_convex_hull()
            hulls.append(hull)
        return get_mesh_collisions_trimesh(sourceMesh=sourceHull, geometries=hulls)

    else:
        raise ValueError('condition not met: type(sourcePcd) is o3d.geometry.PointCloud and len(sourcePcd.points) >0')
        
#### FORMAT CONVERTERS ####

def get_data3d_from_pcd (pcd:o3d.geometry.PointCloud ) ->tuple:
    """Returns the data of an o3d.geometry.PointCloud as the data structure of an e57 file so it can be written to file. 

    Args:
        pcd (o3d.geometry.PointCloud)

    Returns:
        Data3D dictionary conform the E57 standard
    """
    data3D={}
    if pcd.has_points():
        array=np.asarray(pcd.points)
        cartesianX=array[:,0]
        cartesianY=array[:,1]
        cartesianZ=array[:,2]
        data3D.update({'cartesianX' : cartesianX,'cartesianY':cartesianY,'cartesianZ':cartesianZ})

    if pcd.has_colors():
        array=np.asarray(pcd.colors)
        colorRed=array[:,0]*255
        colorGreen=array[:,1]*255
        colorBlue=array[:,2]*255
        data3D.update({'colorRed' : colorRed,'colorGreen':colorGreen,'colorBlue':colorBlue})
    
    if pcd.has_normals():
        array=np.asarray(pcd.normals)
        nx=array[:,0]
        ny=array[:,1]
        nz=array[:,2]
        data3D.update({'nor:normalX' : nx,'nor:normalY':ny,'nor:normalZ':nz})
    return data3D

def arrays_to_pcd(tuple) -> o3d.geometry.PointCloud:
    """Returns PointCloud from e57 arrays.\n

    Args:
        tuple (Tuple): \n
            1. pointArray:np.array \n
            2. colorArray:np.array \n
            3. normalArray:np.array \n
            4. cartesianTransform:np.array \n

    Returns:
        o3d.geometry.PointCloud
    """        
    pointcloud = o3d.geometry.PointCloud()
    pointcloud.points = o3d.utility.Vector3dVector(tuple[0])
    if tuple[1] is not None:
        pointcloud.colors = o3d.utility.Vector3dVector(tuple[1])
    if tuple[2] is not None:
        pointcloud.normals = o3d.utility.Vector3dVector(tuple[2])
    if len(tuple)==5 and 'ndarray' in str(type(tuple[3])) :
        pointcloud.transform(tuple[3])  
    return pointcloud

def e57_get_cartesian_transform(header:dict)->np.array:
    """Returns cartesianTransform (np.array(4x4)) from a e57 header

    Args:
        header (dict): retrieved from pye57 e57.get_header(e57Index)

    Returns:
        cartesianTransform (np.array(4x4))
    """
    cartesianTransform=np.diag(np.diag(np.ones((4,4))))    
    if 'pose' in header.scan_fields:
        rotation_matrix=None
        translation=None
        if getattr(header,'rotation',None) is not None:
                rotation_matrix=header.rotation_matrix
        if getattr(header,'translation',None) is not None:
            translation=header.translation
        cartesianTransform=get_cartesian_transform(rotation=rotation_matrix,translation=translation)
    return  cartesianTransform

def e57_to_pcd(e57:pye57.e57.E57,e57Index : int = 0,percentage:float=1.0)->o3d.geometry.PointCloud:
    """Convert a scan from a pye57.e57.E57 file to o3d.geometry.PointCloud

    Args:
        1. e57 (pye57.e57.E57)\n
        2. e57Index (int,optional) \n
        3. percentage (float,optional): downsampling ratio. defaults to 1.0 (100%) \n

    Returns:
        o3d.geometry.PointCloud
    """
    #get header
    header = e57.get_header(e57Index)
    
    #get transformation
    cartesianTransform=e57_get_cartesian_transform(header)

    #get raw geometry (no transformation)
    rawData = e57.read_scan_raw(e57Index)    
    if all(elem in header.point_fields  for elem in ['cartesianX', 'cartesianY', 'cartesianZ']):   
        pointArray=e57_get_xyz_from_raw_data(rawData)
    elif all(elem in header.point_fields  for elem in ['sphericalRange', 'sphericalAzimuth', 'sphericalElevation']):   
        pointArray=e57_get_xyz_from_spherical_raw_data(rawData)
    else:
        raise ValueError('e57 rawData parsing failed.')

    #downnsample
    if percentage <1.0:
        indices=np.random.randint(0,len(pointArray)-1,int(len(pointArray)*percentage))
        pointArray=pointArray[indices]

    #create point cloud
    points = o3d.utility.Vector3dVector(pointArray)
    pcd=o3d.geometry.PointCloud(points)

    #get color or intensity
    if (all(elem in header.point_fields  for elem in ['colorRed', 'colorGreen', 'colorBlue'])
        or 'intensity' in header.point_fields ): 
        colors=e57_get_colors(rawData)
        if percentage <1.0:
            colors=colors[indices]
        pcd.colors=o3d.utility.Vector3dVector(colors) 

    #get normals
    if all(elem in header.point_fields  for elem in ['nor:normalX', 'nor:normalY', 'nor:normalZ']): 
        normals=e57_get_normals(rawData)
        if percentage <1.0:
            normals=normals[indices]
        pcd.normals=o3d.utility.Vector3dVector(normals)

    #return transformed data
    pcd.transform(cartesianTransform)    
    return pcd

def arrays_to_mesh(tuple) -> o3d.geometry.TriangleMesh:
    """Returns TriangleMesh from arrays.\n

    Args:
        tuple (Tuple): \n
            1. vertexArray:np.array \n
            2. triangleArray:np.array \n
            3. colorArray:np.array \n
            4. normalArray:np.array \n

    Returns:
        o3d.geometry.PointCloud
    """ 
    mesh = o3d.geometry.TriangleMesh()
    mesh.vertices = o3d.utility.Vector3dVector(tuple[0])
    mesh.triangles = o3d.utility.Vector3iVector(tuple[1])

    if tuple[2] is not None:
        mesh.vertex_colors = o3d.utility.Vector3dVector(tuple[2])
    if tuple[3] is not None:
        mesh.vertex_normals = o3d.utility.Vector3dVector(tuple[3])
    return mesh

def img_to_arrays(path:str,tasknr:int=0)->Tuple[np.array,int]:
    """Convert an img from a file path to a tuple of 1 np.arrays and a tasknr (used for multi-processing)\n

    Args:
        1. path (str): path to mesh file \n
        2. tasknr(int,optional): tasknr used to keep the order in multiprocessing

    Returns:
        Tuple[img (np.array), tasknr (int)]
    """
    img=cv2.imread(path)
    return img, tasknr

def mesh_to_arrays(path:str,tasknr:int=0)->Tuple[np.array,np.array,np.array,np.array,int]:
    """Convert a mesh from a file path to a tuple of 4 np.arrays.\n

    Features:
        0. vertexArray,triangleArray,colorArray,normalArray,tasknr \n

    Args:
        1. path (str): path to mesh file \n
        2. tasknr(int,optional): tasknr used to keep the order in multiprocessing

    Returns:
        Tuple[np.array,np.array,np.array,int]
    """
    if not os.path.exists(path):
        raise ValueError('File not found.')
    
    mesh=o3d.io.read_triangle_mesh(path)   
    vertexArray=np.asarray(mesh.vertices)
    triangleArray=np.asarray(mesh.triangles)

    #colors
    if mesh.has_vertex_colors():
        colorArray=np.asarray(mesh.vertex_colors)
    else:
        colorArray=None    
    #normals
    if mesh.has_vertex_normals():
        normalArray=np.asarray(mesh.vertex_normals)
    else:
        normalArray=None
    return vertexArray,triangleArray,colorArray,normalArray,tasknr

def pcd_to_arrays(path:str,percentage:float=1.0,tasknr:int=0)->Tuple[np.array,np.array,np.array,int]:
    """Convert a pcd from a pcd file to a tuple of 3 np.arrays.\n

    Features:
        1. ['cartesianX', 'cartesianY', 'cartesianZ'] \n
        2. ['colorRed', 'colorGreen', 'colorBlue'] \n
        3. ['normalX', 'normalY', 'normalZ']\n
        4. tasknr (int): int to retrieve order in multiprocessing

    Args:
        1. path (str): path to .pcd file \n
        2. percentage (float,optional): downsampling ratio. defaults to 1.0 (100%) \n
        3. tasknr (int): int to retrieve order in multiprocessing

    Returns:
        Tuple[np.array,np.array,np.array]
    """
    if not os.path.exists(path):
        raise ValueError('File not found.')
    
    pcd=o3d.io.read_point_cloud(path)   
    pointArray=np.asarray(pcd.points)
    
    #colors
    if pcd.has_colors():
        colorArray=np.asarray(pcd.colors)
    else:
        colorArray=None
    
    #normals
    if pcd.has_normals():
        normalArray=np.asarray(pcd.normals)
    else:
        normalArray=None

    #downnsample
    if percentage <1.0:
        indices=np.random.randint(0,len(pcd.points)-1,int(len(pcd.points)*percentage))
        pointArray=pointArray[indices]
        if pcd.has_colors():
            colorArray=colorArray[indices]
        if pcd.has_normals():
            normalArray=normalArray[indices]

    return pointArray,colorArray,normalArray,tasknr

def e57_get_xyz_from_spherical_raw_data(rawData: dict) -> np.array:
    """Converts spherical(rae) to cartesian(xyz), where rae = range, azimuth(theta), 
    elevation(phi). Where range is in meters and angles are in radians.\n
    
    Reference for formula: http://www.libe57.org/bestCoordinates.html \n

    Args:
        rawData (e57 dict):  rawData = e57.read_scan_raw(e57Index)   
        
    Returns:
        np.array (nx3): XYZ cartesian coordinates np.array
    """
    range = rawData.get('sphericalRange')
    theta = rawData.get('sphericalAzimuth')
    phi =  rawData.get('sphericalElevation')
    range_cos_phi = range * np.cos(phi)
    # pointArray= np.concatenate((
    #     range_cos_phi * np.cos(theta),
    #     range_cos_phi * np.sin(theta),
    #     range * np.sin(phi)
    # ), axis=1)
    # pointArray=np.reshape(pointArray.flatten('F'),(len(pointArray),3))

    pointArray=np.reshape(np.vstack( range_cos_phi * np.cos(theta),
                                    range_cos_phi * np.sin(theta),
                                    range * np.sin(phi)).flatten('F'),(len(range),3))
    return pointArray

def e57_get_xyz_from_raw_data(rawData: dict)->np.array:
    """returns xyz coordinates from e57 raw data.\n

    Args:
        rawData (e57 dict):  rawData = e57.read_scan_raw(e57Index)   
        
    Returns:
        np.array (nx3): XYZ cartesian coordinates np.array
    """
    x=rawData.get('cartesianX')
    y=rawData.get('cartesianY')
    z=rawData.get('cartesianZ') 
    pointArray=np.reshape(np.vstack(( x,y,z)).flatten('F'),(len(x),3))
    return pointArray

def e57_get_cartesianTransform(header)-> np.array:
    """Returns the cartesianTransform from an e57 header.\n

    Args:
        header (e57): rotation and translation should be present.

    Returns:
        np.array (4x4): transformation Matrix
    """
    if 'pose' in header.scan_fields:
        rotation_matrix=None
        translation=None
        if getattr(header,'rotation',None) is not None:
            rotation_matrix=header.rotation_matrix
        if getattr(header,'translation',None) is not None:
            translation=header.translation
        cartesianTransform=get_cartesian_transform(rotation=rotation_matrix,translation=translation)
        return cartesianTransform
    else:
        return None

def e57_to_arrays(e57Path:str,e57Index : int = 0,percentage:float=1.0,tasknr:int=0)->Tuple[np.array,np.array,np.array,np.array,int]:
    """Convert a scan from a pye57.e57.E57 file to a tuple of 4 arrays.\n

    Features:
        0. ['cartesianX', 'cartesianY', 'cartesianZ'] \n
        1. ['colorRed', 'colorGreen', 'colorBlue'] \n
        2. ['nor:normalX', 'nor:normalY', 'nor:normalZ']\n
        3. cartesianTransform (np.array)
        4. tasknr (int): int to retrieve order in multiprocessing

    Args:
        1. e57 (pye57.e57.E57) \n
        2. e57Index (int,optional): index of the scan. Typically found in e57.scan_count \n
        3. tasknr (int): int to retrieve order in multiprocessing

    Returns:
        Tuple[pointArray(np.array),colorArray(np.array),normalArray(np.array),cartesianTransform(np.array),tasknr(int)]
    """
    e57 = pye57.E57(e57Path)
    #get transformation
    header = e57.get_header(e57Index)
    cartesianTransform= e57_get_cartesianTransform(header)
    
    #get points    
    rawData = e57.read_scan_raw(e57Index)    
    if all(elem in header.point_fields  for elem in ['cartesianX', 'cartesianY', 'cartesianZ']):   
        pointArray=e57_get_xyz_from_raw_data(rawData)
    elif all(elem in header.point_fields  for elem in ['sphericalRange', 'sphericalAzimuth', 'sphericalElevation']):
        pointArray=e57_get_xyz_from_spherical_raw_data(rawData)

    #downnsample
    if percentage <1.0:
        indices=np.random.random_integers(0,len(pointArray)-1,int(len(pointArray)*percentage))
        pointArray=pointArray[indices]

    #get color or intensity
    colorArray=None
    if (all(elem in header.point_fields  for elem in ['colorRed', 'colorGreen', 'colorBlue'])
        or 'intensity' in header.point_fields ): 
        colorArray=e57_get_colors(rawData)
        if percentage <1.0:
            colorArray=colorArray[indices]

    #get normals
    normalArray=None
    if all(elem in header.point_fields  for elem in ['nor:normalX', 'nor:normalY', 'nor:normalZ']): 
        normalArray=e57_get_normals(rawData)
        if percentage <1.0:
            normalArray=normalArray[indices]

    return pointArray,colorArray,normalArray,cartesianTransform,tasknr

def e57path_to_pcd(e57Path:str , e57Index : int = 0,percentage:float=1.0) ->o3d.geometry.PointCloud:
    """Load an e57 file and convert the data to o3d.geometry.PointCloud.\n

    Args:
        e57path

    Raises:
        ValueError: Invalid e57Path.

    Returns:
        o3d.geometry.PointCloud
    """
    if not os.path.exists(e57Path):
        raise ValueError( 'Invalid e57Path.')
 
    e57 = pye57.E57(e57Path)
    pcd=e57_to_pcd(e57,e57Index,percentage)
    return pcd

def e57path_to_pcds_multiprocessing(e57Path:str,percentage:float=1.0) ->List[o3d.geometry.PointCloud]:
    """Load an e57 file and convert all data to a list of o3d.geometry.PointCloud objects.\n

    **NOTE**: Complex types cannot be pickled (serialized) by Windows. Therefore, a two step parsing is used where e57 data is first loaded as np.arrays with multi-processing.
    Next, the arrays are passed to o3d.geometry.PointClouds outside of the loop.\n  

    **NOTE**: starting parallel processing takes a bit of time. This method will start to outperform single-core import from 3+ pointclouds.\n

    Args:
        1. e57path(str): absolute path to .e57 file\n
        2. percentage(float,optional): percentage of points to load. Defaults to 1.0 (100%)\n

    Raises:
        ValueError: Invalid e57Path.

    Returns:
        o3d.geometry.PointCloud
    """   
    if not os.path.exists(e57Path):
        raise ValueError( 'Invalid e57Path.')
 
    e57 = pye57.E57(e57Path)
    pcds=[None]*e57.scan_count
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # first load all e57 data and output it as np.arrays
        results=[executor.submit(e57_to_arrays,e57Path=e57Path,e57Index=s,percentage=percentage,tasknr=s) for s in range(e57.scan_count)]
        # next, the arrays are assigned to point clouds outside the loop.
        for r in concurrent.futures.as_completed(results):
            tasknr=r.result()[-1]
            print(r.result()[-2])
            pcd=arrays_to_pcd(r.result())
            pcds[tasknr]=pcd
    return pcds

def box_to_mesh(box:o3d.geometry) ->o3d.geometry.TriangleMesh:
    """Returns o3d.geometry.TriangleMesh of OrientedBoundingBox or AxisAlignedBoundingBox. \n

    Args:
        box (o3d.geometry.OrientedBoundingBox or AxisAlignedBoundingBox)

    Returns:
        o3d.geometry.TriangleMesh
    """
    if type(box) is o3d.geometry.OrientedBoundingBox or type(box) is o3d.geometry.AxisAlignedBoundingBox:
        mesh=o3d.geometry.TriangleMesh()
        mesh.vertices=box.get_box_points()
        #triangles rotate counterclockwise
        mesh.triangles= o3d.cpu.pybind.utility.Vector3iVector(np.array([[0,2,1],
                            [0,1,3],
                            [0,3,2],
                            [1,6,3],
                            [1,7,6],
                            [1,2,7],
                            [2,3,5],
                            [2,5,4],
                            [2,4,7],
                            [3,4,5],
                            [3,6,4],
                            [4,6,7]])) 
        return mesh                  
    else:
        print('Incorrect geometry input. Only input o3d.geometry.AxisAlignedBoundingBox or o3d.geometry.OrientedBoundingBox or type(geometry)  ')
        return None 

def ifc_to_mesh(ifcElement:ifcopenshell.entity_instance)-> o3d.geometry.TriangleMesh: 
    """Convert an ifcOpenShell geometry to an Open3D TriangleMesh.\n

    Args:
        ifcElement (ifcopenshell.entity_instance): IfcOpenShell Element parsed from and .ifc file. See BIMNode for more documentation.

    Raises:
        ValueError: Geometry production error. This function throws an error if no geometry can be parsed for the ifcElement.  

    Returns:
        o3d.geometry.TriangleMesh: Open3D Mesh Geometry of the ifcElment boundary surface
    """    
    try:
        if ifcElement.get_info().get("Representation"): 
            # Set geometry settings and global coordinates as true
            settings = geom.settings() 
            settings.set(settings.USE_WORLD_COORDS, True) 
        
            # Extract vertices/faces of the IFC geometry
            shape = geom.create_shape(settings, ifcElement) 
            ifcVertices = shape.geometry.verts 
            ifcFaces = shape.geometry.faces 

            #Group the vertices and faces in a way they can be read by Open3D
            vertices = [[ifcVertices[i], ifcVertices[i + 1], ifcVertices[i + 2]] for i in range(0, len(ifcVertices), 3)]
            faces = [[ifcFaces[i], ifcFaces[i + 1], ifcFaces[i + 2]] for i in range(0, len(ifcFaces), 3)]

            #Convert grouped vertices/faces to Open3D objects 
            o3dVertices = o3d.utility.Vector3dVector(np.asarray(vertices))
            o3dTriangles = o3d.utility.Vector3iVector(np.asarray(faces))

            # Create the Open3D mesh object
            mesh=o3d.geometry.TriangleMesh(o3dVertices,o3dTriangles)
            if len(mesh.triangles)>1:
                return mesh
            else: 
                return None 
    except:
        print('Geometry production error')
        return None

def get_oriented_bounding_box(data) ->o3d.geometry.OrientedBoundingBox:
    """Get Open3DOrientedBoundingBox  from cartesianBounds or orientedBounds.

    Args:
        1. cartesianBounds (np.array): [xMin,xMax,yMin,yMax,zMin,zMax]\n
        2. orientedBounds (np.array): [8x3] bounding points\n

    Returns:
        o3d.geometry.OrientedBoundingBox
    """
    if type(data) is np.ndarray and len(data) ==6:
        points=get_oriented_bounds(data)
        box=o3d.geometry.OrientedBoundingBox.create_from_points(points)
        return box
    
    elif type(data) is np.ndarray and data.shape[1] == 3 and data.shape[0] > 2:
        points = o3d.utility.Vector3dVector(data)
        box = o3d.geometry.OrientedBoundingBox.create_from_points(points)
        return box
    else:
        raise ValueError("No valid data input (np.array [6x1] or [mx3])")

def generate_visual_cone_from_image(cartesianTransform : np.array, height : float=10.0, fov : float = math.pi/3) -> o3d.geometry.TriangleMesh:
    """Generate a conical mesh from the camera's center up to the height with a radius equal to the field of view.\n

    Args:
        1. cartesianTransform (np.array [◙4x4]): camera position\n
        2. height (float, optional): Height of the cone. Defaults to 10.0.\n
        3. fov (float, optional): angle from the top of the cone equal to the field-of-view of the . Defaults to math.pi/3.\n

    Raises:
        ValueError: The given cartesianTransform is not a 4x4 np.array

    Returns:
        o3d.geometry.TriangleMesh
    """
    radius=height*math.cos(fov)
    cone=o3d.geometry.TriangleMesh.create_cone(radius, height)
    if (cartesianTransform.size ==16):
        return cone.transform(cartesianTransform)
    else:
        raise ValueError("The given cartesianTransform is not a 4x4 np.array") 

def get_cartesian_transform(rotation: np.array= None, 
                            translation:  np.array=  None,
                            cartesianBounds:  np.array= None ) -> np.ndarray:
    """Return cartesianTransform from rotation, translation or cartesianBounds inputs.\n

    Args:
        1. rotation (np.array[3x3]) : rotation matrix\n
        2. translation (np.array[1x3]) : translation vector\n
        3. cartesianBounds (np.array[1x6]) : [xMin,xMax,yMin,yMax,zMin,zMax]\n

    Returns:
        cartesianTransform (np.array[4x4])
    """   
    r=np.diag(np.diag(np.ones((3,3))))
    t=np.zeros((3,1))
    c=np.zeros((6,1))

    if rotation is not None:
        if rotation.size==9:
            r=rotation
            r=np.reshape(r,(3, 3))
        else:
            raise ValueError("The rotation is not a 3x3 np.array")
    if translation is not None:
        if translation.size==3:
            t=translation
            t=np.reshape(t,(3, 1))  
        else:
            raise ValueError("The translation is not a 3x1 np.array")      
    elif cartesianBounds is not None:
        if cartesianBounds.size==6:
            t=get_translation(cartesianBounds)    
            t=np.reshape(t,(3, 1))
        else:
            raise ValueError("The cartesianBounds is not a 6x1 np.array")
    h= np.zeros((1,4))
    h[0,3]=1
    transform= np.concatenate((r,t),axis=1,dtype=float)
    transform= np.concatenate((transform,h),axis=0,dtype=float)
    return transform

def mesh_to_pcd(mesh:o3d.geometry.TriangleMesh,voxelSize : float = 0.1) -> o3d.geometry.PointCloud:
    """Sample a point cloud on a triangle mesh (Open3D).\n

    Args:
        1. mesh (o3d.geometry.TriangleMesh) : source geometry\n
        2. voxel_size (float) : spatial resolution of the point cloud e.g. 0.1m\n

    Returns:
        o3d.geometry.PointCloud
    """
    pcd = o3d.geometry.PointCloud()
    mesh=ut.item_to_list(mesh)
    for submesh in mesh:
        k = round(submesh.get_surface_area() * 1000)
        submeshpcd = submesh.sample_points_uniformly(number_of_points = k, use_triangle_normal=True)
        pcd.__iadd__(submeshpcd)
    pcd = pcd.voxel_down_sample(voxelSize)    
    return pcd

#### GEOMETRY GENERATION ####

def generate_virtual_images(geometries: List[o3d.geometry.Geometry],cartesianTransforms: List[np.array],width:int=640,height:int=480,f:float=400)-> o3d.geometry.Image:
    """Generate a set of Open3D Images from cartesianTransforms and geometries. \n
    The same intrinsic camera parameters are used for all cartesianTransforms that are passed to the function.\n

    .. image:: ../../../docs/pics/rendering3.PNG

    Args:
        1. geometries (List[o3d.geometry]):o3d.geometry.PointCloud or o3d.geometry.TriangleMesh \n
        2. cartesianTransforms (List[np.array 4x4]): [Rt] \n
        3. width (int, optional): image width in pix. Defaults to 640pix.\n
        4. height (int, optional): image height in pix. Defaults to 480pix. \n
        5. f (float, optional): focal length in pix. Defaults to 400pix. \n

    Returns:
        List[o3d.cpu.pybind.geometry.Image]
    """
    #set renderer
    render = o3d.visualization.rendering.OffscreenRenderer(width,height)
    mtl=o3d.visualization.rendering.MaterialRecord()
    mtl.base_color = [1.0, 1.0, 1.0, 1.0]  # RGBA
    mtl.shader = "defaultUnlit"

    # set internal camera orientation
    fx=f
    fy=f
    cx=width/2-0.5
    cy=width/2-0.5
    intrinsic=o3d.camera.PinholeCameraIntrinsic(width,height,fx,fy,cx,cy)
    
    #add geometries
    geometries=ut.item_to_list(geometries)
    for idx,geometry in enumerate(geometries):
        render.scene.add_geometry(str(idx),geometry,mtl) 

    #set cameras and generate images
    list=[]
    for cartesianTransform in cartesianTransforms:
        extrinsic=np.linalg.inv(cartesianTransform)
        render.setup_camera(intrinsic,extrinsic)
        img = render.render_to_image()
        list.append(img)

    if len(list) !=0:
        return list
    else:
        return None

def generate_virtual_image(geometries: List[o3d.geometry.Geometry],pinholeCamera: o3d.camera.PinholeCameraParameters)-> o3d.geometry.Image:
    """Generate an Open3D Image from a set of geometries and an Open3D camera. 

    Args:
        1. geometries (List[o3d.geometry]):o3d.geometry.PointCloud or o3d.geometry.TriangleMesh\n
        2. pinholeCamera (o3d.camera.PinholeCameraParameters): extrinsic (cartesianTransform) and intrinsic (width,height,f,principal point U and V) camera parameters\n

    Returns:
        o3d.cpu.pybind.geometry.Image or None
    """
    #create renderer
    width=pinholeCamera.intrinsic.width
    height=pinholeCamera.intrinsic.height
    render = o3d.visualization.rendering.OffscreenRenderer(width,height)

    # Define a simple unlit Material. (The base color does not replace the geometry colors)
    mtl=o3d.visualization.rendering.MaterialRecord()
    mtl.base_color = [1.0, 1.0, 1.0, 1.0]  # RGBA
    mtl.shader = "defaultUnlit"

    #set camera
    render.setup_camera(pinholeCamera.intrinsic,pinholeCamera.extrinsic)
    #add geometries
    geometries=ut.item_to_list(geometries)
    for idx,geometry in enumerate(geometries):
        render.scene.add_geometry(str(idx),geometry,mtl) 
    #render image
    img = render.render_to_image()
    if img is not None:
        return img
    else:
        return None

#### GEOMETRY MANIPULATION ####
def e57_get_normals(rawData:dict)->np.array:
    """Returns normal vectors from e57 rawData.

    Args:
        rawData (dict): e57 dictionary resulting from e57.read_scan_raw(e57Index)\n

    Returns:
         np.array(nx3): magnitude 1
    """
    
    nx=rawData.get('nor:normalX')
    ny=rawData.get('nor:normalY')
    nz=rawData.get('nor:normalZ')
    return np.reshape(np.vstack(( nx,ny,nz)).flatten('F'),(len(nx),3))
    
def e57_get_colors(rawData: dict)->np.array:
    """Extract color of intensity information from e57 raw data (3D data) and output Open3D o3d.utility.Vector3dVector(colors).\n

    Args:
        rawData(dict): e57 dictionary resulting from e57.read_scan_raw(e57Index)\n
    
    Returns:
        np.array(nx3): RGB or intensity color information. RGB is prioritised.
    """   
    try:
        colorRed=rawData.get('colorRed')
        colorGreen=rawData.get('colorGreen')
        colorBlue=rawData.get('colorBlue')
        intensity=rawData.get('intensity')

        if colorRed is not None and colorGreen is not None and colorBlue is not None:
            if np.amax(colorRed)<=1:
                colors=np.c_[colorRed , colorGreen,colorBlue ]  
            elif np.amax(colorRed) <=255:
                colors=np.c_[colorRed/255 , colorGreen/255,colorBlue/255 ]  
            else:
                colorRed=(colorRed - np.min(colorRed))/np.ptp(colorRed)
                colorGreen=(colorGreen - np.min(colorGreen))/np.ptp(colorGreen)
                colorBlue=(colorBlue - np.min(colorBlue))/np.ptp(colorBlue)
                colors=np.c_[colorRed , colorGreen,colorBlue ]  
            return np.reshape(colors.flatten('F'),(len(colorRed),3))

        elif intensity is not None:
            if np.amax(intensity) <=1:
                colors=np.c_[intensity , intensity,intensity ]  
            else:
                intensity=(intensity - np.min(intensity))/np.ptp(intensity)
                colors=np.c_[intensity , intensity,intensity ]  
            return np.reshape(colors.flatten('F'),(len(intensity),3))
    except:
        return None
    return None

def e57_fix_rotation_order(rotation_matrix:np.array) -> np.array:
    """Switch the rotation from clockwise to counter-clockwise in e57 rotation matrix. See following url for more information:\n

    https://robotics.stackexchange.com/questions/10702/rotation-matrix-sign-convention-confusion\n
    
    Currently only changes the signs of elements [0,1,5,8].\n

    Args:
        rotation_matrix(np.array(3x3))
    
    Returns:
        transformed rotation_matrix(np.array(3x3))
    """
    r=rotation_matrix
    return np.array([[-r[0,0],-r[0,1],r[0,2]],
                    [r[1,0],r[1,1],-r[1,2]],
                    [r[2,0],r[2,1],-r[2,2]]])

def evaluate_feature(pcd0, pcd1, feat0, feat1, trans_gth, search_voxel_size):
    """ TO BE EVALUATED"""
    match_inds = get_matching_indices(pcd0, pcd1, trans_gth, search_voxel_size)
    pcd_tree = o3d.geometry.KDTreeFlann(feat1)
    dist = []
    for ind in match_inds:
        k, idx, _ = pcd_tree.search_knn_vector_xd(feat0.data[:, ind[0]], 1)
        dist.append(
            np.clip(
                np.power(pcd1.points[ind[1]] - pcd1.points[idx[0]], 2),
                a_min=0.0,
                a_max=1.0))
    return np.mean(dist)

def get_matching_indices(source, target, trans, search_voxel_size, K=None):
    """ TO BE EVALUATED"""

    source_copy = copy.deepcopy(source)
    target_copy = copy.deepcopy(target)
    source_copy.transform(trans)
    pcd_tree = o3d.geometry.KDTreeFlann(target_copy)

    match_inds = []
    for i, point in enumerate(source_copy.points):
        [_, idx, _] = pcd_tree.search_radius_vector_3d(point, search_voxel_size)
        if K is not None:
            idx = idx[:K]
        for j in idx:
            match_inds.append((i, j))
    return match_inds

# def get_correspondences(src_pcd, tgt_pcd, trans, search_voxel_size, K=None):
#     src_pcd.transform(trans)
#     pcd_tree = o3d.geometry.KDTreeFlann(tgt_pcd)

#     correspondences = []
#     for i, point in enumerate(src_pcd.points):
#         [count, idx, _] = pcd_tree.search_radius_vector_3d(point, search_voxel_size)
#         if K is not None:
#             idx = idx[:K]
#         for j in idx:
#             correspondences.append([i, j])
    
#     correspondences = np.array(correspondences)
#     correspondences = torch.from_numpy(correspondences)
#     return correspondences

def crop_geometry_by_box(geometry:o3d.geometry, box:o3d.geometry.OrientedBoundingBox, subdivide:int = 0) ->o3d.geometry:
    """Crop portion of a mesh/pointcloud that lies within an OrientedBoundingBox.

    .. image:: ../../../docs/pics/selection_BB_mesh2.PNG

    Args:
        1. geometry (o3d.geometry.TriangleMesh or o3d.geometry.PointCloud): Geometry to be cropped\n
        2. box (o3d.geometry.OrientedBoundingBox): bouding cutter geometry\n
        3. subdivide (int): number of interations to increase the density of the mesh (1=x4, 2=x16, etc.)\n
        
    Returns:
        o3d.geometry.TriangleMesh or None
    """
    # transform box to axis aligned box 
    r=box.R
    t=box.center
    transformedbox=copy.deepcopy(box)
    transformedbox=transformedbox.translate(-t)
    transformedbox=transformedbox.rotate(r.transpose(),center=(0, 0, 0))
    
    # transform geometry to coordinate system of the box
    transformedGeometry=copy.deepcopy(geometry)
    transformedGeometry=transformedGeometry.translate(-t)
    transformedGeometry=transformedGeometry.rotate(r.transpose(),center=(0, 0, 0))

    # convert to pcd if geometry is a mesh (crop fails with mesh geometry)
    if type(geometry) is o3d.geometry.PointCloud:
        croppedGeometry=transformedGeometry.crop(transformedbox)             
    elif type(geometry) is o3d.geometry.TriangleMesh:
        if subdivide!=0:
            transformedGeometry=transformedGeometry.subdivide_midpoint(subdivide)
        indices=transformedbox.get_point_indices_within_bounding_box(transformedGeometry.vertices) # this is empty
        if len(indices) !=0:
            croppedGeometry=transformedGeometry.select_by_index(indices,cleanup=True)
        else:
            return None

    # return croppedGeometry to original position
    if croppedGeometry is not None:
        croppedGeometry=croppedGeometry.rotate(r,center=(0, 0, 0))
        croppedGeometry=croppedGeometry.translate(t)
        return croppedGeometry
    else:
        return None

def expand_box (box: o3d.geometry.OrientedBoundingBox, u=5.0,v=5.0,w=5.0) -> o3d.geometry.OrientedBoundingBox:
    """expand an o3d.geometry.OrientedBoundingBox in u(x), v(y) and w(z) direction with a certain offset.

    Args:
        1. box (o3d.geometry.OrientedBoundingBox)\n
        2. u (float, optional): Offset in X. Defaults to 5.0.\n
        3. v (float, optional): Offset in Y. Defaults to 5.0.\n
        4. w (float, optional): Offset in Z. Defaults to 5.0.\n

    Returns:
        o3d.geometry.OrientedBoundingBox
    """    
    if 'OrientedBoundingBox' not in str(type(box)):
        raise ValueError('Only OrientedBoundingBox allowed.' )
    if (u<0 and abs(u)>= box.extent[0]) or (v<0 and abs(v)>=box.extent[1]) or (w<0 and abs(w)>=box.extent[2]):
        raise ValueError("can't schrink more than the extent of the box")

    center = box.get_center()
    orientation = box.R 
    extent = box.extent + [u,v,w] 
    return o3d.geometry.OrientedBoundingBox(center,orientation,extent) 

def join_geometries(geometries) ->o3d.geometry:
    """Join a number of o3d.PointCloud or o3d.TriangleMesh instances.\n

    **NOTE**: Only members of the same geometryType can be merged.\n

    Args:
        geometries (o3d.PointCloud or TriangleMesh)

    Returns:
        merged o3d.geometry (o3d.PointCloud or TriangleMesh)
    """
    geometries=ut.item_to_list(geometries)
    if any('TriangleMesh' in str(type(g)) for g in geometries ):
        joined=o3d.geometry.TriangleMesh()
        for geometry in geometries:
            if geometry is not None and len(geometry.vertices) != 0:
                joined +=geometry
        return joined
    if any('PointCloud' in str(type(g)) for g in geometries ):
        joined=o3d.geometry.PointCloud()
        for geometry in geometries:
            if geometry is not None and len(geometry.points) != 0:
                joined +=geometry
        return joined
    else:
        raise ValueError('Only submit o3d.geometry.TriangleMesh or o3d.geometry.PointCloud objects') 

def create_visible_point_cloud_from_meshes (geometries: List[o3d.geometry.TriangleMesh], 
                                            references:List[o3d.geometry.TriangleMesh], 
                                            resolution:float = 0.1,
                                            getNormals:Boolean=False)-> Tuple[List[o3d.geometry.PointCloud], List[float]]:
    """Returns a set of point clouds sampled on the geometries. Each point cloud has its points filtered to not lie wihtin or collide with any of the reference geometries. As such, this method returns the **visible** parts of a set of sampled point clouds. \n
    
    For every point cloud, the percentage of visibility is also reported. This method takes about 50s for 1000 geometries. \n
    \n
    E.g. The figure shows the points of the visible point cloud that were rejected due to their proximity to the other mesh geometries.

    .. image:: ../../../docs/pics/invisible_points.PNG

    Args:
        1. geometries (List[o3d.geometry.TriangleMesh]): Meshes that will be sampled up to the resolution. \n
        2. references (List[o3d.geometry.TriangleMesh]): reference meshes that are used to spatially filter the sampled point clouds so only 'visible' points are retained. If some targget \n
        3. resolution (float, optional): Spatial resolution to sample meshes. Defaults to 0.1m. \n

    Raises:
        ValueError: any('TriangleMesh' not in str(type(g)) for g in geometries )\n
        ValueError: any('TriangleMesh' not in str(type(g)) for g in references )\n

    Returns:
        Tuple[List[o3d.geometry.PointCloud], List[percentages [0-1.0]]] per geometry
    """
    geometries=ut.item_to_list(geometries)    
    references=ut.item_to_list(references)    

    #validate geometries
    if  any('TriangleMesh' not in str(type(g)) for g in geometries ):
        raise ValueError('Only submit o3d.geometry.TriangleMesh objects') 
    #validate geometries
    if  any('TriangleMesh' not in str(type(g)) for g in references ):
        raise ValueError('Only submit o3d.geometry.TriangleMesh objects') 

    colorArray=np.random.random((len(geometries),3))
    identityPointClouds=[]
    percentages=[]
    # percentages=np.full((len(pcd.points), 1), 1.0)

    for i,geometry in enumerate(geometries):        
        
        # create a reference scene 
        referenceGeometries=[g for g in references if g !=geometry ]
        reference=join_geometries(referenceGeometries)
        scene = o3d.t.geometry.RaycastingScene()
        cpuReference = o3d.t.geometry.TriangleMesh.from_legacy(reference)
        _ = scene.add_triangles(cpuReference)

        # sample mesh (optional with normals)
        if getNormals and not geometry.has_triangle_normals():
            geometry.compute_triangle_normals()
        area=geometry.get_surface_area()
        count=int(area/(resolution*resolution))
        pcd=geometry.sample_points_uniformly(number_of_points=10*count,use_triangle_normal=getNormals)
        pcd=pcd.voxel_down_sample(resolution)

        # determine visibility from distance and occupancy querries
        query_points = o3d.core.Tensor(np.asarray(pcd.points), dtype=o3d.core.Dtype.Float32)
        unsigned_distance = scene.compute_distance(query_points)
        occupancy = scene.compute_occupancy(query_points)
        indices=np.where((unsigned_distance.numpy() >=0.5*resolution) & (occupancy.numpy() ==0) )[0]     

        # crop sampled point cloud to only the visible points
        pcdCropped = pcd.select_by_index(indices)
        pcdCropped.paint_uniform_color(colorArray[i])
        identityPointClouds.append(pcdCropped)

        #report percentage
        percentages.append((len(pcdCropped.points)/len(pcd.points)))

    return identityPointClouds, percentages

def create_identity_point_cloud(geometries: o3d.geometry.PointCloud, resolution:float = 0.1) -> Tuple[o3d.geometry.PointCloud, np.array]:
    """Returns a sampled point cloud colorized per object of a set of objects along with an array with an identifier for each point.

    Args:
        1.geometries (o3d.geometry.PointCloud or o3d.geometry.TriangleMesh) \n
        2.resolution (float, optional): (down)sampling resolution for the point cloud. Defaults to 0.1.\n

    Raises:
        ValueError: Geometries must be o3d.geometry (PointCloud or TriangleMesh)

    Returns:
        Tuple[colorized point cloud (o3d.geometry.PointCloud), identityArray(np.array)] per geometry
    """
    geometries=ut.item_to_list(geometries)    
    colorArray=np.random.random((len(geometries),3))
    indentityArray=None
    identityPointCloud=o3d.geometry.PointCloud()

    for i,geometry in enumerate(geometries):
        if 'PointCloud' in str(type(geometry)) :
            pcd=geometry.voxel_down_sample(resolution)
            indentityArray=np.vstack((indentityArray,np.full((len(pcd.points), 1), i)))
            pcd.paint_uniform_color(colorArray[i])
            identityPointCloud +=pcd
            # np.concatenate((np.asarray(identityPointCloud.points),np.asarray(identityPointCloud.points)),axis=0)
        elif 'TriangleMesh' in str(type(geometry)):
            area=geometry.get_surface_area()
            count=int(area/(resolution*resolution))
            pcd=geometry.sample_points_uniformly(number_of_points=10*count)
            pcd=pcd.voxel_down_sample(resolution)
            indentityArray=np.vstack((indentityArray,np.full((len(pcd.points), 1), i)))
            pcd.paint_uniform_color(colorArray[i])
            identityPointCloud +=pcd
        else:
            print(f'{geometry} is invalid')
            continue
            # raise ValueError('Geometries must be o3d.geometry (PointCloud or TriangleMesh)')    
    indentityArray=indentityArray.flatten()
    indentityArray=np.delete(indentityArray,0)
    return identityPointCloud, indentityArray

def determine_observable_point_cloud(pointcloud:o3d.geometry.PointCloud, resolution:float = 0.1,indentityArray:np.ndarray=None )-> Tuple[o3d.geometry.PointCloud, np.array]:
    """THIS FUNCTION DOESNT MAKE SENSE

    """
    return None
#     #crop point cloud
#     dists = np.asarray(pointcloud.compute_point_cloud_distance(pointcloud))
#     indices = np.where((dists < resolution) and (dists >0.001))[0]
#     pcdCropped = pointcloud.select_by_index(indices)

#     if indentityArray:
#         #compute percentages based on occurences
#         unique0, counts0 = np.unique(indentityArray, return_counts=True)
#         percentages=np.full((len(unique0), 1), 1)
#         arrayCropped=indentityArray[list(indices)]
#         unique1, counts1 = np.unique(arrayCropped, return_counts=True)
#         for u in unique1:
#             percentages[u]=counts1[u]/counts0[u]
#     else:
#         percentages=None
#     return pcdCropped, percentages

def determine_percentage_of_coverage(sources: List[o3d.geometry.TriangleMesh], reference:o3d.geometry.PointCloud,threshold:float=0.1)-> np.array:
    """Returns the Percentage-of-Coverage (PoC) of every source geometry when compared to a reference geometry. The PoC is defined as the ratio of points on the boundary surface of the source that lie within a Euclidean distance threshold hold of the reference geometry. sampled point cloud on the boundary surface of the sources with a resolution of e.g. 0.1m. \n

    .. math::
        P_{i'}=\{ p|\forall p \in P_i : p_i \cap N\backslash  n_i \} 
        c_i = \frac{|P_{i'}|}{|P_i|}
    
    E.g. a mesh of a beam of which half the surface lies within 0.1m of a point cloud will have a PoC of 0.5.
    
    Args:
        1. sources (o3d.geometry.TriangleMesh/PointCloud): geometries to determine the PoC for. \n
        2. reference (o3d.geometry.PointCloud): reference geometry for the Euclidean distance calculations.\n
        3. threshold (float, optional): sampling resolution of the boundary surface of the source geometries. Defaults to 0.1m.\n

    Raises:
        ValueError: Sources must be o3d.geometry (PointCloud or TriangleMesh)

    Returns:
        List[percentages[0-1.0]] per source
    """
    #if no list, list
    sources=ut.item_to_list(sources)
    sourcePCDs=[]
    indentityArray=None
    percentages=[0.0]*len(sources)

    # check whether source and reference are close together to minize calculations
    ind=get_box_inliers(reference.get_oriented_bounding_box(), [geometry.get_oriented_bounding_box() for geometry in sources])
    if not ind:
        return percentages
    # inliersSources=[sources[i] for i in ind] 

    # sample o3d.geometry and create identitylist so to track the indices.
    for i,source in enumerate(sources):  
        if i in ind:      
            if 'PointCloud' in str(type(source)) :
                sourcePCD=source.voxel_down_sample(threshold)
                indentityArray=np.vstack((indentityArray,np.full((len(sourcePCD.points), 1), i)))
            elif 'TriangleMesh' in str(type(source)):
                area=source.get_surface_area()
                count=int(area/(threshold*threshold))
                sourcePCD=source.sample_points_uniformly(number_of_points=count)
                indentityArray=np.vstack((indentityArray,np.full((len(sourcePCD.points), 1), i)))
            sourcePCDs.append(sourcePCD)
        else:
            sourcePCDs.append(None)

    indentityArray=indentityArray.flatten()
    indentityArray=np.delete(indentityArray,0)

    #compute distances
    joinedPCD=join_geometries(sourcePCDs)
    distances=joinedPCD.compute_point_cloud_distance(reference)

    #remove distances > threshold
    ind=np.where(np.asarray(distances) <= threshold)[0]
    if ind.size ==0:
        return percentages
    indexArray=[indentityArray[i] for i in ind.tolist()]

    # count occurences
    unique_elements, counts_elements = np.unique(indexArray, return_counts=True)
    for i,n in enumerate(unique_elements):
        percentages[n]=counts_elements[i]/len(sourcePCDs[n].points)

    return percentages

def crop_geometry_by_distance(source: o3d.geometry, cutters, threshold : float =0.10) -> o3d.geometry.PointCloud:
    """Returns the portion of a pointcloud that lies within a range of another mesh/point cloud.\n
    
    .. image:: ../../../docs/pics/crop_by_distance2.PNG

    Args:
        1. source (o3d.geometry.TriangleMesh or o3d.geometry.PointCloud) : point cloud to filter \n
        2. cutters (o3d.geometry.TriangleMesh or o3d.geometry.PointCloud): list of reference data \n
        3. threshold (float, optional): threshold Euclidean distance for the filtering \n

    Returns:
        o3d.geometry (TriangleMesh or PointCloud)
    """
    #if no list, list
    cutters=ut.item_to_list(cutters)
    joined=join_geometries(cutters)

    #Check treshold
    if threshold <0:
        raise ValueError('No values below 0 allowed.')

    #Check cutters
    if  type(joined) is o3d.cpu.pybind.geometry.TriangleMesh:
        reference=joined.sample_points_uniformly(number_of_points=1000000) 
    elif type(joined) is o3d.geometry.PointCloud:
        reference=joined
    else:
        print(type(cutters[0]) + ' is not a suitable input. Please only submit o3d.PointCloud or TriangleMesh')
        return None

    #check source
    if type(source) is o3d.cpu.pybind.geometry.TriangleMesh :
        #convert to pcd
        pcdMesh=o3d.geometry.PointCloud()
        vertices=(np.asarray(source.vertices))
        pcdMesh.points=o3d.utility.Vector3dVector(vertices)

        #compute distance
        distances=pcdMesh.compute_point_cloud_distance(reference)

        #remove vertices > threshold
        ind=np.where(np.asarray(distances) <= threshold)[0]
        if ind.size >0:
            return source.select_by_index(ind, cleanup=True)   
        else:
            return None 
    elif type(source) is o3d.geometry.PointCloud :
        dists=source.compute_point_cloud_distance(reference) #10s to calculate
        dists = np.asarray(dists)
        ind=np.where(dists <= threshold)[0]
        if ind.size >0:
           return source.select_by_index(ind)
        else:
            return None 
    else:
        print(type(source) + ' is not a suitable input. Please only submit o3d.PointCloud or TriangleMesh')
        return None

#### GEOMETRY PROPERTIES

def get_box_inliers(sourceBox:o3d.geometry.OrientedBoundingBox, testBoxes: List[o3d.geometry.OrientedBoundingBox],t_d:float=0.5)->List[int]:
    """Return the indices of the testBoxes of which the bounding points lie within the sourceBox.\n

    .. image:: ../../../docs/pics/get_box_inliers1.PNG

    Args:
        1. sourceBox (o3d.geometry.OrientedBoundingBox):   box to test \n
        2. testBoxes (o3d.geometry.OrientedBoundingBox):   boxes to test \n
    Returns:
        list (List[int]):       indices of testBoxes \n

    """
    #Convert to list
    sourceBox=expand_box(sourceBox,u=t_d,v=t_d,w=t_d)
    testBoxes=ut.item_to_list(testBoxes) 
    array= [False] * len(testBoxes)
    for idx,testbox in enumerate(testBoxes):
        if testbox is not None:
            points=testbox.get_box_points()
            indices=sourceBox.get_point_indices_within_bounding_box(points)        
            if len(indices) !=0:
                array[idx]= True
    list = [ i for i in range(len(array)) if array[i]]
    return list

def get_mesh_inliers(sources:List[o3d.geometry.TriangleMesh], reference:o3d.geometry.TriangleMesh) -> List[int]:
    """Returns the indices of the geometries that lie within a reference geometry. The watertightness of both source and reference geometries is determined after which the occupancy is computed for a numer of sampled points in the source geometries. \n

    .. image:: ../../../docs/pics/selection_BB_mesh5.PNG
    
    Args:
        1. sources (o3d.geometry.TriangleMesh/PointCloud): geometries to test for collision\n
        2. reference (o3d.geometry): reference geometry \n

    Raises:
        ValueError: Only TriangleMesh and PointCloud allowed

    Returns:
        List[int]: Indices of the inlier geometries
    """    
    sources=ut.item_to_list(sources)
    inliers=[None]*len(sources)

    test=str(type(reference))
    #validate reference
    if ('TriangleMesh' in str(type(reference)) and 
        len(reference.triangles)>=2 and
        reference.is_watertight()):    
        pass
    elif 'TriangleMesh' in str(type(reference)) and len(reference.triangles)>=2:
        reference,_=reference.compute_convex_hull()
    elif ('PointCloud' in str(type(reference)) and len(reference.points)>=3):
        reference,_=reference.compute_convex_hull()
    else: 
        raise ValueError('Only TriangleMesh and PointCloud allowed')
    #add reference to scene
    scene = o3d.t.geometry.RaycastingScene()
    reference = o3d.t.geometry.TriangleMesh.from_legacy(reference)
    _ = scene.add_triangles(reference)

    for i,s in enumerate(sources):
        #validate sources
        if ('TriangleMesh' in str(type(s)) and 
            len(s.triangles)>=2 and
            s.is_watertight()): 
            pass
        elif 'TriangleMesh' in str(type(s)) and len(s.triangles)>=2:
            s,_=sources[i].compute_convex_hull()
        elif ('PointCloud' in str(type(reference)) and len(reference.points)>=3):
            s,_=sources[i].compute_convex_hull()
        else:
            continue
        
        #sample geometries
        pcd=s.sample_points_uniformly(10)
        query_points = o3d.core.Tensor(np.asarray(pcd.points), dtype=o3d.core.Dtype.Float32)
        occupancy = scene.compute_occupancy(query_points)
        if np.any(occupancy.numpy()):
            inliers[i]=True
            continue
        inliers[i]=False
    
    #select indices    
    ind=np.where(np.asarray(inliers) ==True)[0]     
    return ind

def get_box_intersections(sourceBox:o3d.geometry.OrientedBoundingBox, testBoxes: List[o3d.geometry.OrientedBoundingBox])->List[int]:
    """Return indices of testBoxes of which the geometry intersects with the sourceBox.\n
    2 oriented bounding boxes (A,B) overlap if the projection from B in the coordinate system of A on all the axes overlap. \n
    The projection of B on the oriented axes of A is simply the coordinate range for that axis.\n

    .. image:: ../../../docs/pics/get_box_inliers1.PNG

    Args:
        1. sourceBox (o3d.geometry.OrientedBoundingBox):   box to test\n
        2. testBoxes (o3d.geometry.OrientedBoundingBox):   boxes to test\n

    Returns:
        list (List[int]):       indices of testBoxes
    """       
    #convert to list
    testBoxes=ut.item_to_list(testBoxes)

    array= [False] * len(testBoxes)

    for idx,testbox in enumerate(testBoxes):
    # compute axes of box A
        if testbox is not None:
            #transform box to aligned coordinate system
            transformedboxA=copy.deepcopy(sourceBox)
            transformedboxA=transformedboxA.translate(-sourceBox.center)
            transformedboxA=transformedboxA.rotate(sourceBox.R.transpose(),center=(0, 0, 0))
            
            #transform testbox to aligned coordinate system
            transformedboxB=copy.deepcopy(testbox)
            transformedboxB=transformedboxB.translate(-sourceBox.center)
            transformedboxB=transformedboxB.rotate(sourceBox.R.transpose(),center=(0, 0, 0))

            # compute coordinates of bounding points of B in coordinate system of A
            minA=transformedboxA.get_min_bound()
            minB=transformedboxB.get_min_bound()
            maxA=transformedboxA.get_max_bound()
            maxB=transformedboxB.get_max_bound()

            if (maxB[0]>=minA[0] and minB[0]<=maxA[0]):
                if (maxB[1]>=minA[1] and minB[1]<=maxA[1]):
                    if (maxB[2]>=minA[2] and minB[2]<=maxA[2]):
                        array[idx]= True  
    # return index if B overlaps with A in all three axes u,v,w 
    list = [ i for i in range(len(array)) if array[i]]
    return list

def get_triangles_center(mesh:o3d.geometry.TriangleMesh,triangleIndices: List[int]=None) -> np.array:
    """Get the centerpoints of a set of mesh triangles.\n

    Args:
        1. mesh (o3d.geometry.TriangleMesh)\n
        2. triangleIndices (List[int], optional): Indices to evaluate. Defaults to all triangles\n

    Raises:
        ValueError: len(triangleIndices)>len(mesh.triangles)\n
        ValueError: all(x > len(mesh.triangles) for x in triangleIndices)\n

    Returns:
        np.array[nx3] XYZ centers of triangles
    """
    #validate inputs
    if not triangleIndices:
        triangleIndices=range(0,len(mesh.triangles))
    if len(triangleIndices)>len(mesh.triangles):
        raise ValueError("len(triangleIndices)>len(mesh.triangles)")
    if all(x > len(mesh.triangles) for x in triangleIndices):
        raise ValueError("all(x > len(mesh.triangles) for x in triangleIndices)")

    triangles=np.asarray([triangle for idx,triangle in enumerate(mesh.triangles) if idx in triangleIndices])
    centers=np.empty((len(triangles),3))
    for idx,row in enumerate(triangles):
        points=np.array([mesh.vertices[row[0]],
                    mesh.vertices[row[1]],
                    mesh.vertices[row[2]]])
        centers[idx]=np.mean(points,axis=0)
    return centers

def get_cartesian_bounds(geometry : o3d.geometry) ->np.array:
    """Get cartesian bounds from Open3D geometry.\n

    Args:
        geometry (o3d.geometry): Open3D geometry supertype (PointCloud, TriangleMesh, OrientedBoundingBox, etc.)\n

    Returns:
        np.array: [xMin,xMax,yMin,yMax,zMin,zMax]
    """
    max=geometry.get_max_bound()
    min=geometry.get_min_bound()
    return np.array([min[0],max[0],min[1],max[1],min[2],max[2]])

def get_translation(data)-> np.array:
    """Get translation vector from various inputs.\n

    Args:
        0. cartesianTransform (np.array [4x4])\n
        1. cartesianBounds (np.array[6x1])\n
        2. orientedBounds(np.array[8x3])\n
        3. Open3D geometry\n

    Raises:
        ValueError: data.size !=6 (cartesianBounds), data.shape[1] !=3 (orientedBounds), data.size !=16 (cartesianTransform) or type != Open3D.geometry

    Returns:
        np.array[3x1]
    """
    if data.size ==6: #cartesianBounds
        x=(data[1]+data[0])/2
        y=(data[3]+data[2])/2
        z=(data[5]+data[4])/2
        return np.array([x,y,z])
    elif data.shape[1] ==3:   #orientedBounds
        return np.mean(data,axis=0)
    elif data.size ==16: #cartesianTransform
        return data[0:3,3]
    elif 'Open3D' in str(type(data)): #Open3D geometry
        return data.get_center()
    else:
        raise ValueError(" data.size !=6 (cartesianBounds), data.shape[1] !=3 (orientedBounds), data.size !=16 (cartesianTransform) or type != Open3D.geometry")

def get_oriented_bounds(cartesianBounds:np.array) -> List[o3d.utility.Vector3dVector]:
    """Get 8 bounding box from cartesianBounds.\n

    Args:
        cartesianBounds (np.array[6x1])

    Returns:
        List[o3d.utility.Vector3dVector]
    """    
    array=np.empty((8,3))
    xMin=cartesianBounds[0]
    xMax=cartesianBounds[1]
    yMin=cartesianBounds[2]
    yMax=cartesianBounds[3]
    zMin=cartesianBounds[4]
    zMax=cartesianBounds[5]

    #same order as Open3D
    array[0]=np.array([xMin,yMin,zMin])
    array[1]=np.array([xMax,yMin,zMin])
    array[2]=np.array([xMin,yMax,zMin])
    array[3]=np.array([xMin,yMin,zMax])
    array[4]=np.array([xMax,yMax,zMax])
    array[5]=np.array([xMin,yMax,zMax])
    array[6]=np.array([xMax,yMin,zMax])
    array[7]=np.array([xMax,yMax,zMin])

    return o3d.utility.Vector3dVector(array)
    
def get_rotation_matrix(data:np.array) -> np.array:
    """Get rotation matrix from one of the following inputs.\n

    Args:
        1. cartesianTransform (np.array [4x4])\n
        2. Euler angles (np.array[3x1]): yaw, pitch, roll  (in degrees)\n
        3. quaternion (np.array[4x1]): w,x,y,z\n
        4. orientedBounds(np.array[8x3])\n

    Returns:
        rotationMatrix (np.array[3x3])
    """  
    if data.size ==16:
        return data[0:3,0:3]

    elif data.size == 4:
        r = R.from_quat(data)
        return r.as_matrix()

    elif data.size ==3:
        r = R.from_euler('zyx',data,degrees=True)
        return r.as_matrix()
    elif data.size == 24:
        boxPointsVector = o3d.utility.Vector3dVector(data)
        open3dOrientedBoundingBox = o3d.geometry.OrientedBoundingBox.create_from_points(boxPointsVector)
        return np.asarray(open3dOrientedBoundingBox.R)    
    else:
        raise ValueError('No suitable input array found')

#### GEOMETRY TESTING ####

def get_mesh_collisions_open3d(sourceMesh: o3d.geometry.TriangleMesh, meshes: List[o3d.geometry.TriangleMesh], t_d:float=0.5) -> List[int]:
    """Return the index of the geometries that collide the sourceMesh
        NOT IMPLEMENTED
    """
    meshes=ut.item_to_list(meshes)
    if len(sourceMesh.triangles) !=0:
        # select those faces that are within proximity of each other
        box=sourceMesh.get_oriented_bounding_box()
        expand_box(box,u=t_d,v=t_d,w=t_d)

        boxes=np.empty(len(meshes),dtype=o3d.geometry.OrientedBoundingBox)
        for idx,mesh in enumerate(meshes):
            referenceBox=mesh.get_oriented_bounding_box()

            # crop both meshes based on the expanded bounding box
            croppedReferenceMesh=crop_geometry_by_box(mesh,box).triangles
            croppedSourceMesh=crop_geometry_by_box(sourceMesh,referenceBox).triangles

            # check if reference edges intersect with sourcemesh faces
            croppedReferenceMesh.edges

                # get all edges of refernence and traingles of source

                # compute mathmetical point of intersection between the lines and each plane

                # check if barymetric coordinates of intersection point lie within the triangle => if so, there is a collision#  
                # # if Mesh
                # # find vertices
                # mesh=o3d.geometry.TriangleMesh()
                # mesh.vertices 


                # mesh.remove_vertices_by_index()
                # mesh.remove_triangles_by_index()
                # points=mesh.vertices
                # faces=mesh.triangles
                # mesh.merge_close_vertices(0.01)
                # mesh.remove_duplicated_vertices()
                # triangle_mask=False*len(mesh.triangles)
                # cleanedMesh=mesh.remove_triangles_by_mask(triangle_mask)
                # mesh.remove_unreferenced_vertices()

                # CleanedMesh=mesh.select_by_index(indices,cleanup=True)
                # smoothMesh=mesh.subdivide_midpoint(1)
        return False

def crop_geometry_by_raycasting(source:o3d.geometry.TriangleMesh, cutter: o3d.geometry.TriangleMesh, inside : Boolean = True,strict : Boolean = True ) -> o3d.geometry.TriangleMesh:
    """Select portion of a mesh that lies within a mesh shape (if not closed, convexhull is called).\n
    
    inside=True
    .. image:: ../../../docs/pics/crop_by_ray_casting1.PNG

    inside=False 
    .. image:: ../../../docs/pics/crop_by_ray_casting2.PNG

    Args:
        1. source (o3d.geometry.TriangleMesh) : mesh to cut \n
        2. cutter (o3d.geometry.TriangleMesh) : mesh that cuts \n
        3. inside (bool): 'True' to retain inside. 'False' to retain outside \n
        4. strict (bool): 'True' if no face vertex is allowed outside the bounds, 'False' allows 1 vertex to lie outside \n

    Returns:
        outputmesh(o3d.geometry.TriangleMesh)
    """
    #check if cutter is closed 
    if not cutter.is_watertight():
        cutter=cutter.compute_convex_hull()

    #check if mesh has normals? not needed

    #raycast the scene to determine which points are inside
    query_points=o3d.core.Tensor(np.asarray(source.vertices),dtype=o3d.core.Dtype.Float32 )
    cpuMesh = o3d.t.geometry.TriangleMesh.from_legacy(cutter)
    scene = o3d.t.geometry.RaycastingScene()
    geometry = scene.add_triangles(cpuMesh)
    ans=scene.compute_occupancy(query_points)
    
    if inside:
        occupancyList=ans==0
    else:
        occupancyList=ans>0

    outputmesh=copy.deepcopy(source)
    if strict:
        outputmesh.remove_vertices_by_mask(occupancyList)
        outputmesh.remove_degenerate_triangles()
        outputmesh.remove_unreferenced_vertices
    else:
        triangles=copy.deepcopy(np.asarray(outputmesh.triangles)) #can we remove this one?
        indices= [i for i, x in enumerate(occupancyList) if x == True]
        #mark all unwanted points as -1
        triangles[~np.isin(triangles,indices)] = -1
        # if 2/3 vertices are outside, flag the face
        occupancyList=np.ones ((triangles.shape[0],1), dtype=bool)

        for idx,row in enumerate(triangles):
            if (row[0] ==-1 and row[1]==-1) or (row[0] ==-1 and row[2]==-1) or (row[1] ==-1 and row[2]==-1):
                occupancyList[idx]=False
        outputmesh.remove_triangles_by_mask(occupancyList)
        outputmesh.remove_unreferenced_vertices()
    return outputmesh

def voxel_traversal(pcd, origin, direction, voxelSize, maxRange = 100): 
    """TO BE TESTED Cast a ray in a voxel array created from the pcd"""

    pcd_Voxel = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=voxelSize)
    #the starting index of the voxels
    voxel_origin = pcd.get_voxel(origin)
    iX = math.floor(origin[0] * voxelSize) / voxelSize
    iY = math.floor(origin[1] * voxelSize) / voxelSize
    iZ = math.floor(origin[2] * voxelSize) / voxelSize

    stepX = np.sign(direction[0])
    stepY = np.sign(direction[1])
    stepZ = np.sign(direction[2])

    tDeltaX = 1/direction[0] * voxelSize
    tDeltaY = 1/direction[1] * voxelSize
    tDeltaZ = 1/direction[2] * voxelSize

    tMaxX = origin[0]
    tMaxY = origin[1]
    tMaxZ = origin[2]

    for i in range(0,maxRange):
        # check if the current point is in a occupied voxel
        if(pcd_Voxel.check_if_included(o3d.utility.Vector3dVector([[iX * voxelSize, iY * voxelSize, iY * voxelSize]]))[0]):
            distance = np.linalg.norm(np.array([iX * voxelSize, iY * voxelSize, iY * voxelSize]) - origin)
            return True, distance

        if(tMaxX < tMaxY):
            if(tMaxX < tMaxZ):
                #traverse in the X direction
                tMaxX += tDeltaX
                iX += stepX
            else:
                #traverse in the Z direction
                tMaxZ += tDeltaZ
                iZ += stepZ
        else:
            if(tMaxY < tMaxZ):
                #traverse in the Y direction
                tMaxY += tDeltaY
                iY += stepY
            else:
                #traverse in the Z direction
                tMaxZ += tDeltaZ
                iZ += stepZ

    return False, math.inf


#### OPEN3D VISUALISATION ####

def create_3d_camera(translation: np.array = [0,0,0], rotation:np.array  = np.eye(3), scale:float = 1.0) -> o3d.geometry:
    "TO BE TESTED Returns a geometry lineset object that represents a camera in 3D space"

    box = o3d.geometry.TriangleMesh.create_box(1.6,0.9, 0.1)
    box.translate((-0.8, -0.45, -0.05))
    box.scale(scale, center=(0, 0, 0))
    box.rotate(rotation)
    box.translate(translation)
    return box

def show_geometries(geometries, color = False):
    "TO BE TESTED displays the array of meshes in a 3D view"

    viewer = o3d.visualization.Visualizer()
    viewer.create_window()
    frame = o3d.geometry.TriangleMesh.create_coordinate_frame()
    viewer.add_geometry(frame)
    for i, geometry in enumerate(geometries):
        if color:
            geometry.paint_uniform_color(matplotlib.colors.hsv_to_rgb([float(i)/len(geometries),0.8,0.8]))
        viewer.add_geometry(geometry)
    opt = viewer.get_render_option()
    opt.background_color = np.asarray([1,1,1])
    opt.light_on = True
    viewer.run()
    viewer.destroy_window()

def save_view_point(geometry: o3d.geometry, filename:str) -> None:
    """Saves the viewpoint of a set of geometry in the given filename.\n

    Args:
        1. geometry (o3d.geometry): geometries to visualize.\n
        2. filename (str): absolute filepath\n
    """
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(geometry)
    vis.run()  # user changes the view and press "q" to terminate
    param = vis.get_view_control().convert_to_pinhole_camera_parameters()
    o3d.io.write_pinhole_camera_parameters(filename, param)
    vis.destroy_window()
