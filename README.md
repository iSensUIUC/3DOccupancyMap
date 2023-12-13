# 3D Occupancy Map
The python file occupancy_ply.py contrains two functions, is_occupied and is_occupied_2. Both of these functions take a point cloud, coordinates, and a threshold (representing the grid size) as inputs, and return whether there is a point within the space centered around the given coordinates, within a radius equal to the threshold. 

Usage: python occupancy_ply.py <function_name> <x> <y> <z> <file_name> <threshold>
where x,y,z are coordinates of point in meter, file_name is the point cloud file.
