import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt
import sys

def is_occupied(input_point, point_cloud, threshold=0.05):
    points = np.asarray(point_cloud.points)
    min_bound = points.min(axis=0)
    max_bound = points.max(axis=0)
    # Check if the input point is out of bounds
    if np.any(input_point < min_bound) or np.any(input_point > max_bound):
        print("out of bound")
        return 0

    # Check if any point in the cloud is within the threshold distance 
    distance = np.linalg.norm(points - input_point, axis=1)
    return np.any(distance <= threshold)

def is_occupied_2(input_point, point_cloud, threshold=0.05):
    points = np.asarray(point_cloud.points)
    min_bound = points.min(axis=0)
    max_bound = points.max(axis=0)

    grid_dims = np.ceil((max_bound - min_bound) / threshold).astype(int)
    occupancy_grid = np.zeros(grid_dims)
    
    # use precalculation for these part
    for point in points:
        grid_coord = np.floor((point - min_bound) / threshold).astype(int)
        if (grid_coord >= 0).all() and (grid_coord < grid_dims).all():
            occupancy_grid[tuple(grid_coord)] = 1  # Mark as occupied

    input_grid_coord = np.floor((input_point - min_bound) / threshold).astype(int)
    if (input_grid_coord >= 0).all() and (input_grid_coord < grid_dims).all():
        return occupancy_grid[tuple(input_grid_coord)]
    else:
        print("Point out of bound")
        return 0
    

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python occupancy_ply.py <function_name> <x> <y> <z> <file_name> <threshold>")
        sys.exit(1)

    function_name = sys.argv[1]

    try:
        x = float(sys.argv[2])
        y = float(sys.argv[3])
        z = float(sys.argv[4])
        file_name = sys.argv[5]
        threshold = float(sys.argv[6])
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)
    point = np.array([x,y,z])
    try:
        pcd = o3d.io.read_point_cloud(file_name)
    except Exception as e:
        print(f"Incorrect address or file could not be read: {e}")

    if function_name == "is_occupied":
        occupied = is_occupied(point, pcd, threshold)
    elif function_name == "is_occupied_2":
        occupied = is_occupied_2(point, pcd, threshold)
    else:
        print("Invalid function name. Use 'function1' or 'function2'.")
        sys.exit(1)

    if occupied:
        print("The point is occupied.")
    else:
        print("The point isn't occupied.")