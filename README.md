## 3D Occupancy Map

The `occupancy_ply.py` script contains two functions, `is_occupied` and `is_occupied_2`. These functions are designed to process a point cloud and determine whether a specified space, centered around given coordinates, contains any points within a defined threshold radius.

### Usage

To use the script, execute the following command in your terminal:

```bash
python occupancy_ply.py <function_name> <x> <y> <z> <file_name> <threshold>
```
- `<function_name>`: The name of the function to use (`is_occupied` or `is_occupied_2`).
- `<x>`, `<y>`, `<z>`: The coordinates of the point in meters.
- `<file_name>`: The name of the point cloud file.
- `<threshold>`: The radius of the space around the coordinates (in meters) within which the presence of points is checked.

